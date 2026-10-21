# Guias — revisão de 12 de outubro de 2026

## Âmbito e preservação

O Git foi consultado antes de editar. Preservaram-se as alterações locais das
reformulações anteriores, as novas pastas de imagens e as remoções locais de
ficheiros. Não se fez commit, push ou publicação.

Foram analisados `conteudos/guias.py`, o índice Python `conteudos/catalogo.py`,
as funções de `scripts/gerar.py`, os oito HTML de Guias e as onze imagens locais. Não
foi aberto o documento comercial local. Os exemplos dependentes dele foram
retirados da fonte e das funções específicas de Guias, incluindo nomes, medidas,
referências, campos de exemplos, fotografias e ligações de origem.

As explicações válidas sobre ficheiros, área útil, cor, revisão da maquete,
utilização e prevenção foram conservadas. Substituíram-se as passagens que usavam
referências comerciais por critérios gerais. O guia de técnica passou a integrar
a mesma fonte dos restantes seis; a integração antiga que lhe acrescentava um
exemplo comercial foi eliminada.

## Organização e estrutura

Os três percursos mantêm as âncoras `escolher`, `cor` e `qualidade`, com títulos
“Escolher”, “Preparar ficheiros e cor” e “Rever antes de produzir”. O percurso de
escolha segue evento/uso, material e técnica. Mantêm-se as sete rotas anteriores.

Cada guia inclui resposta breve, critérios ou passos, prevenção, checklist,
perguntas frequentes, fontes com âmbito e datas, e relações internas pertinentes.
As ligações para técnicas e materiais válidas continuam disponíveis em contexto;
as ligações entre Guias são únicas e não repetem resumos inteiros.

Os problemas são organizados por sinal observado, pontos a verificar e evidência
a reunir, incluindo um caso de bordado. Não se atribui uma causa definitiva pela
fotografia. As secções anteriores continuam com âncoras compatíveis; a antiga
âncora `parte-6` do guia de técnica aponta agora para a verificação final, sem
conservar o exemplo retirado.

Em telemóvel, o índice de leitura é expansível para permitir chegar à resposta
breve sem percorrer uma longa lista de ligações. Usa elementos nativos e funciona
por teclado. Em computador, o índice começa aberto.

## Fontes, revisão e limites

As oito fontes públicas foram efetivamente consultadas nesta revisão. Incluem
documentação Adobe sobre raster/vetor, PDF, cores diretas/CMYK e prova de ecrã;
Roland DG sobre teste no objeto concreto; Madeira sobre bordado e fatores de
franzido; ScreenPrinting.com sobre serigrafia têxtil; Inkcups sobre tampografia;
e HSE sobre chegada, circulação e saída em eventos.

Para HSE, cita-se a página específica “Put crowd controls in place”, que contém
as três fases usadas. Não se atribuem à fonte recomendações de seleção de brindes
nem se apresenta este guia como plano de segurança de eventos. A página inicial
da coleção foi consultada para encontrar a documentação específica.

Revisão efetiva dos sete conteúdos: 2026-10-12. As datas de consulta e de revisão
são campos distintos, apresentados e exportados a partir da fonte. A formatação
do texto da data deriva do ISO de cada artigo; não há uma data textual fixa no
novo renderizador. Não se confundem datas de atualização dos documentos externos
com a revisão destes Guias. A bibliografia está em `fontes-guias.md`, gerada por
`gerar_fontes_guias.py`.

Não foram incluídas compatibilidades automáticas, resultados de resistência,
prazos, limiares universais de quantidade, DPI ou detalhe mínimo, equivalências
exatas de cor ou vantagens ambientais não documentadas. As condições específicas
continuam a exigir a identificação de artigo, material, arte e processo.

## Imagens e esquemas

As onze imagens foram abertas e analisadas. Foram escolhidas sete, com nomes
públicos neutros e cópias binárias iguais aos originais:

| Destino | Imagem escolhida | Utilização |
|---|---|---|
| Técnica | Três t-shirts em cabides | Cartão; ilustra variedade visual, sem confirmar processos |
| Evento | Entrega junto a uma mesa | Cartão; ilustra o momento de distribuição |
| Material | Conjunto de objetos sobre fundo cinzento | Cartão; sem inferir composição |
| Maquete | Composição com marcas genéricas | Cartão e uma segunda composição no artigo |
| Cor | Leques de amostras | Cartão e uma segunda imagem de suporte junto a amostras no artigo |

