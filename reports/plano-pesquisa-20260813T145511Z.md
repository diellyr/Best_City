# Plano de execução — Best City SP

Gerado em: 2026-08-13T14:55:11.065751+00:00

Cidades obrigatórias: Jaguariúna, Holambra, Vinhedo, Valinhos, Indaiatuba, Jundiaí, Nova Odessa, Santa Bárbara d'Oeste, São Roque, Itu, Araçoiaba da Serra, Porto Feliz, Iperó, Tatuí, Votorantim



## OrchestratorAgent

Execute os agentes abaixo, valide cada lote, deduplique imóveis, calcule as notas apenas após cobertura suficiente e encaminhe tudo ao ReportAgent.

Regras obrigatórias:
- Pesquise na web no momento da execução e registre links diretos, fonte e horário ISO 8601 com fuso.
- Não invente nem complete lacunas. Use exatamente 'Não confirmado'.
- Rotule cada conclusão como fato, estimativa ou inferência e dê confiança Alta, Média ou Baixa.
- Para dado atual, confirme que a página/anúncio continua ativo. Prefira fonte primária/oficial.
- Mantenha todas as cidades obrigatórias, mesmo quando a nota for baixa.
- Retorne JSON conforme docs/DATA_CONTRACT.md; não retorne prosa sem evidência.


## air-quality

Missão: AQI atual, PM2.5, estação/modelo e histórico sazonal.

Informe AQI exato, escala, classe, PM2.5, horário, estação física ou modelo. Separe retrato atual de sazonalidade, inverno, seca, queimadas, indústria e tráfego.

Regras obrigatórias:
- Pesquise na web no momento da execução e registre links diretos, fonte e horário ISO 8601 com fuso.
- Não invente nem complete lacunas. Use exatamente 'Não confirmado'.
- Rotule cada conclusão como fato, estimativa ou inferência e dê confiança Alta, Média ou Baixa.
- Para dado atual, confirme que a página/anúncio continua ativo. Prefira fonte primária/oficial.
- Mantenha todas as cidades obrigatórias, mesmo quando a nota for baixa.
- Retorne JSON conforme docs/DATA_CONTRACT.md; não retorne prosa sem evidência.


## security

Missão: SSP-SP, Seade, IBGE e Atlas da Violência, com taxas comparáveis.

Colete homicídios, roubos, furtos e roubo de veículos; preserve período, contagem, denominador e taxa por 100 mil. Não compare períodos incompatíveis.

Regras obrigatórias:
- Pesquise na web no momento da execução e registre links diretos, fonte e horário ISO 8601 com fuso.
- Não invente nem complete lacunas. Use exatamente 'Não confirmado'.
- Rotule cada conclusão como fato, estimativa ou inferência e dê confiança Alta, Média ou Baixa.
- Para dado atual, confirme que a página/anúncio continua ativo. Prefira fonte primária/oficial.
- Mantenha todas as cidades obrigatórias, mesmo quando a nota for baixa.
- Retorne JSON conforme docs/DATA_CONTRACT.md; não retorne prosa sem evidência.


## neighborhood

Missão: dez bairros por cidade e critérios familiares auditáveis.

Avalie 10 bairros reais por cidade em segurança, escolas, saúde, comércio, vias, transporte, urbanismo, tranquilidade, verde, relevo, centro, rodovias, oferta, preço e crianças. Explique força e fraqueza.

Regras obrigatórias:
- Pesquise na web no momento da execução e registre links diretos, fonte e horário ISO 8601 com fuso.
- Não invente nem complete lacunas. Use exatamente 'Não confirmado'.
- Rotule cada conclusão como fato, estimativa ou inferência e dê confiança Alta, Média ou Baixa.
- Para dado atual, confirme que a página/anúncio continua ativo. Prefira fonte primária/oficial.
- Mantenha todas as cidades obrigatórias, mesmo quando a nota for baixa.
- Retorne JSON conforme docs/DATA_CONTRACT.md; não retorne prosa sem evidência.


## sale

Missão: casas ativas de 3+ quartos até R$ 500 mil em múltiplas fontes.

Aceite somente casas, 3+ quartos e até R$ 500 mil. Capture suíte, banheiros, vagas, áreas, bairro, condomínio, IPTU, data, URL e indícios de anúncio suspeito. Cruze Viva Real, ZAP, Imovelweb, OLX, Chaves na Mão e imobiliárias locais.

Regras obrigatórias:
- Pesquise na web no momento da execução e registre links diretos, fonte e horário ISO 8601 com fuso.
- Não invente nem complete lacunas. Use exatamente 'Não confirmado'.
- Rotule cada conclusão como fato, estimativa ou inferência e dê confiança Alta, Média ou Baixa.
- Para dado atual, confirme que a página/anúncio continua ativo. Prefira fonte primária/oficial.
- Mantenha todas as cidades obrigatórias, mesmo quando a nota for baixa.
- Retorne JSON conforme docs/DATA_CONTRACT.md; não retorne prosa sem evidência.


## rental

Missão: locações de 3+ quartos até R$ 3 mil e custo mensal total.

Busque 3+ quartos e aluguel-base até R$ 3 mil; separe casa/apartamento. Calcule aluguel + condomínio + IPTU mensalizado, sem tratar campo ausente como zero.

Regras obrigatórias:
- Pesquise na web no momento da execução e registre links diretos, fonte e horário ISO 8601 com fuso.
- Não invente nem complete lacunas. Use exatamente 'Não confirmado'.
- Rotule cada conclusão como fato, estimativa ou inferência e dê confiança Alta, Média ou Baixa.
- Para dado atual, confirme que a página/anúncio continua ativo. Prefira fonte primária/oficial.
- Mantenha todas as cidades obrigatórias, mesmo quando a nota for baixa.
- Retorne JSON conforme docs/DATA_CONTRACT.md; não retorne prosa sem evidência.


