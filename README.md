# BuscaLar

Agente de pesquisa auditável para comparar cidades do interior de São Paulo para
moradia familiar. O projeto transforma a pesquisa em etapas independentes
(qualidade do ar, segurança, bairros, imóveis, mobilidade, topografia e
infraestrutura), preserva todas as coletas e só calcula rankings com evidências
rastreáveis.

## Início rápido

```bash
python -m buscalar init
python -m buscalar plan
python -m buscalar validate examples/coleta-exemplo.json
python -m buscalar ingest examples/coleta-exemplo.json
python -m buscalar report
```

`plan` cria, em `reports/`, um plano de pesquisa com prompts específicos para
cada agente. Depois de executar as pesquisas com ferramentas de busca e fontes
oficiais, os resultados devem ser importados com `ingest`. O comando `report`
usa apenas os registros armazenados — campos ausentes aparecem como **Não
confirmado**, nunca são estimados silenciosamente.

## Princípios

- as 15 cidades obrigatórias nunca são excluídas;
- toda observação exige fonte, URL, instante de coleta e nível de confiança;
- anúncios são validados e deduplicados antes de entrar no histórico;
- snapshots são imutáveis e identificados por timestamp;
- notas ausentes não viram zero: o relatório mostra cobertura e limitações;
- fatos, estimativas e inferências recebem rótulos explícitos;
- a recomendação é produzida pela fórmula configurada, não por preferência do
  agente.

Veja [a especificação operacional](docs/AGENT.md) e o
[contrato de coleta](docs/DATA_CONTRACT.md).

## Testes

```bash
pytest -q
```
