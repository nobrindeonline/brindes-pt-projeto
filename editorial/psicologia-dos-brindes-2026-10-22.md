# Psicologia dos Brindes — 22 de outubro de 2026

## Integração e ficheiros

Página: `guias/psicologia-dos-brindes.html`, no percurso Escolher de
`guias/index.html`. Breadcrumbs, resposta breve, esquema, índice de leitura,
checklist, perguntas e fontes reutilizam os componentes existentes.

- `conteudos/guia_psicologia.py`: fonte do artigo, seis fatores com subtítulos,
  exemplos por objetivo, checklist, avaliação, conclusão e fontes com âmbito.
- `conteudos/guias.py`: integração do nono guia e da bibliografia.
- `scripts/render_guias.py`: suporte opcional a subtítulos e ordem editorial das
  secções, preservando o comportamento anterior quando esses campos não existem.
  Os subtítulos também integram o JSON e a pesquisa.
- `conteudos/guias_imagens.py` e `editorial/preparar_imagens_guias.py`: seleção
  de três imagens, textos alternativos, legendas e registo de utilização.
- `guias/index.html`, `guias/psicologia-dos-brindes.html`, `pesquisa.html`,
  `creditos-imagens.html`, `assets/pesquisa-dados.js`,
  `assets/guias-conteudos.json`, `assets/guias/visuais/imagens.json`,
  `editorial/guias-imagens.json` e `editorial/fontes-guias.md`: saídas integradas.
- `testes/verificar_guias.py` e `testes/pesquisa.test.cjs`: contagem de nove guias,
  verificação seletiva e descoberta do novo conteúdo.

Ligações finais para Produtos, Para quem e Ocasiões e Sazonalidade, além dos
guias relacionados existentes. Não foi necessário alterar esses artigos.

## Evidência e limites

A bibliografia pública e `editorial/fontes-guias.md` registam as fontes, os URLs,
a consulta e o âmbito. Foram selecionadas três investigações:

- Baskin, Wakslak, Trope e Novemsky (2014), DOI `10.1086/675737`: facilidade prática
  e diferenças de perspetiva entre quem oferece e recebe. Foi consultada a versão
  disponibilizada no domínio académico da University of Southern California.
  Não é usada para quantificar uso ou eficácia de brindes.
- Rixom, Mas e Rixom, DOI `10.1002/jcpy.1140`, publicação online em 2019:
  apresentação, expectativas e relação entre participantes. Versão dos autores
  disponível via SSRN e página institucional da University of Nevada, Reno.
  Não é transformada numa regra sobre embalagens mais elaboradas.
- Dorsch e Kelley (1994), DOI `10.1177/0092070394224001`: consultado o resumo
  oficial da editora sobre ofertas a responsáveis de compras. Não foi consultado
  o texto integral por subscrição. A utilização limita-se ao âmbito do resumo:
  obrigação, perceção de manipulação, tipo de oferta e intenções de reciprocidade.

Os exemplos e as recomendações são editoriais. O texto distingue contacto com
a marca, aceitação, utilização, satisfação e causalidade. Não apresenta
estatísticas, previsões individuais, promessas de fidelização ou de vendas.

## Imagens

Foi usada a pasta equivalente existente `assets/guias/PsicologiadosBrindes/`,
sem criar uma segunda pasta de originais com o nome indicado no brief.

- Cartão: `brindes-para-ativacoes-de-marca.webp`, 1448 × 1086; alias público
  `assets/guias/visuais/psicologia-cartao.webp`. Mostra quatro pessoas junto a
  uma mesa com objetos num evento.
- Artigo, na secção Exemplos: `Novidades-e-tendencias-em-brindes-customizados-para-feiras-e-eventos.png`,
  1654 × 832; alias `assets/guias/visuais/psicologia-entrega.png`. Mostra a entrega
  de um saco. A legenda não toma o símbolo de folhas como prova ambiental.
- Artigo, na secção Surpresa, reconhecimento e reciprocidade:
  `porque-amamos-um-brinde.jpg`, 900 × 400; alias público
  `assets/guias/visuais/psicologia-surpresa.jpg`. Incluída por indicação do
  utilizador, como ilustração de surpresa, sem constituir evidência de uma reação real.

As cópias são binárias, sem recorte, conversão ou distorção. Autoria e licença
de terceiros não identificadas; o sistema de créditos existente mantém essa
limitação. As imagens são ilustrativas e não documentam resultados de estudos.

## Geração preservando as páginas existentes

Foi acrescentada uma opção ao gerador para integrar apenas um novo guia:

```powershell
.venv/Scripts/python.exe scripts/gerar.py --secao guias --artigo psicologia-dos-brindes
.venv/Scripts/python.exe editorial/gerar_fontes_guias.py
```

Esta opção gera o artigo, a entrada e os dados partilhados sem reescrever os
outros oito artigos de Guias. Foi confirmada por hashes a preservação byte a
byte dos oito guias anteriores e da página de História durante esta tarefa.

## Verificações

Aprovados:

- `testes/verificar_guias.py --guia psicologia-dos-brindes`: índice com nove
  guias, JSON, fontes, datas, imagens e pesquisa consistentes.
- `node --test testes/pesquisa.test.cjs`: 15 testes aprovados.
- `testes/verificar_estrutura.py`: estrutura do projeto aprovada.
- 102 ligações e recursos locais verificados no novo artigo, índice e créditos.
- Dimensões, proporções declaradas e integridade das imagens com Pillow.
- Um H1, seis fatores e quatro exemplos em H3, referências resolvidas e ordem
  editorial correta das secções, incluindo checklist antes da avaliação.
- Prettier nas quatro páginas geradas por esta tarefa.

A execução de `scripts/verificar_tudo.py` continua a falhar nas âncoras de fontes
ausentes do guia standard, um problema anterior. A verificação adicional da
Indústria também assinala créditos de imagens ausentes na página de História,
que foi preservada como estava. `git diff --check` global encontra espaços finais
nessa página. Estas ocorrências não foram corrigidas para não modificar páginas
fora do pedido.

O novo guia herda as regras responsivas de cartões, leitura, imagens e índice
dos Guias. Não foi possível confirmar a apresentação renderizada em ecrã pequeno
e grande: o inventário de navegadores desta sessão está vazio. Não se declara
uma revisão por capturas de ecrã.

Não foi feito commit, push ou publicação.
