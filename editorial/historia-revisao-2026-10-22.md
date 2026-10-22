# Revisão da História dos brindes — 22 de outubro de 2026

## Resultado e ficheiros

Mantido `industria/historia-dos-brindes.html`, com o título “História dos brindes
e da comunicação promocional”. As âncoras `parte-0` a `parte-7` e `fontes`
continuam disponíveis. Não foi criada outra página ou secção principal.

- `conteudos/historia_brindes.py`: narrativa, seis etapas da cronologia, quatro
  objetos, imagem do cartão, fontes com âmbito e créditos.
- `conteudos/industria.py`: integra o artigo e as suas fontes na estrutura existente.
- `scripts/render_historia.py`: cronologia com duas linhas de leitura e galeria.
- `scripts/gerar.py`: integra o corpo do artigo, créditos e cartão com imagem integral.
- `assets/css/styles.css`: apresentação da cronologia e galeria, com adaptação
  a ecrãs estreitos e imagens contidas, sem recorte nem títulos sobrepostos.
- `industria/historia-dos-brindes.html`, `industria/index.html`,
  `creditos-imagens.html` e `assets/pesquisa-dados.js`: saídas geradas.
- `testes/verificar_industria.py` e `testes/pesquisa.test.cjs`: datas por artigo,
  associação entre objeto e imagem, ordem, fontes, âncoras e descoberta pela pesquisa.
- `editorial/fontes-historia-2026-10-22.md` e `editorial/historia-imagens.json`:
  bibliografia e registo das fotografias, dimensões, hashes e lacunas documentais.

## Decisões históricas

Washington surge primeiro, como apoio e comemoração, sem confundir os botões
com brindes empresariais ou presumir distribuição gratuita. O ano de 1789 é
o do contexto documentado pelo Smithsonian, não uma autenticação da imagem local.

O saco de Coshocton, escolhido para o cartão, é apresentado como um dos primeiros
exemplos documentados no percurso norte-americano descrito. O contributo do curador
Bill Carlisle confirma o contexto local de impressão de sacos de juta com publicidade
de uma loja de calçado. Não é afirmada prioridade mundial. Foram encontrados relatos
com anos diferentes; por isso usa-se o final do século XIX, sem atribuir um ano
preciso ao exemplar. A composição em lona não foi confirmada.

A utilização publicitária de espelhos é sustentada por fonte especializada e pelo
testemunho do arquivista Phil Mooney sobre a própria organização. Não foi possível
documentar uma alegação de pioneirismo para o exemplar da fotografia, por isso não
se usa “primeiro” nem “época vitoriana”. A peça pode não ser contemporânea da imagem
publicitária que reproduz; a fotografia não permite resolver essa questão.

As réguas são identificadas como réguas de madeira, sem referência a calendários
na legenda. A peça de cerca de 1920 conservada no Powerhouse é explicitamente um
exemplo comparativo; essa data não foi transferida para as peças fotografadas.

Na rádio, distingue-se 1935 (emissões regulares da rádio pública portuguesa),
1939 (gravação publicitária identificada pelo Museu RTP) e 1995 (documentário que
recupera gravações anteriores). Na televisão distinguem-se as experiências de
1956 e as emissões regulares de 7 de março de 1957. Não se afirma uma data de
primeiro anúncio televisivo ou radiofónico universal.

Para o digital usam-se os marcos do CERN de 1989 e 1993, separando Web de Internet
e da publicidade online. A presença online da RTP em 1997 é um caso português
institucional. Não se apresenta um anúncio norte-americano como origem global.

## Fotografias e condições de utilização

Usadas as quatro imagens indicadas, na pasta equivalente já existente
`assets/Industria/Historiadosbrindes`, percorrida e inspecionada. A imagem antiga
do livro permanece no disco, mas deixou de ilustrar o cartão e o artigo.

Os quatro ficheiros são apresentados sem edição ou conversão. Autoria fotográfica,
licença, fonte original, autenticidade, data e instituição detentora dos exemplares
locais continuam por confirmar. As instituições citadas documentam peças ou
contextos comparáveis; não lhes é atribuída a propriedade destas fotografias.
Os créditos públicos registam os limites. A integração é local, a pedido do
utilizador; não foi documentada autorização de publicação das fotografias.

Não foram acrescentadas imagens para imprensa, rádio, televisão ou digital:
as quatro fornecidas representam objetos e não esses meios de comunicação.

## Verificações

Geração: `.venv/Scripts/python.exe scripts/gerar.py --secao industria`.

Aprovados os testes da Indústria, estrutura, imagens, materiais, mercado, ocasiões,
produtos, imagens de produtos e públicos. Aprovados os 14 testes de pesquisa.
Verificadas 133 ligações/recursos locais nas três páginas HTML alteradas, incluindo
âncoras. Dimensões e integridade das quatro imagens verificadas com Pillow.
Prettier aprovado nas três páginas alteradas; `git diff --check` aprovado.

A verificação global não passa por um problema anterior e externo a esta revisão:
`guias/produto-standard-ou-a-medida.html` tem referências a `#fontes` e a fontes
individuais sem os respetivos destinos. Essa ausência também existe na versão
committed (`HEAD`), e a página não foi alterada nesta tarefa. O verificador de
Guias falha pela mesma ausência e o Prettier global assinala esse ficheiro.

Não foi possível fazer uma inspeção visual num navegador: o inventário de
navegadores disponível nesta sessão está vazio. A adaptação responsiva foi
implementada em CSS, mas não se declara validada por capturas de ecrã.

Não foi feito commit, push ou publicação.