As duas capturas de interfaces de desenho não foram usadas: eram densas,
parcialmente em inglês e não explicavam bem dimensão final e versão da arte.
As duas imagens da pasta de problemas representavam distribuição ou escolhas
genéricas de eventos, sem mostrar sinais técnicos que sustentassem os casos.
Não foram forçadas no diagnóstico. Usaram-se capas esquemáticas originais nos
cartões de logótipo e problemas.

Os artigos usam diagramas originais de decisão, raster/vetor, CMYK e camadas
possíveis de um artigo. São explicações de conceitos, não provas físicas ou
imagens que estabeleçam uma especificação. Os textos continuam compreensíveis
sem as imagens. Não se descarregaram imagens externas e não se editaram os
originais de assets.

`conteudos/guias_imagens.py` define a seleção. `preparar_imagens_guias.py` gera
aliases em `assets/guias/visuais/`, o manifesto público e o registo privado
`guias-imagens.json`. Nomes de origem, utilização local e hashes ficam no registo
privado; os dados públicos contêm apenas URL neutro, alt, dimensões de imagem e
papel ilustrativo. Não existem campos de autoria/copyright EXIF ou XMP nas imagens
selecionadas; não se inferiu autoria nem licença de terceiros. Não se declara
uma licença aberta para as imagens locais. A seleção foi solicitada pelo utilizador;
isso não foi apresentado como prova de autorização de terceiros.

Créditos públicos neutros em `creditos-imagens.html#guias-ilustrativos`. Nenhuma
imagem selecionada nem os seus metadados identificam a entidade mantenedora.

## Fonte única, pesquisa e consulta futura

`scripts/render_guias.py` apresenta os dados de `conteudos/guias.py`. O índice de artigos
usa cópias desses dados para que as relações antigas de outras secções não
modifiquem acidentalmente a fonte revista dos Guias.

`assets/guias-conteudos.json` é gerado automaticamente: percursos, ID, slug,
título, categoria, resumo, resposta direta, ordem de leitura, passos, casos,
prevenção, checklist, FAQ, esquema, relações, contexto, fontes, datas e imagens.
As citações estão em campos estruturados junto ao texto que sustentam. Imagens
têm papel ilustrativo e `fonte_tecnica: false`. A exportação não contém registos
internos, referências comerciais ou nomes de ficheiros de origem. Não foram
criados chatbot, modelo ou base de dados.

A pesquisa indexa os campos públicos da mesma fonte, incluindo perguntas,
critérios e evidência. As entradas das outras secções foram comparadas por URL
e mantiveram-se iguais. Na página de pesquisa, mudou apenas o texto da ligação
para “Guias práticos”, para corresponder ao índice revisto.

## Ficheiros e verificação

Principais alterações: `conteudos/guias.py`, integração em `conteudos/catalogo.py`,
`scripts/gerar.py`, `scripts/render_guias.py`, `conteudos/guias_imagens.py`, `assets/css/styles.css`, `assets/js/guias.js`,
os oito HTML de Guias, os créditos, a pesquisa, as exportações e os testes de Guias.
Os registos de fontes/imagens e de execução ficam em `editorial/` e `tmp/guias-qa/`.
As demais páginas e os dados de Produtos foram preservados.

- Geração completa: `python scripts/gerar.py` terminou com sucesso. A versão final foi
  regenerada com `python scripts/gerar.py --secao guias` para preservar os textos alheios.
- `python scripts/verificar.py`: 78 páginas e 2713 ligações/recursos locais válidos.
- `node --test testes/pesquisa.test.cjs`: onze testes aprovados, incluindo Guias.
- `python testes/verificar_guias.py`: fontes, datas, rotas, imagens, relações,
  anonimato, pesquisa e exportação consistentes.
- Verificações existentes de Materiais, Produtos e imagens de Produtos aprovadas.
- Verificador geral de imagens: 75 utilizações e 61 ficheiros, com dimensões,
  decodificação, alt e destinos válidos.
- Playwright com o Chrome existente: índice e sete artigos em 360, 390, 768 e
  1440 px; 32 apresentações sem overflow, imagens com proporção natural e sem
  ampliação, navegação, FAQ, índice expansível por teclado e pesquisa funcionais.
- Inspeção visual da entrada, resposta breve em telemóvel, diagnóstico e diagramas.
- Comparação com o estado inicial: páginas alheias preservadas; apenas Guias,
  créditos e índice de pesquisa alterados. Sem referências proibidas nas páginas,
  nos dados públicos ou na pesquisa dos Guias.

Não foi feita publicação nem qualquer alteração ao histórico Git.
