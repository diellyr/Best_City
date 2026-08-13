from __future__ import annotations

from dataclasses import dataclass

from .config import WEIGHTS


@dataclass(frozen=True)
class Score:
    final: float | None
    coverage: float
    missing: tuple[str, ...]


def weighted_score(values: dict[str, float | None]) -> Score:
    """Calcula a nota sem converter dados ausentes em desempenho ruim.

    A nota é normalizada pelos pesos cobertos e a cobertura é exibida à parte.
    """
    unknown = tuple(key for key in WEIGHTS if values.get(key) is None)
    covered_weight = sum(weight for key, weight in WEIGHTS.items() if values.get(key) is not None)
    if covered_weight == 0:
        return Score(None, 0.0, unknown)
    for key, value in values.items():
        if key in WEIGHTS and value is not None and not 0 <= value <= 10:
            raise ValueError(f"Nota de {key} fora do intervalo 0–10")
    total = sum(values[key] * weight for key, weight in WEIGHTS.items() if values.get(key) is not None)
    return Score(round(total / covered_weight, 2), round(covered_weight * 100, 1), unknown)
