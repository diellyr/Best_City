from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from .config import DATASETS
from .models import Observation


class AppendOnlyStore:
    def __init__(self, root: str | Path = ".") -> None:
        self.root = Path(root)
        self.data_dir = self.root / "data"
        self.reports_dir = self.root / "reports"

    def initialize(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.reports_dir.mkdir(parents=True, exist_ok=True)
        for filename in DATASETS.values():
            path = self.data_dir / filename
            if not path.exists():
                path.write_text("[]\n", encoding="utf-8")

    def ingest(self, observations: Iterable[Observation]) -> tuple[int, int]:
        self.initialize()
        accepted = duplicates = 0
        grouped: dict[str, list[Observation]] = {}
        for item in observations:
            grouped.setdefault(item.kind, []).append(item)
        for kind, incoming in grouped.items():
            path = self.data_dir / DATASETS[kind]
            current = json.loads(path.read_text(encoding="utf-8"))
            identities = {Observation.from_dict(row).identity for row in current}
            for item in incoming:
                if item.identity in identities:
                    duplicates += 1
                    continue
                current.append(asdict(item))
                identities.add(item.identity)
                accepted += 1
            self._atomic_write(path, current)
        return accepted, duplicates

    def load_all(self) -> list[Observation]:
        self.initialize()
        result: list[Observation] = []
        for filename in DATASETS.values():
            rows = json.loads((self.data_dir / filename).read_text(encoding="utf-8"))
            result.extend(Observation.from_dict(row) for row in rows)
        return result

    def write_report(self, stem: str, body: str) -> Path:
        self.initialize()
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        path = self.reports_dir / f"{stem}-{timestamp}.md"
        path.write_text(body, encoding="utf-8")
        return path

    @staticmethod
    def _atomic_write(path: Path, rows: list[dict]) -> None:
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temporary.replace(path)
