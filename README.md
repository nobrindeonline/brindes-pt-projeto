# brindes.pt — biblioteca informativa da Nobrinde

> Versão local para revisão. Site estático em português de Portugal, sem loja,
> chatbot, base de dados ou recolha de pesquisas. Não foi publicado na Internet.
> A maquete aprovada mantém-se como base: Poppins, branco, azul e cartões
> arredondados.

## Atualizações

### Ocasiões e Sazonalidade — 21 de outubro de 2026

A nova entrada `ocasioes/index.html` reúne quatro cartões e guias próprios:
`natal.html`, `inverno.html`, `carnaval.html` e `verao.html`. Está separada de
Para quem e integrada na navegação partilhada, na página inicial e na pesquisa.

Edite `conteudos/ocasioes.py`; o renderizador é `scripts/render_ocasioes.py`.
São reutilizadas quatro imagens locais, identificadas nos dados, sem criar
ficheiros de imagem novos. O JSON público é `assets/ocasioes-conteudos.json`.
Fontes, âmbito, limitações e verificações estão em `editorial/ocasioes-2026-10-21.md`.

Use `npm.cmd run build` para geração completa, necessária quando muda a navegação
global. Para posteriores alterações apenas aos guias, pode usar
`python scripts/gerar.py --secao ocasioes`. Verifique com `npm.cmd run check`.
Nas três páginas novas de Para quem, a bibliografia final e a ligação de créditos
no corpo ficam ocultas conforme preferência confirmada; as referências inline,
os dados de fontes e os créditos gerais mantêm-se.

### Para quem — Crianças, Agricultura e Animais — 21 de outubro de 2026

A secção tem onze guias, incluindo `publicos/criancas.html`,
`publicos/agricultura.html` e `publicos/animais.html`. Os oito guias anteriores
mantêm as rotas e os conteúdos. A integração dos novos temas está em
`conteudos/publicos_novos.py`, carregado por `conteudos/publicos.py`.

Os três novos guias usam os cartões e a leitura existentes, acrescentando
personalização, cuidados e fontes com âmbito explícito. O gerador inclui estes
campos na pesquisa e em `assets/para-quem-conteudos.json`.
As imagens locais de `assets/para_quem` são selecionadas em
`conteudos/publicos_imagens.py`; o preparador copia-as sem transformação para
aliases neutros em `visuais/` e regista a origem no manifesto editorial.

Gere com `python scripts/gerar.py --secao publicos` e verifique com
`npm.cmd run check`. Consulte `editorial/publicos-novos-2026-10-21.md` para
fontes, escolha de imagens e limites. Não foram criadas páginas sazonais.

### Organização dos ficheiros — 21 de outubro de 2026

- `scripts/`: gerador, renderizadores e verificadores gerais.
- `assets/js/` e `assets/css/`: JavaScript e estilos públicos.
- `docs/`: brief e registos de apoio.
- `../arquivo/referencias/`: PDFs de referência, fora da pasta publicada.
- `../arquivo/backups/`: ZIPs de arquivo, fora da pasta publicada.

As páginas mantêm os URLs. Configurações, README, páginas de entrada,
pesquisa, créditos e robots.txt continuam na raiz. As ferramentas, documentos
e fontes editoriais são excluídos da publicação por `.assetsignore`.

Gere com `npm run build` ou `python scripts/gerar.py`. Verifique tudo com
`npm run check` ou `python scripts/verificar_tudo.py`. A verificação usa o
ambiente `.venv` existente quando são necessários os testes de imagens.
Não existe publicação automática nestes comandos.

### Produtos — 21 de outubro de 2026

A entrada apresenta dez cartões visuais. As cinco áreas antes ligadas a
conteúdos provisórios têm guias próprios: Casa, Desporto, Eventos, Mobilidade
e Embalagem. As seis famílias anteriores e a coleção transversal Premium
conservam os URLs; os guias existentes foram desenvolvidos com novas variantes
e critérios. A secção tem agora doze artigos.

Edite `conteudos/produtos.py`, `conteudos/produtos_complementos.py` e
`conteudos/produtos_areas.py`. A seleção das 29 imagens locais está em
`conteudos/produtos_imagens.py`; todas usam cópias públicas neutras e preservam
os originais das dez pastas. Não se deduzem materiais ou certificações dos
nomes dos ficheiros.

