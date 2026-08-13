from __future__ import annotations

REQUIRED_CITIES = (
    "Jaguariúna", "Holambra", "Vinhedo", "Valinhos", "Indaiatuba",
    "Jundiaí", "Nova Odessa", "Santa Bárbara d'Oeste", "São Roque",
    "Itu", "Araçoiaba da Serra", "Porto Feliz", "Iperó", "Tatuí",
    "Votorantim",
)

WEIGHTS = {
    "seguranca": 0.20,
    "qualidade_ar": 0.15,
    "compra_imoveis": 0.15,
    "aluguel": 0.10,
    "qualidade_bairros": 0.10,
    "acesso_paulista": 0.10,
    "topografia": 0.05,
    "infraestrutura": 0.10,
    "proximidade": 0.05,
}

AGENTS = {
    "air-quality": "AQI atual, PM2.5, estação/modelo e histórico sazonal",
    "security": "SSP-SP, Seade, IBGE e Atlas da Violência, com taxas comparáveis",
    "neighborhood": "dez bairros por cidade e critérios familiares auditáveis",
    "sale": "casas ativas de 3+ quartos até R$ 500 mil em múltiplas fontes",
    "rental": "locações de 3+ quartos até R$ 3 mil e custo mensal total",
    "real-estate-analysis": "comparação comprar versus alugar",
    "mobility": "tempos realistas a Campinas, Sorocaba e Avenida Paulista",
    "terrain": "relevo municipal e topografia dos bairros",
    "infrastructure": "saúde, educação, serviços, emprego, fibra e acessos",
    "ranking": "normalização, cobertura, notas e ranking ponderado",
    "report": "relatório final com fatos, estimativas, inferências e confiança",
}

DATASETS = {
    "cidade": "cidades.json",
    "bairro": "bairros.json",
    "aqi": "aqi-history.json",
    "seguranca": "seguranca.json",
    "venda": "imoveis-venda.json",
    "aluguel": "imoveis-aluguel.json",
    "ranking": "ranking-history.json",
}
