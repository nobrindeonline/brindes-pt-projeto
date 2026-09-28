# Sublimação — fontes, integração e validações

Revisão documental: 28 de setembro de 2026. Guia permanente, para revisão local.
Página: `tecnicas/tecnica-sublimacao.html`. Conteúdo: `conteudos/sublimacao.py`.
O ID `tecnica-sublimacao` evita colisão com `sublimacao`, já usado pelo guia
`industria/sublimacao.html`, preservado e ligado ao novo artigo.

## Fontes técnicas consultadas

- [Epson — Sublimation Printers for Makers](https://epson.com/sublimation-printers-for-makers):
  poliéster, revestimentos preparados, ausência de tinta branca e influência da cor.
- [Sawgrass — SubliJet](https://www.sawgrassink.com/sublijet/): transferência com calor,
  impressora/tinta/papel e artigos preparados para sublimação.
- [Sawgrass Care — Sublimation Heat Press Settings](https://care.sawgrassink.com/hc/en-us/articles/10587333978011-Sublimation-Heat-Press-Settings):
  tabelas como ponto de partida; consultar o fabricante do artigo, calibrar e testar.
- [Roland DG — Sublimation Printing](https://www.rolanddg.com/applications/sublimated-graphics):
  transferência, equipamento e aplicações de imagens a cores.

Não foram generalizadas promessas comerciais de permanência ou resistência dos
fabricantes. Não existe uma receita de 180–200 °C aplicável a qualquer artigo.
As perguntas sobre área, amostra, cuidados e aprovação são orientação editorial,
não um procedimento industrial confirmado da Nobrinde. Não foi declarada
compatibilidade de qualquer caneca, base de rato ou placa sem ficha por referência.

## Imagens

As quatro imagens encontradas em `assets/tecnicas/Sublimacao/` foram incluídas
após autorização expressa do utilizador em 28/09/2026. A autoria e a fonte original
continuam não documentadas; o crédito não declara uma licença aberta. Registo individual em
`editorial/imagens-por-confirmar.md`; hashes antes/depois em
`tmp/sublimacao-imagens-antes.json`. Nenhum original foi alterado.

As fotografias documentadas de tampografia, serigrafia e UV tinham sido movidas
para as subpastas respetivas antes desta tarefa. Comparação com o Git confirmou
bytes idênticos. Atualizaram-se os caminhos no gerador de fotografias e créditos,
preservando autores/licenças e a organização escolhida pelo utilizador. Corrigiu-se
também a capitalização de `Tampografia` nos caminhos das imagens já existentes.
Esta correção não constitui uma nova autorização das imagens provisórias anteriores.

## Ficheiros desta alteração

Fontes e geração:
- `conteudos/sublimacao.py` (novo).
- `conteudos/catalogo.py` (registo e relações inversas).
- `conteudos/recursos.py` e `conteudos/apresentacao_recursos.py` (caminhos movidos).
- `gerar.py` (data de revisão, caminhos e integração das imagens autorizadas).
- `styles.css` (limite de largura das imagens de Sublimação).
- `assets/pesquisa-dados.js` (pesquisa).
- `testes/pesquisa.test.cjs` (regressão: técnica e equipamentos, com/sem acentos).

Páginas geradas:
- `tecnicas/tecnica-sublimacao.html` (novo), `tecnicas/index.html`.
- `tecnicas/serigrafia.html`, `tecnicas/impressao-uv.html`, `tecnicas/tampografia.html`.
- `guias/como-escolher-a-tecnica.html`.
- `materiais/materiais-texteis.html`, `materiais/vidro-e-ceramica.html`.
- `produtos/garrafas-copos-e-canecas.html`, `produtos/texteis.html`.
- `industria/sublimacao.html`, `industria/index.html`, `industria/da-ideia-a-entrega.html`,
  `industria/equipamentos-de-serigrafia.html`, `industria/impressoras-uv.html`,
  `industria/maquinas-de-tampografia.html`.
- `creditos-imagens.html`.

Documentação:
- `editorial/plano.md`, `editorial/imagens-por-confirmar.md`, este registo e `README.md`.

As alterações de Tendências e os movimentos de imagens anteriores foram preservados.
A página inicial foi preservada: o gerador tem um desfasamento anterior entre o
modelo e o HTML, documentado no registo da integração de Tendências.

## Verificações

- Geração e Prettier concluídos.
- Verificação geral: 66 páginas, 2372 ligações/recursos locais; H1, idioma e âncoras válidos.
- Testes de pesquisa: cinco passaram. Verificação de Materiais passou.
- Imagens de Sublimação: SHA-256 inalterado; quatro imagens integradas com legendas,
  texto alternativo e ligação ao registo de autorização nos créditos.
- Verificação adicional da capitalização dos caminhos locais, incluindo os recursos movidos.

- Chromium/Playwright: quatro páginas (técnica, listagem, guia de escolha e guia de
  indústria) a 360, 390, 768 e 1440 px, sem deslocamento horizontal. Cabeçalho,
  rodapé, menu e âncoras funcionais; ambos os guias encontrados na pesquisa;
  sem erros JavaScript. Capturas estáveis com movimento reduzido.
- Inspeção visual das capturas do topo e da secção de parâmetros a 390 px e do
  guia a 1440 px; relatório em `tmp/sublimacao-browser.json`, capturas
  `tmp/sublimacao-*.png` (ficheiros locais ignorados pelo Git).
- Prettier e `git diff --check` passaram.

## Pendências

- Documentar a origem/autoria e os eventuais direitos de terceiros das quatro imagens;
  a autorização de utilização dada pelo utilizador já está registada.
- Aprovação técnica/editorial pela Nobrinde; confirmar equipamentos e capacidades reais.
- Confirmar, por referência, composição/revestimento, parâmetros do fabricante,
  área imprimível, cuidados e amostra aprovada; não há validação de produção neste guia.
- Testar num telemóvel físico e em Safari/iOS; a simulação Chromium não os substitui.

Não houve publicação nem push para o GitHub.

Atualização das imagens: carregamento das quatro imagens verificado no navegador,
com largura máxima de 474 px, proporções originais e layout responsivo.