Execute `python scripts/gerar.py --secao produtos`,
`python editorial/gerar_fontes_produtos.py`, `python scripts/verificar.py`,
`python testes/verificar_produtos.py`,
`.venv/Scripts/python.exe testes/verificar_produtos_imagens.py` e
`node --test testes/pesquisa.test.cjs`.
O relatório da revisão, fontes e limites está em
`editorial/produtos-guias-2026-10-21.md`.

### Mercado — 14 de outubro de 2026

A entrada `mercado/index.html` reúne seis áreas de produto: Papelaria e
Escritório; Tecnologia e Acessórios Digitais; Casa, Lazer e Bebidas; Têxtil e
Vestuário; Sazonalidade e Clima; Brindes Ecológicos. Cada area apresenta tres ou quatro
exemplos ligados aos perfis canónicos. São catorze entradas selecionadas, com
Velilla Group / MUKUA num único perfil. Dimatur e Eurovinil mantêm os perfis
complementares; os seis guias anteriores de cadeia conservam as rotas.

Edite `conteudos/mercado_areas.py`, `conteudos/mercado_novos_perfis.py` e
`conteudos/perfis_mercado.py`. A integração está em `conteudos/mercado.py`;
`scripts/render_mercado.py` reutiliza os componentes comuns. Gere com
`python scripts/gerar.py --secao mercado`: atualiza entrada, artigos e pesquisa de
Mercado, preservando as outras secções.

As fontes públicas, limites de cada perfil, candidatas não incluídas e
resultados de verificação estão em [editorial/fontes-mercado.md](editorial/fontes-mercado.md),
reproduzível com `python editorial/gerar_fontes_mercado.py`. Mercado segue a
indexabilidade de Indústria; não altera as diretivas das restantes secções.
Não existe sitemap nem domínio canónico confirmado neste projeto.

Os cartões reutilizam imagens locais inspecionadas e selecionadas em
`conteudos/mercado_imagens.py`. A geração
prepara cópias com nomes neutros em `assets/mercado/visuais/`, preservando os
originais. Os logótipos estão mapeados em `conteudos/mercado_empresas.py`.

Os dezasseis perfis incluem história, operação, especialização, limites e
fontes por secção, conforme a informação disponível. Para regenerar artigos
e pesquisa preservando a entrada aprovada, use
`python scripts/gerar.py --secao mercado --preservar-entrada`. As fichas-resumo usam os
logótipos locais de `assets/mercado/Empresas/`. O dossier de fontes regista as
afirmações publicadas e as informações que não puderam ser confirmadas.

Verifique com `python scripts/verificar.py`, `python testes/verificar_mercado.py`,
`node --test testes/pesquisa.test.cjs` e `npm.cmd run format:check`.

### Costura, argolagem e encadernação — 7 de outubro de 2026

A entrada [`tecnicas/costura-argolagem-e-encadernacao.html`](tecnicas/costura-argolagem-e-encadernacao.html)
reúne três guias completos. Edite `conteudos/montagem.py` e execute
`python scripts/gerar.py` para atualizar o HTML e a pesquisa. Os guias anteriores de
Indústria mantêm as rotas.

Fontes, seleção de imagens e confirmações pendentes estão em
[`editorial/fontes-montagem.md`](editorial/fontes-montagem.md). Os originais
locais não foram alterados.

### Transfers — 30 de setembro de 2026

A entrada [`tecnicas/transfers.html`](tecnicas/transfers.html) liga os guias de
Transfer Serigráfico, Transfer Digital, Transfer Digital com Base e DTF. O
conteúdo está em `conteudos/transfers.py`; use `python scripts/gerar.py` para atualizar
páginas e pesquisa.

As definições comerciais de Digital e Digital com Base precisam de confirmação
pela Nobrinde. A entrada de Técnicas apresenta apenas Transfers; as quatro
modalidades são exploradas dentro dessa página. Cinco imagens de
`assets/tecnicas/Transfers/` foram integradas após autorização expressa do
utilizador, sem alterar os originais e com créditos e legendas factuais.

