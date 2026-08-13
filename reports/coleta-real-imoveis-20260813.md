# Coleta real de imóveis — 13 de agosto de 2026

## Resultado executivo

Foi localizada e conferida uma casa real em **Itu**, uma das 15 cidades da
pesquisa. O imóvel tem três quartos, mas custa R$ 630 mil e, portanto, **não
entra** na lista final limitada a R$ 500 mil. Nenhuma casa que simultaneamente
atendesse a 3+ quartos, preço de até R$ 500 mil e disponibilidade verificável
foi encontrada nas fontes que puderam ser abertas nesta rodada.

Não relaxei os filtros e não transformei apartamento, imóvel acima do teto ou
anúncio inacessível em recomendação de casa.

## Casa conferida

| Cidade | Bairro | Quartos | Suítes | Banheiros | Vagas | Área útil | Terreno | Preço | Resultado |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| Itu | Liberdade | 3 | 1 | 3 | 2 | 112 m² | 200 m² | R$ 630.000 | Excluída: R$ 130.000 acima do teto |

**Anúncio:** [Casa ampla, linda, sem retoques](https://www.imoveis-itu-salto.com.br/imoveis/casa-ampla-linda-sem-rotoques/).

**Evidência auditável:** [dados estruturados mantidos pelo anunciante](https://github.com/Marcio-itu/Imoveis-Itu-Salto-Indaiatuba/blob/28016a4829524e1fe10aecb0bf690deedc3f770c/imoveis/casa-ampla-linda-sem-rotoques/dados.json).

- Referência do anúncio: `OVO01016`.
- Tipo de operação: venda.
- Data declarada de publicação: 10 de agosto de 2026.
- Fonte: site do corretor Marcio Santos, CRECI-SP 276471-F.
- Coleta: 13 de agosto de 2026, 15:20 UTC.
- Confiança: **média**. Os dados estruturados, fotos e página gerada estão no
  repositório público do anunciante; o domínio comercial não pôde ser reaberto
  pelo proxy desta execução.
- Integridade da cópia coletada: SHA-256
  `ec3ffed11d783ed4476aa7af68d41b99d33d4cbbff1144e690845a66ce18002a`.

## Validação dos critérios

| Critério | Exigência | Observado | Situação |
|---|---|---|---|
| Cidade obrigatória | Uma das 15 cidades | Itu | Atende |
| Tipo | Casa | Casa | Atende |
| Quartos | 3 ou mais | 3 | Atende |
| Preço | Até R$ 500.000 | R$ 630.000 | **Não atende** |
| Link individual | Obrigatório | Disponível | Atende |
| Dados e fotos | Conferíveis | Disponíveis na fonte | Atende |

## Fontes pesquisadas e limitações

Também foram tentadas consultas ao Viva Real, OLX, Imovelweb, Chaves na Mão e
Mercado Livre. O proxy respondeu `403 Forbidden` antes de abrir esses domínios,
e a busca web integrada respondeu `401 Unauthorized`. O repositório público do
anunciante no GitHub foi acessível e permitiu conferir os dados acima.

Este é um relatório de coleta real, mas **não é uma recomendação de compra**.
Preço, documentação e disponibilidade devem ser reconfirmados diretamente com
o corretor antes de visita ou proposta.
