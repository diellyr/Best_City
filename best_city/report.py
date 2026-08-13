from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone

from .config import REQUIRED_CITIES
from .models import Observation

PARTS = (
    "Resumo executivo", "Ranking completo", "Qualidade do ar", "Segurança",
    "Topografia", "Infraestrutura", "Mobilidade", "Top 10 bairros de cada cidade",
    "Casas de 3 quartos à venda até R$ 500 mil", "Imóveis de 3 quartos para aluguel",
    "Comprar x alugar", "Melhores imóveis encontrados",
    "Pontos positivos e negativos de cada cidade", "Recomendação final",
)


def render_report(items: list[Observation]) -> str:
    counts = Counter((item.city, item.kind) for item in items)
    lines = ["# Relatório Best City SP", "", f"Gerado em {datetime.now(timezone.utc).isoformat()}", ""]
    lines += [
        "> Relatório de cobertura. Recomendações e ranking ficam pendentes até existirem evidências",
        "> validadas suficientes; ausência de dado nunca é convertida em nota zero.", "",
        "## Cobertura por cidade", "",
        "| Cidade | AQI | Segurança | Bairros | Venda | Aluguel | Cidade/infra |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for city in REQUIRED_CITIES:
        lines.append(f"| {city} | {counts[city, 'aqi']} | {counts[city, 'seguranca']} | {counts[city, 'bairro']} | {counts[city, 'venda']} | {counts[city, 'aluguel']} | {counts[city, 'cidade']} |")
    for number, title in enumerate(PARTS, 1):
        lines += ["", f"## Parte {number} — {title}", "", _section_text(number, items)]
    return "\n".join(lines) + "\n"


def _section_text(number: int, items: list[Observation]) -> str:
    if not items:
        return "**Não confirmado:** nenhuma coleta validada foi importada. Execute o plano de pesquisa antes de emitir conclusões."
    if number in {9, 10}:
        kind = "venda" if number == 9 else "aluguel"
        selected = [item for item in items if item.kind == kind]
        if not selected:
            return "**Não confirmado:** não há anúncios validados para esta seção."
        return _property_table(selected, kind)
    return "**Pendente de síntese:** há dados importados, mas esta versão não afirma conclusões sem cobertura completa das 15 cidades."


def _property_table(items: list[Observation], kind: str) -> str:
    """Render validated listings in the report instead of hiding them in JSON."""
    price_key = "preco" if kind == "venda" else "aluguel"
    price_title = "Preço" if kind == "venda" else "Aluguel-base"
    lines = [
        f"{len(items)} anúncio(s) validado(s) no snapshot.", "",
        f"| Cidade | Bairro | Tipo | Quartos | {price_title} | Área | Coleta | Fonte |",
        "|---|---|---|---:|---:|---:|---|---|",
    ]
    for item in sorted(items, key=lambda value: (value.city, value.data[price_key])):
        data = item.data
        area = data.get("area_construida", data.get("area", "Não confirmado"))
        lines.append(
            f"| {_cell(item.city)} | {_cell(data['bairro'])} | {_cell(data['tipo'])} | "
            f"{data['quartos']} | {_money(data[price_key])} | {_area(area)} | "
            f"{_cell(item.collected_at)} | [{_cell(item.source)}]({item.url}) |"
        )
    lines += [
        "",
        "> Os links apontam para os anúncios consultados. Preço e disponibilidade são um retrato da data de coleta.",
    ]
    return "\n".join(lines)


def _money(value: object) -> str:
    if not isinstance(value, (int, float)):
        return _cell(value)
    return f"R$ {value:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")


def _area(value: object) -> str:
    return f"{value} m²" if isinstance(value, (int, float)) else _cell(value)


def _cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")
