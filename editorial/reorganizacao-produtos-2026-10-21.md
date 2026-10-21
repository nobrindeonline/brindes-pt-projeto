# Produtos — reorganização de 21 de outubro de 2026

## Correção posterior: dez cartões visuais

A pedido do utilizador, as dez áreas estão agora na mesma grelha, cada uma com
imagem, título, descrição e ligação real. Foi removida a navegação de etiquetas
e a divisão entre cinco cartões e cinco blocos de ligações. Reutilizam-se as
classes existentes de cartões, imagem e ligação; não foi necessário alterar CSS.

Casa usa a imagem dos copos e o guia de bebidas; Desporto usa vestuário
desportivo e o guia de clubes; Eventos usa as pulseiras já publicadas em Para
quem e o guia de eventos; Embalagem usa o estojo e a seleção de apresentação.
As cinco imagens foram inspecionadas visualmente antes da seleção.

Mobilidade não dispõe de fotografia de ferramentas ou equipamentos de segurança
nem de guia específico. Usa, como exemplo parcial, o porta-chaves já publicado
em Materiais e liga ao guia de plásticos. A descrição explicita o limite.
O preparador copia essa imagem sem transformação para mobilidade-cartao.jpg,
evitando códigos de produto no URL. A origem permanece registada no código;
os créditos gerais existentes aplicam-se sem atribuição de nova licença.

Não se criaram páginas. Os URLs e as âncoras anteriores mantêm-se. O teste de
Produtos verifica dez cartões ordenados, com imagem, H2, descrição e ligação,
e a ausência da navegação por etiquetas. O teste de imagens decodifica também
os cinco visuais reaproveitados e confirma a integridade da cópia do porta-chaves.
Geração parcial, verificação geral, testes de Produtos, imagens, pesquisa e
formatação aprovados. A ferramenta de navegador não disponibilizou nenhum
navegador nesta sessão; a responsividade foi conservada através da grelha e dos
breakpoints existentes, sem confirmação visual de layout em navegador.

O relato abaixo documenta o estado anterior a esta correção.

## Auditoria anterior à edição

Foram lidos README.md, editorial/integracao-produtos.md, o modelo de conteúdos,
o renderizador, a integração no catálogo, o gerador e os testes de Produtos e
imagens. Não foram encontradas instruções AGENTS.md. O Git estava limpo.

Fonte: conteudos/produtos.py; adaptação para ARTIGOS em conteudos/catalogo.py.
Apresentação: render_produtos.py. Geração: python gerar.py --secao produtos.
Pesquisa: textos_publicos alimenta os sete artigos; os grupos da entrada e o
HTML alimentam a descoberta das áreas. Exportação: assets/produtos-conteudos.json.
Imagens: seis pastas de origem em assets/produtos, seleção em
conteudos/produtos_imagens.py e cópias neutras em assets/produtos/visuais.
O manifesto mantém dimensões, alt, função ilustrativa e ligação aos créditos.

Inventário: seis cartões de família e uma ligação à coleção Premium; sete
artigos e a entrada. Não foram encontrados artigos equivalentes duplicados,
cartões sem destino ou ligações partidas. Escrita e escritório eram famílias
distintas que pertencem agora à mesma área; continuam como dois guias úteis.

| Página existente em produtos/ | Área atual |
| --- | --- |
| canetas-e-escrita.html | Papelaria, escritório e escrita |
| artigos-de-escritorio.html | Papelaria, escritório e escrita |
| tecnologia.html | Tecnologia e acessórios digitais |
| garrafas-copos-e-canecas.html | Bebidas, refeições e cozinha |
| sacos-e-mochilas.html | Sacos, mochilas e viagem |
| texteis.html | Têxtil, vestuário e acessórios |
| brindes-premium.html | Seleção transversal; relacionada com apresentação |

## Implementação e limites

conteudos/produtos_areas.py é a fonte das dez áreas. As cinco áreas com guias
usam os cartões e as imagens existentes. Escrita e escritório têm ligações
distintas no mesmo cartão. As restantes cinco áreas ficam como ligações
relacionadas, conforme a exceção prevista no pedido para conteúdo insuficiente.
Não foram criados artigos vazios nem usadas fotografias sem relação com o tema.
Os caminhos e as sete âncoras anteriores foram preservados.

Os artigos já continham variantes, componentes, contextos, personalização,
limites, critérios, cuidados e referências. Foram mantidos. As menções nominais
a fabricantes no texto e nos rótulos bibliográficos foram neutralizadas,
preservando URLs e âmbito das referências; a identificação original das fontes
continua no código e nos registos editoriais anteriores. Não se acrescentaram
factos técnicos, promessas ambientais ou compatibilidades. Técnicas continuam
como possibilidades gerais sujeitas à confirmação do artigo concreto.

A ligação à área foi acrescentada aos seis guias. Públicos e sazonalidade
remetem para Para quem e Tendências. Premium conserva a rota e a posição
transversal. Não foram alterados CSS, menu global ou conteúdo de outras secções.
O gerador passou a atualizar os créditos no mesmo lugar, evitando a sua
reordenação a cada geração parcial.

## Lacunas dependentes de documentação e imagens adequadas

- Refeições e cozinha: lancheiras, caixas térmicas, utensílios e bar.
- Viagem: malas, bolsas e acessórios específicos.
- Vestuário: roupa de trabalho, chapéus e cachecóis sem guia específico.
- Casa, decoração e cuidados pessoais: velas, higiene e bem-estar.
- Desporto, lazer e exterior: praia, piquenique, jogos e proteção sazonal.
- Eventos, identificação e prémios: fitas, pins, medalhas e troféus. O guia
  técnico de crachás ligado não é uma descrição de toda esta família.
- Mobilidade, ferramentas e segurança: falta guia, fontes e imagem adequada;
  a ligação de materiais é apenas orientação inicial.
- Embalagem: a coleção e o guia de papel/cartão não substituem um guia próprio
  sobre formatos de embalagem e acondicionamento.

Não se criaram páginas para crianças, animais ou setores profissionais.
Os assets de Produtos não fornecem cobertura representativa das cinco áreas
sem guia. Não se extraíram nem descarregaram imagens de catálogos.

## Validação

- Geração normal com --secao produtos, preservando as outras secções.
- verificar.py: 109 páginas e mais de 4100 ligações/recursos locais válidos.
- testes/verificar_produtos.py: dez áreas, cinco cartões, sete rotas, âncoras,
  ligações relacionadas, JSON e presença das áreas na pesquisa.
- testes/verificar_produtos_imagens.py: 17 ficheiros decodificados, dimensões,
  integridade das cópias, manifesto e créditos válidos.
- node --test testes/pesquisa.test.cjs: 12 testes aprovados.
- npm.cmd run format:check: aprovado.

Sem revisão visual em navegador nesta execução. As imagens foram verificadas
por decodificação e manifesto, e a grelha reutiliza os componentes existentes.
Sem commit, push ou publicação.
