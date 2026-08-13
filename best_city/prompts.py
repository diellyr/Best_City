from __future__ import annotations

from datetime import datetime, timezone

from .config import AGENTS, REQUIRED_CITIES, WEIGHTS

COMMON_RULES = """Regras obrigatórias:
- Pesquise na web no momento da execução e registre links diretos, fonte e horário ISO 8601 com fuso.
- Não invente nem complete lacunas. Use exatamente 'Não confirmado'.
- Rotule cada conclusão como fato, estimativa ou inferência e dê confiança Alta, Média ou Baixa.
- Para dado atual, confirme que a página/anúncio continua ativo. Prefira fonte primária/oficial.
- Mantenha todas as cidades obrigatórias, mesmo quando a nota for baixa.
- Retorne JSON conforme docs/DATA_CONTRACT.md; não retorne prosa sem evidência.
"""


def research_plan() -> str:
    now = datetime.now(timezone.utc).isoformat()
    cities = ", ".join(REQUIRED_CITIES)
    sections = [
        "# Plano de execução — Best City SP",
        f"Gerado em: {now}",
        f"Cidades obrigatórias: {cities}",
        "",
        "## OrchestratorAgent",
        "Execute os agentes abaixo, valide cada lote, deduplique imóveis, calcule as notas apenas após cobertura suficiente e encaminhe tudo ao ReportAgent.",
        COMMON_RULES,
    ]
    for name, mission in AGENTS.items():
        sections.extend((f"## {name}", f"Missão: {mission}.", _agent_details(name), COMMON_RULES))
    sections.extend(("## Pesos", *[f"- {key}: {weight:.0%}" for key, weight in WEIGHTS.items()]))
    return "\n\n".join(sections) + "\n"


def _agent_details(name: str) -> str:
    details = {
        "air-quality": "Informe AQI exato, escala, classe, PM2.5, horário, estação física ou modelo. Separe retrato atual de sazonalidade, inverno, seca, queimadas, indústria e tráfego.",
        "security": "Colete homicídios, roubos, furtos e roubo de veículos; preserve período, contagem, denominador e taxa por 100 mil. Não compare períodos incompatíveis.",
        "neighborhood": "Avalie 10 bairros reais por cidade em segurança, escolas, saúde, comércio, vias, transporte, urbanismo, tranquilidade, verde, relevo, centro, rodovias, oferta, preço e crianças. Explique força e fraqueza.",
        "sale": "Aceite somente casas, 3+ quartos e até R$ 500 mil. Capture suíte, banheiros, vagas, áreas, bairro, condomínio, IPTU, data, URL e indícios de anúncio suspeito. Cruze Viva Real, ZAP, Imovelweb, OLX, Chaves na Mão e imobiliárias locais.",
        "rental": "Busque 3+ quartos e aluguel-base até R$ 3 mil; separe casa/apartamento. Calcule aluguel + condomínio + IPTU mensalizado, sem tratar campo ausente como zero.",
        "real-estate-analysis": "Por cidade, use medianas, relação aluguel/preço anual, número de anúncios deduplicados e qualidade dos bairros. Explicite limitações de amostra.",
        "mobility": "Estime porta a porta em faixas, incluindo espera, caminhada e integrações. Destinos: Campinas, Sorocaba e Trianon-Masp/Consolação. Registre cenário, dia e horário.",
        "terrain": "Use mapas/altimetria e fontes públicas; classifique Muito plana, Plana, Moderadamente ondulada, Acidentada ou Muito acidentada, distinguindo município e bairro.",
        "infrastructure": "Verifique hospitais, PA, escolas, mercados, shopping, comércio, restaurantes, fibra, universidades, empregos, aeroportos e rodovias; não confunda proximidade com presença municipal.",
        "ranking": "Atribua 0–10 por categoria com justificativa e IDs das evidências. Não puna dado ausente com zero; exiba cobertura. Preserve os pesos fornecidos.",
        "report": "Gere as 14 partes pedidas, tabelas consolidadas e seleções baseadas na fórmula. Qualquer recomendação deve citar evidências, cobertura e data de validade dos anúncios.",
    }
    return details.get(name, "")
