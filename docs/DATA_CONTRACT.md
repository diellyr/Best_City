# Contrato de coleta

Cada lote é uma lista JSON. Todo registro contém:

```json
{
  "kind": "aqi",
  "city": "Jaguariúna",
  "collected_at": "2026-08-13T12:00:00-03:00",
  "source": "Nome da fonte",
  "url": "https://fonte.example/leitura",
  "confidence": "Alta confiança",
  "evidence_type": "fato",
  "data": {}
}
```

`kind` aceita `cidade`, `bairro`, `aqi`, `seguranca`, `venda`, `aluguel` e
`ranking`. Confiança aceita `Alta confiança`, `Média confiança` e
`Baixa confiança`; evidência aceita `fato`, `estimativa` e `inferência`.

## Campos recomendados por tipo

- `aqi`: `aqi`, `escala`, `classificacao`, `pm25`, `medido_em`, `origem`
  (`estacao`, `modelo` ou `interpolacao`).
- `seguranca`: `indicador`, `contagem`, `taxa_100_mil`, `periodo`,
  `populacao_referencia`.
- `bairro`: `bairro`, notas e justificativas dos critérios, `ponto_forte`,
  `ponto_fraco`, `faixa_preco` e oferta observada.
- `venda`: `bairro`, `tipo`, `preco`, `quartos`, `suites`, `banheiros`,
  `vagas`, `area_construida`, `area_terreno`, `condominio`, `iptu`,
  `anuncio_publicado_em`, `status` e `suspeito`.
- `aluguel`: `bairro`, `tipo`, `aluguel`, `quartos`, `condominio`,
  `iptu_mensal`, `custo_total`, `area`, `vagas`, `status`.
- `ranking`: nove notas com as chaves descritas em `buscalar/config.py`,
=======
  justificativa e IDs/URLs das evidências.

Valores desconhecidos devem ser a string `Não confirmado`, nunca `0`. Para
aluguel, `custo_total` só pode ser calculado quando aluguel, condomínio e IPTU
mensal estiverem confirmados; caso contrário também é `Não confirmado`.
