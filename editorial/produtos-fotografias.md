# Produtos — atualização visual de 12 de outubro de 2026

## Estado inicial e âmbito

Consultou-se o Git antes de editar. Existiam as alterações locais da reformulação
anterior, seis novas pastas de fotografias e remoções dos antigos visuais WebP e
do respetivo manifesto. Todas estas alterações foram preservadas. Não se repuseram
ficheiros eliminados e não houve commit, push ou publicação.

Analisaram-se a entrada, a fonte semântica `conteudos/produtos.py`, o índice Python
`conteudos/catalogo.py`, as relações de imagens de `conteudos/recursos.py`,
`render_produtos.py`, as funções de geração de páginas, cartões, imagens e pesquisa,
e os testes. Não foi aberto o documento comercial local nem foram utilizados
os seus dados na redação ou na escolha dos novos textos alternativos.

O utilizador autorizou também corrigir apenas as referências às imagens removidas
em outras secções, sem reescrever os textos. A comparação estrutural com o estado
inicial confirmou esse âmbito: 12 páginas tiveram referências corrigidas e não
houve outras alterações de conteúdo, além dos créditos dos novos visuais.

## Fotografias

Foram abertas e inspecionadas as 20 fotografias das seis pastas indicadas. As
folhas de inspeção estão em `tmp/produtos-fotos-qa/`. Escolheram-se seis imagens
para os cartões e onze para secções dos guias. As três não usadas tinham menor
relevância para a seleção editorial; não foram excluídas por exigir referências
à origem proibida. Não se repetem imagens entre cartões e guias.

| Família | Cartão | Visuais adicionais |
|---|---|---|
| Canetas e escrita | Estojo aberto com dois instrumentos de escrita | Estojo transparente |
| Garrafas, copos e canecas | Canecas com pegas e interiores de várias cores | Dois copos; recipiente com pega superior |
| Têxteis | Pessoa com t-shirt e calções | Pessoa com calças justas e top; quatro bonés |
| Sacos e mochilas | Três sacos de duas alças | Sacos de cordões; pasta com pegas e alça |
| Tecnologia | Telemóvel e objeto retangular | Dispositivo com mostrador; base circular com cabo |
| Artigos de escritório | Calendário de mesa | Régua; suporte com instrumentos de escrita e mostrador |

Os textos alternativos descrevem apenas o visível, sem modelos, marcas, composição,
autonomia, capacidades ou funções deduzidas dos nomes de ficheiro. As fotografias
não são fontes das explicações técnicas. Premium mantém-se como bloco textual.

`conteudos/produtos_imagens.py` é a seleção única. A preparação automática copia
os ficheiros binariamente para `assets/produtos/visuais/`, com nomes públicos
neutros. Não há recorte, conversão, ampliação, remoção de metadados nem alteração
dos originais. Os hashes SHA-256 das cópias são iguais aos dos originais.

O manifesto público é gerado em `assets/produtos/visuais/imagens.json`. A relação
dos nomes de origem com os nomes públicos e os registos de utilização local
ficam apenas em `editorial/produtos-imagens.json`. Os comentários JPEG registam
o software de codificação, não autoria ou licença; não se inferem direitos a
partir desses comentários.

A utilização local destas pastas foi expressamente solicitada. Autoria e licença
de terceiros não estão identificadas nos registos disponíveis; não se inventaram
créditos, autorização de terceiros ou licença aberta. Os créditos públicos
encontram-se em `creditos-imagens.html#produtos-ilustrativos`, com formulação neutra,
sem entidade mantenedora, modelos, nomes de origem ou tramitação interna.

## Conteúdo e dados

Mantiveram-se os seis guias, a coleção Premium e todas as rotas e âncoras anteriores.
A grelha única utiliza o mesmo tipo de cartão, fundo, enquadramento e ligação
de leitura de Materiais. As restantes imagens aparecem nas secções adequadas
dos guias. Não se usam fotografias de uma pasta para representar outra família.

A fonte semântica mantém variantes, usos, componentes por parte do artigo,
zonas de personalização, condições de técnica, critérios, cuidados, limitações,
perguntas, sinónimos e fontes. `assets/produtos-conteudos.json` continua a ser
gerado da fonte; agora inclui metadados públicos das imagens, com
`funcao: ilustrativa` e `fonte_tecnica: false`. Não inclui nomes de origem,
registos editoriais, autorizações internas ou dados comerciais. Não foi criado
chatbot, modelo ou base de dados.

Mantiveram-se as 13 fontes técnicas efetivamente consultadas na reformulação
anterior, registadas em `fontes-produtos.md`. Foram reconfirmadas nesta atualização
as páginas/documentos de Pilot Rollerball, USB-IF e GINETEX. Não foram acrescentadas
afirmações técnicas a partir das novas fotografias. Continuam excluídas garantias
não documentadas de desempenho térmico, estanquidade, carga, autonomia, velocidade,
resistência, sustentabilidade e compatibilidade automática de técnicas.

## Geração e verificações finais

- `python gerar.py`: preparação de 17 visuais e geração completa de 78 páginas
  bem-sucedidas. Os geradores de imagens antigas respeitam a remoção do manifesto.
- A versão final foi produzida com `python gerar.py --secao produtos`, preservando
  os textos anteriores das outras secções e aplicando apenas as correções de
  referências autorizadas e os novos créditos.
- `python verificar.py`: 78 páginas; 2712 ligações e recursos locais válidos.
- `node --test testes/pesquisa.test.cjs`: dez testes aprovados.
- `python testes/verificar_produtos.py`: cartões, guias, fontes, pesquisa semântica,
  exportação e nomes públicos neutros consistentes.
- `.venv/Scripts/python.exe testes/verificar_produtos_imagens.py`: 17 imagens das
  pastas corretas, hashes e dimensões iguais aos originais, sem repetição ou créditos
  inventados.
- `python testes/verificar_materiais.py`: verificações existentes aprovadas.
- `.venv/Scripts/python.exe testes/verificar_imagens.py`: 64 utilizações de imagens,
  50 ficheiros; decodificação, dimensões, alt, navegação e ausência de preços válidos.
- Playwright com o Chrome existente: oito páginas em 360, 390, 768 e 1440 px
  (32 combinações), sem overflow; fotografias carregadas, sem ampliação ou alteração
  de proporções; cartões, regressos, menu, FAQ e pesquisa funcionais, sem erros JS.
- Inspeção visual da entrada em desktop e telemóvel e das imagens nos guias.
- Verificação de identidade: saídas de Produtos e manifestos sem identificação da
  entidade mantenedora. A estrutura das páginas alheias foi comparada com o estado
  inicial, descontando apenas as alterações autorizadas.

Registos detalhados e capturas em `tmp/produtos-fotos-qa/`.
