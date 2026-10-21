# Para quem — Crianças, Agricultura e Animais

Revisão de 21 de outubro de 2026.

## Auditoria e implementação

Foram revistos conteudos/publicos.py, o índice e os oito guias existentes,
public_listing/public_article/dados_publicos e a pesquisa em scripts/gerar.py,
o catálogo de artigos, os estilos de cartões e leitura, caminhos de imagens,
créditos e testes. Não havia página equivalente aos três temas. Escolas é um
contexto educativo; não foi substituído nem duplicado integralmente por Crianças.

Foram criadas as rotas publicos/criancas.html, publicos/agricultura.html e
publicos/animais.html. O índice tem onze cartões. Os oito HTML anteriores
permanecem sem diferenças de conteúdo em relação ao Git antes da tarefa.
Não se alterou CSS, menu global ou outras secções.

Os novos dados vivem em conteudos/publicos_novos.py e entram em PUBLICOS pelo
módulo existente. O gerador suporta campos opcionais de personalização, cuidados
e bibliografia apenas nos novos guias. Mantém o comportamento anterior nos
restantes. O JSON e a pesquisa incluem os novos campos. As datas de revisão
dos artigos antigos não foram alteradas; o JSON indica a revisão mais recente.

As famílias são justificadas pelo destinatário, função e ocasião, sem promessas
de resultados ou popularidade. Crianças distingue acompanhamento e utilização
prevista de certificação; Agricultura separa comunicação, ferramentas e EPI;
Animais distingue os destinatários humanos dos utilizadores animais.

## Fontes consultadas e respetivo âmbito

Todas as cinco fontes efetivamente usadas estão registadas em FONTES de
conteudos/publicos_novos.py, com URL, data e âmbito, e aparecem nos três guias.
As afirmações pertinentes têm ligações inline.

- Comissão Europeia, Toy Safety in the EU:
  https://single-market-economy.ec.europa.eu/sectors/toys/toy-safety_en
  Enquadramento específico de brinquedos; não classifica os artigos ilustrados.
  A página inclui o período de transição do novo regulamento. Não se publicou
  uma descrição jurídica desatualizada nem se atribuiu certificação aos exemplos.
- Comissão Europeia, Toy Safety Tips, PDF de três páginas:
  https://ec.europa.eu/docsroom/documents/6791/attachments/1/translations
  Idade, capacidades, peças pequenas, instruções, supervisão e desgaste de
  brinquedos. Não se estende a todos os produtos infantis nem se atribui uma
  idade aos lápis ou ao objeto de jogo fotografados.
- Comissão Europeia, Personal protective equipment:
  https://single-market-economy.ec.europa.eu/sectors/mechanical-engineering/personal-protective-equipment-ppe_en
  Finalidade de proteção e enquadramento de EPI. Não demonstra proteção de
  bonés ou vestuário promocional e não certifica o acessório ilustrado.
- HSE, Children and public safety:
  https://www.hse.gov.uk/agriculture/topics/children.htm
  Riscos para crianças e visitantes de explorações. Não se transportaram
  idades legais ou disposições britânicas para o contexto português.
- UK Pet Food, Choking Hazards, ficha publicada em 2019:
  https://www.ukpetfood.org/static/65de2abb-a72d-4d6f-8a4b638b53087fb9/25c59779-b16c-414a-8ed87b154cce6391/Choking-Hazards.pdf
  Associação setorial, não organismo certificador. Consultou-se a orientação
  sobre brinquedos para cães: dimensões, desgaste e supervisão. Não se usaram
  recomendações alimentares nem se extrapolou para coleiras, recipientes ou
  outras espécies. Não se garante segurança de nenhum exemplo.

Tentativas de consulta da ASAE e de outra página veterinária tiveram limitações
de acesso; não foram usadas como base de afirmações não verificadas. Não se
usou Excel como fonte, nem se copiaram textos ou fotografias externas.

## Imagens inspecionadas

A pasta real é assets/para_quem; não se criou assets/paraquem. Foram percorridas
as subpastas e inspecionados os nove ficheiros novos numa folha de contacto.
As cinco imagens escolhidas têm aliases sem marcas ou referências comerciais.
Originais, dimensões e SHA-256 estão em publicos-novos-imagens.json.

| Tema | Cartão | Corpo |
| --- | --- | --- |
| Crianças | Estojo de lápis de cor | Objeto de jogo com cordão, sem idade ou material inferidos |
| Agricultura | Acessório dobrável com lâmina | O mesmo exemplo, com legenda explícita sobre o limite profissional e o destinatário adulto |
| Animais | Dispensadores de sacos para o tutor | Coleira, sem alegações de visibilidade, resistência ou aptidão |

Agricultura tem uma limitação visual: não há fotografia representativa de
feira, formação, bonés ou cadernos nessa pasta. O acessório é apresentado como
exemplo pessoal para adultos, não ferramenta de trabalho nem artigo a distribuir
indiscriminadamente em visitas. O conjunto de mesa foi excluído por ter marca
visível e menor relação com o foco editorial. Em Animais, foram excluídas imagens
de recipiente e conjunto com marcas ou alegações impressas; não se repetiram
essas alegações como características. A fotografia da peça vestível de Crianças
não acrescentava explicação necessária e não foi usada.

Os créditos foram acrescentados à página existente e mantêm autoria e licença
individual como não identificadas; não se inventou licença aberta ou autor.

## Verificação

- python scripts/gerar.py --secao publicos: onze artigos, entrada, pesquisa,
  exportação estruturada e créditos atualizados.
- npm.cmd run check: todos os verificadores aprovados, incluindo estrutura,
  públicos, imagens, Produtos e regressão das outras secções.
- 117 páginas e 4501 ligações/recursos locais válidos.
- 232 utilizações de imagens e 133 ficheiros decodificados, dimensões e alt válidos.
- Doze testes de pesquisa, agora com consultas para os três temas, aprovados.
- Integridade binária das cinco cópias confirmada; nenhuma transformação.
- Formatação HTML aprovada.

A ferramenta de navegador devolveu uma lista vazia nesta execução. Não se
afirma revisão visual do layout; os componentes e breakpoints anteriores foram
reutilizados. A seleção das fotografias foi inspecionada visualmente.

Permanecem dependentes do artigo concreto a idade indicada, composição,
certificação, aptidão profissional, resistência à mordida e contacto com alimentos.
Estas informações não foram inventadas. Sem commit, push ou publicação.
