# Transfers — integração de 30 de setembro de 2026

## Atualização após revisão do utilizador

O utilizador autorizou expressamente o uso das imagens locais. Foram integradas
cinco fotografias, com originais preservados, dimensões reais, alt factual e
créditos em `creditos-imagens.html#transfers-fornecidas`: duas de Serigráfico,
uma de Digital e duas de DTF. A autoria e a origem continuam por documentar.
Esta autorização substitui a decisão inicial de excluir todas as fotografias,
registada abaixo. As imagens DTF (29) e (30) são esquemas inconsistentes;
as fotografias Digital (24)/(25) são duplicadas e mostram rolos sem identificar
o processo; Digital (26) mostra acabamentos de tecnologia não identificada.
A montagem Serigráfico (21) não acrescenta informação ao exemplo selecionado.
Não existe pasta própria de Digital com Base; mantém-se o esquema original.

A entrada Técnicas mostra apenas Transfers, tanto nos cartões como nas etiquetas.
Os quatro cartões e respetivos destinos mantêm-se dentro de Transfers, assim
como a pesquisa dos guias e as comparações entre modalidades.
Alterado também `conteudos/apresentacao_recursos.py` para registar os créditos.
Verificações após integração: 72 páginas, 2717 ligações/recursos válidos,
195 utilizações de imagens/37 ficheiros e seis testes de pesquisa aprovados.

## Âmbito e decisões

Cinco páginas locais, geradas por `gerar.py` a partir de `conteudos/transfers.py`:

- `tecnicas/transfers.html`: entrada e quatro cartões distintos.
- `tecnicas/transfer-serigrafico.html`.
- `tecnicas/transfer-digital.html`.
- `tecnicas/transfer-digital-com-base.html`.
- `tecnicas/dtf.html`.

Reutilizados cabeçalho, navegação, índice de leitura, esquemas HTML/CSS, cartões,
fontes e rodapé das técnicas. Bordado e Termogravura foram analisados antes da
implementação. A etiqueta do grupo têxtil é resolvida pelo título do artigo;
os títulos dos transfers passaram a coincidir com os destinos gerados.
O guia industrial DTF existente foi conservado e ligado à nova técnica.

## Fontes consultadas e acessíveis

Consulta direta em 30/09/2026. As páginas abaixo devolveram conteúdo legível.
As alegações comerciais de preço, velocidade e resistência não foram importadas.
Os parâmetros numéricos não foram convertidos em regras genéricas.