Fontes, inventário e verificações estão em
[`editorial/fontes-transfers.md`](editorial/fontes-transfers.md) e
[`editorial/imagens-por-confirmar.md`](editorial/imagens-por-confirmar.md).

### Tendências — integração de 28 de setembro de 2026

A listagem [`tendencias/index.html`](tendencias/index.html) reúne quatro artigos
do pacote editorial recebido e as três ideias existentes. Os novos textos,
fontes, data editorial, classificação e confirmações pendentes são mantidos em
`conteudos/novidades.py`, integrado em `ARTIGOS` por `conteudos/catalogo.py`.
`novelty_article` em `scripts/gerar.py` reutiliza o cabeçalho, rodapé, leitura e
navegação comuns; `idea_listing` constrói os sete cartões. A geração e a
pesquisa não dependem dos Markdown originais fora do projeto.

Os três produtos estão identificados como novidades nas fontes dos
fornecedores; a SMART collection fica como coleção em destaque enquanto a
página original da PF Concept não puder ser reconfirmada. As propostas visuais
dos Markdown são notas editoriais, não fotografias disponíveis: foram usados
painéis tipográficos próprios. As instruções de integração do pacote não
constituem autorização para publicar.

Gere com `python3 scripts/gerar.py` após `npm ci`. Verifique com `python3 scripts/verificar.py`
e `node --test testes/pesquisa.test.cjs`. Consulte
[`editorial/integracao-tendencias.md`](editorial/integracao-tendencias.md) para
evidências, ficheiros e validações pendentes.

### Artigos e fotografias

#### Para quem

A secção está em `publicos/index.html`, com seis guias próprios: `empresas.html`,
`camaras-municipais.html`, `escolas.html`, `clubes-desportivos.html`,
`revendedores.html` e `eventos.html`. Edite as introduções, seleções e
justificações em `conteudos/publicos.py`.

Os factos e fotografias continuam centralizados em `conteudos/recursos.py`; a
pesquisa inclui também as justificações e referências das escolhas. Após
gerar, atualize o registo com `python editorial/gerar_fontes_catalogo.py`.

#### Tendências e artigos

