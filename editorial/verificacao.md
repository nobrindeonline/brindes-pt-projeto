# Verificação da versão local

## Atualização: Para quem

- Página de entrada com seis cartões e seis guias, totalizando 23 escolhas.
- 33 páginas; 1127 ligações e recursos locais válidos.
- 83 utilizações de imagens, em 17 ficheiros decodificáveis, com alt e dimensões corretas.
- Verificadas as seis ligações de entrada, as âncoras antigas, os regressos,
  as ligações às categorias e técnicas e as páginas PDF nas citações.
- Cada seleção tem três ou quatro produtos e justificações de três frases.
- Os quatro testes da pesquisa passaram; nenhum preço publicado em HTML.
- Cartões em três/duas/uma colunas; produtos em duas/uma colunas, com mudança
  para uma coluna até 620 px e fotografias sem corte.
- A ferramenta de navegador continua sem aplicações ou navegadores ligados.
  Foi feita revisão do código responsivo, mas não inspeção visual da página renderizada.

## Atualização: imagens e secção editorial

- 27 páginas geradas, incluindo três artigos de ideias e a página de créditos.
- `python verificar.py`: 937 ligações e recursos locais válidos.
- `.venv/Scripts/python.exe testes/verificar_imagens.py`: 54 utilizações de imagens
  em 17 ficheiros, todos decodificáveis, com texto alternativo e dimensões corretas.
- As três ligações «Ler mais» apontam para os artigos certos; todos têm ligação
  de regresso. Os artigos editoriais não contêm marcação de data nem «Guia permanente».
- Os quatro testes existentes da pesquisa continuam a passar.
- Não existem preços em HTML nem referências a `assets/assets/`.
- Fotografias e fichas selecionadas do PDF inspecionadas visualmente; imagens
  extraídas sem preços ou páginas inteiras. Fontes em `fontes-catalogo.md`.
- Grelha editorial: três colunas em desktop, duas até 1000 px e uma até 620 px.
  Imagens inteiras, com dimensões reservadas e carregamento diferido.
- Limitação: não há navegador ligado à ferramenta nesta sessão; a inspeção
  visual da página renderizada em desktop e telemóvel permanece pendente.

Os resultados abaixo documentam a versão anterior, antes desta atualização.

Data: 24 de setembro de 2026.

## Verificações concluídas

- Geração das 17 páginas: inicial, pesquisa, oito índices e sete artigos.
- `python verificar.py`: 550 destinos de ligações e recursos locais verificados,
  incluindo âncoras. Nenhum destino em falta; nenhum ID repetido; um H1 por página;
  idioma `pt-PT` em todas as páginas.
- `node --test testes/pesquisa.test.cjs`: quatro testes aprovados. Cobrem acentos,
  maiúsculas, combinação de termos, prioridade do título, pesquisa vazia,
  ausência de resultados, entrada com marcação HTML e temas editoriais pendentes.
- `node --check script.js` e `node --check pesquisa.js`: sintaxe válida.
- As 17 páginas responderam com HTTP 200 no servidor local e texto UTF-8.
- Conteúdos e modelos revistos à procura de caracteres corrompidos pela codificação.
- Revisão do código responsivo: grelhas adaptáveis, menu para larguras até 1100 px,
  índice do artigo sem posição fixa em ecrãs pequenos, campos e botões adaptáveis.

## Limitação da verificação

A ferramenta de controlo do navegador devolveu «No browser is available» e
o inventário confirmou zero navegadores e zero aplicações ligados. Não foi
possível fazer inspeção visual, capturar ecrãs, clicar na navegação ou testar
o comportamento real do menu e da pesquisa num navegador nesta sessão.

Os testes automatizados não substituem essa revisão visual. Está pendente
validar em 360, 390, 768 e 1440 px, incluindo fontes carregadas, foco, menu,
resultados da pesquisa, histórico do navegador e abertura direta por `file://`.

## Revisão de conteúdo pendente

Consultar `validacoes.md` e `plano.md`. Não foram publicados perfis de fornecedores,
artigos históricos ou notícias sem fontes suficientes. Não houve publicação do site.
# Verificação da secção indústria — 24/09/2026

