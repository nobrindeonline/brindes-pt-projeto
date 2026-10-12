# Reformulação de Produtos — 12 de outubro de 2026

Este registo descreve a primeira reformulação. A atualização posterior com as
fotografias das seis novas pastas, os resultados finais e as correções de
referências autorizadas encontram-se em `produtos-fotografias.md`.

O estado do Git foi consultado antes de editar. Existiam alterações locais em
conteúdos, geração, páginas, imagens de Materiais e registos editoriais; foram
preservadas. Não se fez commit, push ou publicação.

A implementação anterior tinha uma grelha de artigos e grupos repetidos, e os
textos de famílias dependiam de exemplos comerciais. `conteudos/catalogo.py`
é o índice de conteúdos Python: foi analisado e ajustado para integrar a nova
fonte semântica. `conteudos/recursos.py` foi analisado para identificar as relações
entre fotografias, exemplos, artigos e pesquisa; os seus dados comerciais não
foram usados na nova redação. O documento comercial local não foi aberto.

## Fonte, apresentação e rotas

- `conteudos/produtos.py` é a fonte única dos seis guias e da coleção transversal.
  A adaptação `NOVOS_ARTIGOS` mantém o contrato do índice existente.
- `render_produtos.py` gera a entrada, os guias e o JSON público.
- A entrada tem uma grelha única de seis cartões, orientação de escolha e uma
  ligação separada para Premium. Todas as sete rotas anteriores e as âncoras
  `canetas`, `bebidas`, `texteis`, `sacos`, `tecnologia`, `escritorio` e `premium`
  continuam a funcionar.
- Cada guia tem variantes, contextos, critérios, componentes, zonas, condições
  de técnica, cuidados, perguntas de escolha, três perguntas frequentes e fontes.
- As datas documentais públicas referem-se à consulta das fontes. Os registos
  de execução e revisão interna ficam neste diretório.
- O rodapé gerador é neutro e os seletores CSS do logótipo antigo foram removidos.
  A correção de neutralidade já existente foi reparada para respeitar os pares
  de etiquetas HTML. Os destinos de créditos e os índices de exemplos órfãos
  deixados pela limpeza anterior foram corrigidos.

## Exportação e pesquisa

`assets/produtos-conteudos.json` é gerado automaticamente. Inclui ID, slug, URL,
categoria, sinónimos, nomes alternativos, resumo, tipos, contextos, componentes
por parte do artigo, zonas, técnicas e condições, critérios, limitações, cuidados,
perguntas, ligações resolvidas, fontes e data documental. A coleção tem categoria
`colecao_editorial`; as restantes entradas têm categoria `familia`.

As citações do texto-fonte são convertidas em campos `citacoes` com `campo`,
`indice` quando necessário e IDs de fontes. Os textos exportados não contêm HTML.
Todas as técnicas têm `estatuto: possibilidade_geral` e
`compatibilidade_confirmada: false`. O ficheiro contém apenas os dados públicos
de Produtos; não integra registos de aprovação, procedência interna ou exemplos
comerciais. Não foi criado chatbot, modelo ou base de dados.

A pesquisa deriva dos campos semânticos e inclui resumos e sinónimos que não
precisam de ser repetidos artificialmente no corpo das páginas.

## Imagens e afirmações excluídas

Não se usaram as fotografias comerciais locais em Produtos: os registos
disponíveis identificavam imagens por origem, modelos e páginas do documento
cuja referência pública foi excluída. Não se inventaram créditos nem autorização.
Os originais e os registos anteriores de direitos permanecem preservados; as
novas páginas usam cartões tipográficos e não precisam de imagens de produto.

Não foram incluídos valores ou garantias de desempenho térmico, estanquidade,
resistência a quedas ou lavagem, cargas máximas, encolhimento, autonomia,
velocidade de carregamento, vida útil de escrita ou vantagem ambiental. Não havia
documentação revista para os atribuir a artigos específicos. Também não se
declarou compatibilidade confirmada de técnicas com artigos. As páginas indicam
o que comparar ou confirmar, sem converter essas perguntas em promessas.

## Geração e preservação do âmbito

Foi executada a geração completa `python gerar.py`, após reparar uma falha na
neutralização de etiquetas HTML. A geração e a validação completa terminaram
com sucesso. Para a versão final, preservou-se o conteúdo anterior das páginas
alheias a Produtos e executou-se `python gerar.py --secao produtos`. Este modo
regenera os oito HTML de Produtos, pesquisa e JSON, aplicando às restantes páginas
apenas correções de identidade ou de destinos já órfãos.

A comparação do texto público das restantes páginas com o estado inicial não
detetou alterações além da remoção das ligações para exemplos que já não existiam.
Não houve reescrita das outras secções. A formatação automática passou a abranger
apenas as páginas públicas geradas, excluindo cópias editoriais privadas.

## Verificações

- `python gerar.py`: geração completa bem-sucedida; geração final também feita
  com `--secao produtos` para preservar o âmbito.
- `python verificar.py`: 78 páginas, 2715 ligações e recursos locais válidos na
  versão final; H1, idioma, ficheiros, IDs e âncoras válidos.
- `node --test testes/pesquisa.test.cjs`: dez testes aprovados, incluindo sinónimos
  das sete entradas de Produtos e regressão das restantes técnicas.
- `python testes/verificar_produtos.py`: fonte, exportação, citações, rotas,
  ausência de conteúdo proibido e indexação semântica consistentes.
- `python testes/verificar_materiais.py`: verificações existentes aprovadas.
- `.venv/Scripts/python.exe testes/verificar_imagens.py`: 73 utilizações e 41
  ficheiros, decodificação, proporções, alt e navegação válidos. As asserções que
  obrigavam a publicar exemplos comerciais em Para quem foram atualizadas porque
  já contrariavam a neutralização anterior; os controlos reais de imagem mantêm-se.
- Playwright com o Chrome e as ferramentas já instaladas: 32 combinações das
  oito páginas com larguras de 360, 390, 768 e 1440 px; sem deslocamento horizontal,
  menu, FAQ, navegação dos cartões e pesquisa funcionais, sem erros JavaScript.
- Inspeção visual da entrada em desktop e telemóvel e da leitura dos guias.
  Capturas e resultados detalhados em `tmp/produtos-qa/`.

A bibliografia completa, gerada da fonte única, está em `fontes-produtos.md`.
