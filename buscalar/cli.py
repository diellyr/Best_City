from __future__ import annotations

import argparse
import json
from pathlib import Path

from .models import Observation, ValidationError
from .prompts import research_plan
from .report import render_report
from .storage import AppendOnlyStore


def _read(path: str) -> list[Observation]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValidationError("O arquivo de coleta deve conter uma lista JSON")
    return [Observation.from_dict(row) for row in payload]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="buscalar", description="Agente comparativo de cidades de SP")
    parser.add_argument("--root", default=".", help="diretório de dados e relatórios")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init", help="cria os arquivos históricos sem sobrescrever dados")
    commands.add_parser("plan", help="gera prompts dos agentes de pesquisa")
    for command in ("validate", "ingest"):
        child = commands.add_parser(command, help=f"{command} uma coleta JSON")
        child.add_argument("file")
    commands.add_parser("report", help="gera relatório de cobertura com dados validados")
    args = parser.parse_args(argv)
    store = AppendOnlyStore(args.root)
    try:
        if args.command == "init":
            store.initialize()
            print("Estrutura inicializada sem sobrescrever o histórico.")
        elif args.command == "plan":
            path = store.write_report("plano-pesquisa", research_plan())
            print(path)
        elif args.command == "validate":
            items = _read(args.file)
            print(f"{len(items)} registro(s) válido(s).")
        elif args.command == "ingest":
            accepted, duplicates = store.ingest(_read(args.file))
            print(f"{accepted} incluído(s); {duplicates} duplicado(s) ignorado(s).")
        elif args.command == "report":
            path = store.write_report("relatorio", render_report(store.load_all()))
            print(path)
    except (OSError, json.JSONDecodeError, ValidationError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