| Fonte direta | Afirmações sustentadas e âmbito |
| --- | --- |
| [Mimaki — TxF150-75](https://mimaki.com/product/inkjet/dtf/txf150-75/) | Secções «What is DTF?», tintas e aplicações: impressão no filme, pó termofusível, preparação térmica e prensa; CMYK e branco no sistema citado. |
| [Transfer Express — Goof Proof](https://www.transferexpress.com/heat-press-transfers/goof-proof-screen-printed-transfers) | Tinta plastisol serigráfica neste produto; materiais e aplicação próprios da referência. Não generaliza formulação ou lavagem. |
| [Transfer Express — Application Instructions](https://www.transferexpress.com/application-instructions) | Demonstra diferenças de parâmetros e destaque entre produtos e variantes. Referência para pedir a ficha correta, não para operar outro sistema. |
| [Avient — Technical Tips](https://www.avient.com/technical-tips-transfer-printing) | Papel de libertação e influência da estabilidade/humidade no registo de transfers serigráficos. |
| [Avient — Union Ink Transfer Inks](https://www.avientspecialtyinks.com/products-brand/union-ink/union-ink-transfer-inks) | Adesivo em pó e adesivo imprimível como opções documentadas. Não afirma que todos os transfers tenham construção idêntica. |
| [Avient — Transfer Troubleshooting](https://www.avient.com/transfer-troubleshooting) | Diagnóstico de libertação e aderência; várias causas possíveis a analisar com o produtor. Não se reproduzem receitas corretivas. |
| [Siser — Digital Printing](https://www.siser.com/digital-printing/) | Exemplo identificado de material para impressão digital e corte, incluindo Colorprint PU. Não define o serviço Nobrinde. |
| [Siser — filmes brancos e transparentes](https://www.siser.com/news/printable-white-films-printable-transparent-films/) | Diferenças de preparação, espelhamento e aplicação; indicação de claros/escuros restrita aos materiais descritos. |
| [FOREVER — Laser-Dark (No-Cut)](https://www.forever-ots.com/product/laser-dark-no-cut-cmyw/) | Exemplo A-Foil/B-Paper e revestimento branco de opacidade. Não prova que «Digital com Base» seja esse produto, nem tinta branca sob CMYK. |

As comparações, listas de verificação e propostas de avaliação de amostras são
orientação editorial. Não são especificações do parque de máquinas, serviços ou
capacidades da Nobrinde. Cada guia inclui fontes no formato das outras técnicas.
Nenhum proxy Gmail/Bing foi usado como fonte ou para obter imagens.

## Confirmações necessárias pela Nobrinde

1. Fabricante e referência do processo designado «Transfer Digital».
2. Significado de «Transfer Digital com Base»: confirmar se a base é branca,
   como é criada, composição documentada e função; em particular, não está
   demonstrado que seja uma camada branca impressa sob CMYK.
3. Compatibilidade artigo/tecido/revestimento/transfer, instruções de aplicação
   e lavagem, critérios de amostra e ensaios. Não se publicaram mínimos,
   preços, prazos, temperaturas, tempos ou garantias universais.
4. Origem e direitos das 11 imagens locais. Não incluídas nos novos guias.
   Não existe a pasta específica de Digital com Base indicada no pedido.

## Ficheiros de implementação

`conteudos/transfers.py`, `conteudos/catalogo.py`, `gerar.py`, `styles.css`,
`testes/pesquisa.test.cjs`, `assets/pesquisa-dados.js`, este registo,
`editorial/imagens-por-confirmar.md`, `editorial/plano.md` e `README.md`.

Além das cinco páginas novas, as ligações atualizam `tecnicas/index.html`,
`tecnicas/bordado.html`, `tecnicas/serigrafia.html`,
`tecnicas/tecnica-sublimacao.html`, `industria/dtf-e-prensas-termicas.html`,
`materiais/materiais-texteis.html`, `produtos/texteis.html`,
`produtos/sacos-e-mochilas.html` e `guias/como-escolher-a-tecnica.html`.
A regeneração de `index.html` também repõe uma frase já presente no modelo
`modelos/inicio.html`; o modelo não foi alterado nesta tarefa.

## Verificações

- Geração com Prettier local concluída.
- `python verificar.py`: 72 páginas, 2715 ligações/recursos locais válidos.
- Verificação de imagens: 190 utilizações, 32 ficheiros; dimensões e textos
  alternativos válidos. As imagens não autorizadas de Transfers não são carregadas.
- Verificação existente de Materiais aprovada.
- `node --test testes/pesquisa.test.cjs`: seis testes aprovados, incluindo as
  designações dos transfers e os dois destinos DTF (técnica e equipamentos).
- `npm run format:check`: todos os HTML conformes.
- Chrome headless/Playwright: cinco páginas a 360, 390, 768 e 1440 px (20
  combinações), sem deslocamento horizontal. Carregamento e alt das imagens
  existentes válidos; nenhuma fotografia de Transfers carregada.
- Quatro cartões da entrada clicados; destinos e regresso confirmados. As
  três comparações de cada modalidade e as cinco etiquetas do grupo têxtil
  têm destinos válidos. Menu móvel abre e fecha por Escape nas cinco páginas.
- Sem erros JavaScript. Capturas das cinco páginas a 390 e 1440 px em
  `tmp/transfers-qa/`; inspeção visual conjunta em `mobile-review.png`.
  Texto, títulos, cartões e espaçamento legíveis na amostra móvel inspecionada.
- Ferramenta de QA instalada apenas em `tmp/transfers-qa/`, sem alterar
  dependências ou configuração de execução do site.

Sem push nem publicação externa.
