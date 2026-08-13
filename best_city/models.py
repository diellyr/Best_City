from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any
from urllib.parse import urlparse

VALID_CONFIDENCE = {"Alta confiança", "Média confiança", "Baixa confiança"}
VALID_KINDS = {"cidade", "bairro", "aqi", "seguranca", "venda", "aluguel", "ranking"}
VALID_EVIDENCE = {"fato", "estimativa", "inferência"}


class ValidationError(ValueError):
    pass


@dataclass(frozen=True)
class Observation:
    kind: str
    city: str
    collected_at: str
    source: str
    url: str
    confidence: str
    evidence_type: str
    data: dict[str, Any]

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Observation":
        required = {"kind", "city", "collected_at", "source", "url", "confidence", "evidence_type", "data"}
        missing = sorted(required - value.keys())
        if missing:
            raise ValidationError(f"Campos obrigatórios ausentes: {', '.join(missing)}")
        item = cls(**{key: value[key] for key in required})
        item.validate()
        return item

    def validate(self) -> None:
        if self.kind not in VALID_KINDS:
            raise ValidationError(f"Tipo de registro inválido: {self.kind}")
        if self.confidence not in VALID_CONFIDENCE:
            raise ValidationError(f"Confiança inválida: {self.confidence}")
        if self.evidence_type not in VALID_EVIDENCE:
            raise ValidationError(f"Tipo de evidência inválido: {self.evidence_type}")
        try:
            parsed_time = datetime.fromisoformat(self.collected_at.replace("Z", "+00:00"))
        except ValueError as exc:
            raise ValidationError("collected_at deve estar em ISO 8601") from exc
        if parsed_time.tzinfo is None:
            raise ValidationError("collected_at deve incluir fuso horário")
        parsed_url = urlparse(self.url)
        if parsed_url.scheme not in {"http", "https"} or not parsed_url.netloc:
            raise ValidationError("url deve ser HTTP(S) completa")
        if not self.city.strip() or not self.source.strip() or not isinstance(self.data, dict):
            raise ValidationError("city, source e data são obrigatórios")
        if self.kind in {"venda", "aluguel"}:
            self._validate_property()

    def _validate_property(self) -> None:
        required = {"bairro", "tipo", "quartos", "preco" if self.kind == "venda" else "aluguel"}
        missing = sorted(required - self.data.keys())
        if missing:
            raise ValidationError(f"Imóvel sem: {', '.join(missing)}")
        if self.data["quartos"] < 3:
            raise ValidationError("Imóvel deve ter ao menos 3 quartos")
        if self.kind == "venda":
            if self.data["tipo"].casefold() != "casa":
                raise ValidationError("Pesquisa principal de venda aceita apenas casa")
            if self.data["preco"] > 500_000:
                raise ValidationError("Venda excede R$ 500 mil")
        if self.kind == "aluguel" and self.data["aluguel"] > 3_000:
            raise ValidationError("Aluguel excede R$ 3 mil")

    @property
    def identity(self) -> tuple[Any, ...]:
        if self.kind not in {"venda", "aluguel"}:
            return (self.kind, self.city.casefold(), self.collected_at, self.url)
        value = self.data.get("preco", self.data.get("aluguel"))
        return (
            self.kind, self.city.casefold(), str(self.data.get("bairro", "")).casefold(),
            self.data.get("tipo", "").casefold(), self.data.get("quartos"), value,
            self.data.get("area_construida", self.data.get("area")),
        )