- Geradas 46 páginas no total: entrada da indústria revista e 13 novos guias.
- `python verificar.py`: 1518 ligações e recursos locais válidos; títulos, idioma e âncoras válidos.
- `.venv/Scripts/python.exe testes/verificar_imagens.py`: 95 utilizações, 17 ficheiros de imagem; dimensões, textos alternativos, créditos e ausência de preços verificados.
- `node --test testes/pesquisa.test.cjs`: 4 testes aprovados. DTF passa a conduzir ao guia publicado.
- Mantidas as âncoras `fluxo`, `maquinas`, `montagem` e `historia`. Ligações entre os cinco guias de técnicas e os novos guias de máquinas em ambos os sentidos.
- Cronologia com lista ordenada de 11 etapas; cartões e esquemas com regras responsivas, colunas flexíveis e uma coluna em ecrãs pequenos. Reutilizados cabeçalho, rodapé e menu móvel.
- **Limitação:** não foi possível inspecionar o resultado renderizado em computador ou telemóvel: a ferramenta de navegador devolveu zero navegadores disponíveis. A revisão foi estrutural e de CSS; a inspeção visual continua pendente.
- Fontes técnicas/históricas e confirmações operacionais em `fontes-industria.md`; imagens e características do catálogo em `fontes-catalogo.md`.
# Materiais — 28 de setembro de 2026

- Entrada com sete cartões ligados a sete guias completos; fotografias existentes
  em quatro famílias. Âncoras antigas preservadas e sete artigos na pesquisa.
- `python gerar.py`: geração e Prettier concluídos.
- `python verificar.py`: 61 páginas e 2170 ligações/recursos locais válidos.
- `node --test testes/pesquisa.test.cjs`: quatro testes aprovados.
- `.venv/Scripts/python.exe testes/verificar_imagens.py`: 172 utilizações,
  25 ficheiros válidos, dimensões e textos alternativos verificados.
- `python testes/verificar_materiais.py`: sete cartões e destinos, fontes,
  produtos/técnicas relacionados e ausência de referências ao catálogo no texto
  público e nos alt de Materiais.
- `npm.cmd run format:check`: todos os HTML conformes.
- Imagens inspecionadas na folha de contacto existente; composição conferida
  no registo de recursos. Nenhuma fotografia externa acrescentada.
- CSS revisto: grelha com três, duas e uma coluna pelos pontos de quebra existentes;
  leitura passa a uma coluna até 750 px, imagens contidas e índice sem posição
  fixa em telemóvel. Esta revisão estrutural não comprova a renderização.
- **Limitação visual:** `cua.getBrowser` devolveu “No browser is available” e
  `cua.getState()` devolveu `apps: []` e `browsers: []`. Não foi possível fazer
  inspeção renderizada em computador/telemóvel. Rever 360, 390, 768 e 1440 px
  quando houver navegador: cartões, índice, menu, foco e deslocamento horizontal.
- Entrada servida localmente com HTTP 200. Sem publicação na Internet.
- Fontes reproduzíveis em `gerar_fontes_materiais.py`; confirmações da Nobrinde
  registadas em `fontes-materiais.md` e `validacoes.md`.

# Correção de acesso às quatro áreas de Indústria

- História preservada em `industria/historia-dos-brindes.html`, sem reposição de versões antigas.
- Entrada com quatro cartões, começando pela História; percurso e máquinas em páginas próprias.
- Mantidas as âncoras anteriores, os guias, fontes, fotografias e créditos.
- Verificações: 48 páginas, 1560 ligações/recursos locais, 97 utilizações de imagens e quatro testes de pesquisa aprovados.
- Navegação verificada estruturalmente: menu → Indústria → cada uma das quatro áreas, com ligações de regresso. Não equivale a uma inspeção visual em navegador.
# Tampografia — conteúdo e imagens provisórias

- Página revista com definição, cinco passos, componentes, equipamento, aplicações,
  cores, preparação da arte, condições, limitações e história documentada.
- Três JPG com largura original de 474 px; apresentação com largura automática,
  máximo de 100% do espaço disponível e altura proporcional. O quarto JPG permanece
  guardado sem exibição. Legendas, texto alternativo e estado dos créditos incluídos.
- Preservadas as âncoras anteriores, as ligações de navegação, os guias relacionados
  e a ligação aos créditos da fotografia anterior.
- Verificações de HTML, caminhos, imagens e pesquisa aprovadas.
- Limite da verificação: a ferramenta de navegação não disponibiliza qualquer
  navegador. Foram inspecionadas as imagens de origem e as regras CSS para computador
  e telemóvel; não foi possível verificar a renderização real nesses tamanhos.
