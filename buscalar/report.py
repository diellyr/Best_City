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
    lines = ["# Relatório BuscaLar", "", f"Gerado em {datetime.now(timezone.utc).isoformat()}", ""]
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
        return f"Há {len(selected)} anúncio(s) validado(s) no snapshot. A exportação detalhada permanece nos arquivos JSON auditáveis."
    return "**Pendente de síntese:** há dados importados, mas esta versão não afirma conclusões sem cobertura completa das 15 cidades."