Abra `tendencias/index.html` por duplo clique no Explorador de Ficheiros para
ver a grelha editorial. Os três cartões abrem artigos próprios sobre garrafas,
sacos para eventos e kits de boas-vindas. Também pode usar o servidor local
descrito em [Abrir e rever](#abrir-e-rever) e abrir
<http://127.0.0.1:8765/tendencias/index.html>.

Os textos são artigos e ideias, sem data de notícia. Edite-os em
`conteudos/ideias.py`; a listagem e os artigos usam as funções `idea_listing` e
`idea_article` de `scripts/gerar.py`. Cada artigo identifica as fotografias em `imagens`
e, quando necessário, uma lista adicional de produtos citados no texto.

#### Fotografias, créditos e verificação

As cinco fotografias de técnicas estão em `assets/tecnicas/`. Foram extraídas
12 fotografias individuais do catálogo para `assets/produtos/`. Os créditos
estão em [`creditos-imagens.html`](creditos-imagens.html), acessível em todos
os rodapés; o registo editorial completo está em
`editorial/fontes-catalogo.md`. As sete categorias de produtos têm agora
páginas próprias, além dos guias existentes.

Depois de alterar os conteúdos, execute `python scripts/gerar.py` e
`python editorial/gerar_fontes_catalogo.py`. Para verificar também as imagens,
execute `.venv/Scripts/python.exe testes/verificar_imagens.py`. Este teste
adicional usa Pillow; a extração usa PyMuPDF e Pillow, instalados no ambiente
local `.venv`. A geração normal e a navegação não dependem desses pacotes.

Os ficheiros em `tmp/pdfs/` são apenas material de inspeção local e podem
conter páginas originais com preços; não são ligados nem carregados pelo site.

### Secção Indústria — 14 de outubro de 2026

#### Cartões e navegação

A entrada apresenta quatro cartões: História dos Brindes, Da ideia à entrega,
Máquinas e processos e Montagem e acabamentos. Os destinos são:

- `industria/historia-dos-brindes.html`
- `industria/da-ideia-a-entrega.html`
- `industria/maquinas-e-processos.html`
- `industria/montagem-e-acabamentos.html`

A história anterior foi preservada integralmente; o percurso e a lista de
máquinas passaram para páginas próprias. As âncoras antigas da entrada
continuam válidas.

#### Conteúdos e fontes

Abra `industria/index.html` no navegador para consultar o percurso e os 13
guias. Os textos e as 11 etapas são mantidos em `conteudos/industria.py`; a
apresentação é gerada por `scripts/gerar.py` e `assets/css/styles.css`.

As fontes técnicas e históricas estão em
[`editorial/fontes-industria.md`](editorial/fontes-industria.md), reproduzíveis
com `python editorial/gerar_fontes_industria.py`. O registo do catálogo
continua em `editorial/fontes-catalogo.md`.

O conteúdo foi ampliado para explicar a evolução histórica dos brindes, as
etapas possíveis entre a ideia inicial e a entrega e os principais processos
de produção e equipamentos, com ligações para as técnicas correspondentes.
Foi também desenvolvida a parte final do percurso: montagem, controlo final,
embalagem e preparação para expedição, incluindo o encaminhamento para o
transportador e a entrega. O texto distingue etapas que podem variar de
projeto para projeto e não apresenta um fluxo empresarial como universal.

#### Imagens e apresentação

As imagens de `assets/industria/` foram organizadas por tema para apoiar os
cartões e os artigos. A apresentação da página foi afinada para mostrar uma
imagem adequada no primeiro cartão, evitar a duplicação do título sobre a
imagem e no texto e dar mais largura ao texto introdutório de Indústria.

#### Descoberta e indexação

A secção destina-se a ser pública e descoberta por motores de pesquisa e
sistemas de IA. Antes da disponibilização pública, é necessário verificar:

- o domínio;
- as regras de rastreio;
- os canonicals;
- o sitemap.

A possibilidade de rastreio não garante indexação.

### Sublimação — técnica de personalização

O guia `tecnicas/tecnica-sublimacao.html` usa o modelo comum das técnicas e é
mantido em `conteudos/sublimacao.py`. O ID é distinto do guia de equipamentos já
existente em `industria/sublimacao.html`. As relações são registadas em
`conteudos/catalogo.py`; a listagem de Técnicas e a pesquisa são atualizadas
pelo gerador habitual.

As quatro imagens em `assets/tecnicas/Sublimacao/` foram incluídas após
autorização expressa do utilizador em 28/09/2026, com legendas e créditos. A
origem/autoria continua por documentar; os originais não foram alterados.
Consulte `editorial/fontes-sublimacao.md` e
`editorial/imagens-por-confirmar.md`.

## Abrir e rever

Abra `index.html` no navegador. Os artigos, a navegação e a pesquisa funcionam
também através de ficheiros locais. A fonte Poppins requer Internet; existe uma
alternativa de sistema quando não está disponível.

Para iniciar um servidor local, abra um terminal nesta pasta e execute:

```powershell
python -m http.server 8765 --bind 127.0.0.1
```

Abra <http://127.0.0.1:8765> e termine o servidor com `Ctrl+C`. Este comando
serve apenas o computador local; não é um processo de publicação.

## O que foi criado

- Página inicial, pesquisa e índices das oito secções.
- Guias de tampografia, serigrafia, gravação a laser, impressão digital UV e
  bordado.
- Guia «Como escolher a técnica» e página «Canetas e escrita».
- Percursos de navegação, índices dentro dos artigos, fontes e assuntos
  relacionados.
- Pesquisa nos artigos e nos assuntos dos índices, sem distinguir acentos ou
  maiúsculas.
- Menu adaptável com indicação de estado e fecho por Escape; foco visível e
  ligação para saltar para o conteúdo.
- Planeamento dos restantes assuntos sem publicar artigos vazios.

As páginas técnicas são sínteses iniciais para revisão. A data de revisão
documental não equivale à aprovação da Nobrinde. Não há casos reais de produção
porque ainda não foram fornecidos. Os exemplos da página inicial estão
identificados como ilustrativos.

## Organização do projeto

| Caminho                       | Conteúdo                                      |
| ----------------------------- | --------------------------------------------- |
| `index.html`, `pesquisa.html` | Páginas geradas                               |
| `tecnicas/`, `materiais/`, …  | Índices e artigos HTML gerados                |
| `assets/css/styles.css`                  | Estilos da maquete e da biblioteca            |
| `assets/js/script.js`                   | Menu e navegação                              |
| `assets/js/pesquisa.js`                 | Pesquisa local                                |
| `assets/pesquisa-dados.js`    | Índice gerado, sem dados privados             |
| `conteudos/catalogo.py`       | Conteúdos, relações, fontes e data de revisão |
| `conteudos/modelos.py`        | Modelos: técnica, material, produto e guia    |
| `modelos/inicio.html`         | Corpo editável da página inicial              |
| `scripts/gerar.py`                    | Cabeçalho, rodapé e renderização partilhada   |
| `scripts/verificar.py`                | Verificação de páginas, recursos e âncoras    |
| `testes/pesquisa.test.cjs`    | Testes da pesquisa                            |
| `editorial/plano.md`          | Mapa completo e temas pendentes               |
| `editorial/validacoes.md`     | Afirmações e dados por validar pela Nobrinde  |
| `editorial/verificacao.md`    | Resultados e limitações da verificação        |

## Alterar uma página

### Crachás tipo pin/botão

O guia está em `tecnicas/crachas-automaticos.html`. O conteúdo, componentes,
passos, FAQ, imagem e fontes estão em `conteudos/crachas.py`. O título delimita
o produto e o texto explica o alcance da prensagem automática. Conserva-se
`industria/producao-de-crachas.html`, com ligação ao novo guia. Consulte
`editorial/fontes-crachas.md` para fontes, verificações e confirmações.

### Troquelagem

A técnica está em `tecnicas/tecnica-troquelagem.html`, com conteúdo em
`conteudos/troquelagem.py`. Conserva-se o guia de equipamentos em
`industria/troquelagem.html`. Fontes consultadas, seleção das imagens locais,
verificações e pontos a confirmar estão em
`editorial/fontes-troquelagem.md`.

### Materiais

A secção Materiais tem uma entrada e sete guias completos, mantidos em
`conteudos/materiais.py`. As funções `material_listing`, `material_article` e
`material_media` de `scripts/gerar.py` reutilizam os cartões, navegação e leitura do
site. As âncoras antigas da entrada são preservadas. As fotografias reutilizam
`assets/produtos/` e têm legendas descritivas, sem referências ao catálogo.

O registo interno é reproduzível com `python editorial/gerar_fontes_materiais.py`.
Depois de gerar, execute também `python editorial/gerar_fontes_catalogo.py` e
`python testes/verificar_materiais.py`. Consulte
`editorial/fontes-materiais.md` para fontes por tema e confirmações por artigo.

### Guias

A secção Guias tem sete artigos completos. Os seis novos guias e os seus
esquemas/listas estão em `conteudos/guias.py`; o guia «Como escolher a
técnica» conserva o texto inicial em `conteudos/catalogo.py`, com complementos
do mesmo módulo de guias. `guide_listing` e `guide_article` em `scripts/gerar.py` usam
o cabeçalho e rodapé comuns.

Consulte `editorial/fontes-guias.md` para fontes, resultados das verificações e
pontos de validação. O registo por artigo no catálogo é reproduzível com
`python editorial/gerar_fontes_catalogo.py`.

### Guias «Para quem»

Os oito guias são mantidos em `conteudos/publicos.py`, com destinatários,
ocasiões, locais, épocas, objetivos, famílias genéricas, critérios, fontes,
etiquetas e relações estruturadas. As imagens dos cartões usam aliases neutros
em `assets/para_quem/visuais/`.

Para regenerar apenas esta secção, execute `python scripts/gerar.py --secao publicos`.
O processo também atualiza a pesquisa e `assets/para-quem-conteudos.json`, que
conserva os campos para consulta estruturada.

## Gerar e verificar

Depois de alterar conteúdos, execute os comandos necessários e recarregue a
página no navegador. Para a geração completa e verificações gerais:

```powershell
python scripts/gerar.py
python editorial/gerar_plano.py
python scripts/verificar.py
node --test testes/pesquisa.test.cjs
```

Python 3 gera o site usando a biblioteca padrão. Node.js e a dependência de
desenvolvimento Prettier são necessários para a formatação automática no fim
da geração; Node.js também executa os testes JavaScript. O site gerado continua
estático e não precisa destas ferramentas para ser navegado.

### Formatação dos HTML

Na primeira utilização (ou após atualizar as dependências), execute `npm ci`.
Depois, use normalmente `python scripts/gerar.py`: o comando gera as páginas e aplica
automaticamente o Prettier a todos os HTML do projeto, incluindo o modelo
inicial. Se Node.js ou Prettier estiverem em falta, a geração avisa antes de
escrever páginas.

Para formatar apenas, use `npm run format`. Para confirmar o estilo sem
modificar ficheiros, use `npm run format:check`. Em PowerShell, se a política
impedir `npm`, use `npm.cmd` nos mesmos comandos.

O estilo está em `.prettierrc.json`: dois espaços, um atributo por linha
quando há vários atributos, largura de referência de 100 caracteres e finais
de linha LF. A opção `htmlWhitespaceSensitivity: css` conserva os espaços
significativos dos elementos inline; CSS e JavaScript incorporados não são
reformatados. A versão do Prettier está fixada em `package.json` e
`package-lock.json`. `node_modules`, `.venv` e `tmp` ficam excluídos. As
integrações de Prettier no editor usam a mesma configuração.

Edite os conteúdos Python/modelos e volte a gerar, em vez de alterar
diretamente as páginas geradas.

## Acrescentar conteúdo

1. Consulte `editorial/plano.md` e complete as fontes antes de publicar um
   artigo local.
2. Use `novo('tecnica')`, `novo('material')`, `novo('produto')` ou
   `novo('guia')` de `conteudos/modelos.py` como estrutura. Copie os campos
   para uma nova entrada de `ARTIGOS`.
3. Escolha um `id` estável, em minúsculas e com hífen, sem acentos. Exemplo:
   `aluminio`.
4. Preencha `sec`, `titulo`, `resumo`, `seccoes`, `problemas`, `fontes`,
   `relacionados`, `ancoras` e `tags`. Use listas vazias apenas quando o campo
   não se aplica.
5. Registe fontes públicas em `FONTES`; num parágrafo, `[chave]` cria uma
   referência à fonte.
6. Em `relacionados`, use IDs de artigos existentes. Em `ancoras`, use
   destinos existentes, como `materiais/index.html#metais`. Registe as
   relações inversas onde fizer sentido.
7. Gere e verifique novamente. O novo artigo entra no índice da sua secção e
   na pesquisa.

Não mude IDs de páginas já divulgadas sem prever redirecionamento. Não publique
texto por validar como facto: registe-o em `editorial/validacoes.md`. Para um
artigo de atualidade, acrescente primeiro um modelo com data de publicação
visível e categoria de notícia; não o apresente como guia permanente.

Edite o corpo da página inicial em `modelos/inicio.html`. Os seus destaques
são curadoria manual: ao trocar um artigo, atualize o respetivo cartão e
destino. Cabeçalho, rodapé, páginas de secção e artigos partilham funções de
`scripts/gerar.py`. Não altere diretamente o HTML gerado se pretender conservar a
alteração na próxima geração.

## Verificação e próximos passos

Consulte `editorial/verificacao.md` para resultados exatos. O ambiente desta
sessão não disponibilizou um navegador ligado às ferramentas: a inspeção
visual em desktop e telemóvel continua pendente, embora os estilos responsivos
estejam implementados.

Antes de aprovar a apresentação, reveja larguras de 360, 390, 768 e 1440 px:
menu, pesquisa, leitura dos artigos, navegação por teclado e ausência de
deslocamento horizontal. Experimente «gravacao», «canetas», «DTF», pesquisa
vazia e uma palavra inexistente.

As páginas incluem `noindex, nofollow` por serem uma versão de revisão. Uma
futura publicação deve ser preparada separadamente, com aprovação dos
conteúdos e escolha explícita dos ficheiros públicos. Não envie `editorial/`,
o brief ou os scripts internos para alojamento público. `noindex` não é um
mecanismo de privacidade.