## real-estate-analysis

Missão: comparação comprar versus alugar.

Por cidade, use medianas, relação aluguel/preço anual, número de anúncios deduplicados e qualidade dos bairros. Explicite limitações de amostra.

Regras obrigatórias:
- Pesquise na web no momento da execução e registre links diretos, fonte e horário ISO 8601 com fuso.
- Não invente nem complete lacunas. Use exatamente 'Não confirmado'.
- Rotule cada conclusão como fato, estimativa ou inferência e dê confiança Alta, Média ou Baixa.
- Para dado atual, confirme que a página/anúncio continua ativo. Prefira fonte primária/oficial.
- Mantenha todas as cidades obrigatórias, mesmo quando a nota for baixa.
- Retorne JSON conforme docs/DATA_CONTRACT.md; não retorne prosa sem evidência.


## mobility

Missão: tempos realistas a Campinas, Sorocaba e Avenida Paulista.

Estime porta a porta em faixas, incluindo espera, caminhada e integrações. Destinos: Campinas, Sorocaba e Trianon-Masp/Consolação. Registre cenário, dia e horário.

Regras obrigatórias:
- Pesquise na web no momento da execução e registre links diretos, fonte e horário ISO 8601 com fuso.
- Não invente nem complete lacunas. Use exatamente 'Não confirmado'.
- Rotule cada conclusão como fato, estimativa ou inferência e dê confiança Alta, Média ou Baixa.
- Para dado atual, confirme que a página/anúncio continua ativo. Prefira fonte primária/oficial.
- Mantenha todas as cidades obrigatórias, mesmo quando a nota for baixa.
- Retorne JSON conforme docs/DATA_CONTRACT.md; não retorne prosa sem evidência.


## terrain

Missão: relevo municipal e topografia dos bairros.

Use mapas/altimetria e fontes públicas; classifique Muito plana, Plana, Moderadamente ondulada, Acidentada ou Muito acidentada, distinguindo município e bairro.

Regras obrigatórias:
- Pesquise na web no momento da execução e registre links diretos, fonte e horário ISO 8601 com fuso.
- Não invente nem complete lacunas. Use exatamente 'Não confirmado'.
- Rotule cada conclusão como fato, estimativa ou inferência e dê confiança Alta, Média ou Baixa.
- Para dado atual, confirme que a página/anúncio continua ativo. Prefira fonte primária/oficial.
- Mantenha todas as cidades obrigatórias, mesmo quando a nota for baixa.
- Retorne JSON conforme docs/DATA_CONTRACT.md; não retorne prosa sem evidência.


## infrastructure

Missão: saúde, educação, serviços, emprego, fibra e acessos.

Verifique hospitais, PA, escolas, mercados, shopping, comércio, restaurantes, fibra, universidades, empregos, aeroportos e rodovias; não confunda proximidade com presença municipal.

Regras obrigatórias:
- Pesquise na web no momento da execução e registre links diretos, fonte e horário ISO 8601 com fuso.
- Não invente nem complete lacunas. Use exatamente 'Não confirmado'.
- Rotule cada conclusão como fato, estimativa ou inferência e dê confiança Alta, Média ou Baixa.
- Para dado atual, confirme que a página/anúncio continua ativo. Prefira fonte primária/oficial.
- Mantenha todas as cidades obrigatórias, mesmo quando a nota for baixa.
- Retorne JSON conforme docs/DATA_CONTRACT.md; não retorne prosa sem evidência.


## ranking

Missão: normalização, cobertura, notas e ranking ponderado.

Atribua 0–10 por categoria com justificativa e IDs das evidências. Não puna dado ausente com zero; exiba cobertura. Preserve os pesos fornecidos.

Regras obrigatórias:
- Pesquise na web no momento da execução e registre links diretos, fonte e horário ISO 8601 com fuso.
- Não invente nem complete lacunas. Use exatamente 'Não confirmado'.
- Rotule cada conclusão como fato, estimativa ou inferência e dê confiança Alta, Média ou Baixa.
- Para dado atual, confirme que a página/anúncio continua ativo. Prefira fonte primária/oficial.
- Mantenha todas as cidades obrigatórias, mesmo quando a nota for baixa.
- Retorne JSON conforme docs/DATA_CONTRACT.md; não retorne prosa sem evidência.


## report

Missão: relatório final com fatos, estimativas, inferências e confiança.

Gere as 14 partes pedidas, tabelas consolidadas e seleções baseadas na fórmula. Qualquer recomendação deve citar evidências, cobertura e data de validade dos anúncios.

Regras obrigatórias:
- Pesquise na web no momento da execução e registre links diretos, fonte e horário ISO 8601 com fuso.
- Não invente nem complete lacunas. Use exatamente 'Não confirmado'.
- Rotule cada conclusão como fato, estimativa ou inferência e dê confiança Alta, Média ou Baixa.
- Para dado atual, confirme que a página/anúncio continua ativo. Prefira fonte primária/oficial.
- Mantenha todas as cidades obrigatórias, mesmo quando a nota for baixa.
- Retorne JSON conforme docs/DATA_CONTRACT.md; não retorne prosa sem evidência.


## Pesos

- seguranca: 20%

- qualidade_ar: 15%

- compra_imoveis: 15%

- aluguel: 10%

- qualidade_bairros: 10%

- acesso_paulista: 10%

- topografia: 5%

- infraestrutura: 10%

- proximidade: 5%
