# Especificação operacional do agente

## Fluxo

1. **OrchestratorAgent** gera uma rodada identificada por timestamp e distribui
   as 15 cidades a todos os especialistas.
2. Especialistas pesquisam fontes atuais, devolvendo observações no contrato
   JSON. Uma URL de busca não substitui o link direto da evidência.
3. O validador rejeita registros incompletos e imóveis fora dos limites.
4. O armazenamento acrescenta observações ao histórico e elimina duplicações
   conservadoras. Ele nunca altera snapshots anteriores.
5. O RankingAgent só pontua categorias cobertas. A nota normalizada deve sempre
   aparecer junto da porcentagem de cobertura.
6. O ReportAgent produz as 14 partes e deixa lacunas visíveis.

## Política de pesquisa

- **AQI:** declarar a escala (por exemplo, US AQI), poluente, PM2.5, horário da
  leitura e se a origem é estação física, interpolação ou modelo. Uma estação
  de outra cidade não pode ser apresentada como medição local.
- **Segurança:** priorizar SSP-SP, Seade, IBGE e Atlas da Violência. Registrar
  período e população usada; não misturar contagem mensal com taxa anual.
- **Bairros:** somente nomes confirmados por mapas municipais, cadastros ou
  fontes imobiliárias convergentes. Dez bairros por cidade, sem inventar o
  décimo para preencher tabela.
- **Imóveis:** abrir o anúncio, confirmar critérios e marcar campos ausentes
  como `Não confirmado`. Comparar URL, bairro, preço, quartos e área para
  detectar republicações.
- **Mobilidade:** declarar origem, destino, dia, horário e todas as esperas. O
  destino paulistano padrão é Trianon-Masp ou Consolação.
- **Topografia:** distinguir relevo médio municipal das condições da quadra ou
  bairro.

## Critério de publicação

Uma classificação final deve ser retida quando a cobertura ponderada for menor
que 80% em qualquer cidade candidata ao Top 5 ou quando faltar segurança, AQI,
compra ou aluguel. Isso evita precisão artificial. Anúncios são um retrato da
data de coleta, não garantia de disponibilidade futura.

## Saída final

O relatório segue as 14 partes solicitadas, inclui todas as cidades, tabelas de
bairros e imóveis, comparação comprar/alugar, 20 opções destacadas e a seleção
das cinco cidades para visita. Expressões como “melhor” significam sempre
“maior nota conforme os pesos e evidências desta rodada”.
