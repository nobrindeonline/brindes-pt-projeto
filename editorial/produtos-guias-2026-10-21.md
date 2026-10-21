# Revisão e desenvolvimento de Produtos — 21 de outubro de 2026

## Estrutura revista antes da edição

Foram revistos o README, os registos editoriais anteriores, a fonte semântica
de Produtos, a integração no catálogo, o renderizador, o gerador, as classes de
cartões e grelha, os testes e todos os caminhos recursivos de assets/produtos.
Não existe AGENTS.md aplicável. Foram preservadas as alterações anteriores e
as fotografias novas colocadas nas cinco pastas pelo utilizador.

O site gera HTML a partir de Python. PRODUTOS alimenta NOVOS_ARTIGOS, a pesquisa
semântica, o JSON público e o renderizador. AREAS define os dez cartões. Os
novos conteúdos foram integrados por produtos_complementos.py antes da criação
de NOVOS_ARTIGOS, mantendo uma única estrutura final de dados. Não se editaram
os HTML manualmente, nem se alteraram CSS ou navegação global.

## Páginas e integração

Novas rotas em produtos/:

- casa-decoracao-e-cuidados-pessoais.html
- desporto-lazer-e-exterior.html
- eventos-identificacao-e-premios.html
- mobilidade-ferramentas-e-seguranca.html
- embalagem-e-apresentacao.html

As sete rotas anteriores foram preservadas. Há onze guias de famílias e uma
coleção transversal. Os dez cartões ligam a Produtos; o primeiro reúne os
dois guias de escrita e escritório. Premium continua fora da grelha principal.
As âncoras antigas mantêm-se. Os novos guias recebem ligações relacionadas
de outros artigos, ligam aos materiais e técnicas pertinentes e entram na
pesquisa e na exportação estruturada.

Foram acrescentados marcadores; calendários e organização de secretária;
cabos e acessórios de computador/telemóvel; térmicos, copos de viagem,
garrafas de atividade, lancheiras e utensílios; sacos dobráveis e térmicos,
desporto, computador e viagem; roupa de trabalho/desporto e acessórios.
Os cinco novos guias têm variantes, critérios próprios, contextos, componentes,
zonas de personalização, condições de técnica, limites, cuidados, FAQ e fontes.

Os critérios de observação, encaixe, organização, conforto de utilização e
abertura são orientação editorial. Não são resultados de ensaios. Não se
publicaram estatísticas nem relações comerciais; não se usou Excel como fonte.

## Pesquisa pública e âmbito das fontes

As fontes novas foram consultadas publicamente nesta execução. Estão também
no registo reproduzível fontes-produtos.md e nos pontos pertinentes dos guias:

- Comissão Europeia, materiais em contacto com alimentos: âmbito de
  recipientes, utensílios, louça e embalagem. Sem validação de um modelo.
- Comissão Europeia, equipamento de proteção individual: distinção pela
  finalidade de proteção e documentação aplicável. Nenhuma fotografia foi
  apresentada como prova de proteção ou conformidade.
- FEFCO, construções de caixas: distingue sistemas construtivos. Não foi
  usado para atribuir resistência, reciclabilidade ou aptidão para expedição.
- Governo do Reino Unido, segurança de velas: orientação doméstica sobre
  chama, vigilância e afastamento de materiais inflamáveis; sem aplicar regras
  de certificação ou de jurisdição ao leitor português.
- CNIL, exemplo de informação em acesso por cartão: ilustra informação sobre
  tratamento de dados. Não demonstra tecnologia eletrónica de um cartão.

Foram ainda consultados os documentos públicos USB-IF e GINETEX, já presentes
na bibliografia, para rigor na distinção entre conector/protocolo/função e nos
cuidados têxteis. As datas antigas dessas referências não foram substituídas
por uma falsa data nova de revisão integral. O renderizador mostra agora as
datas reais de cada referência e artigo, em vez de uma data textual fixa.

## Imagens e créditos

As treze fotografias novas foram inspecionadas numa folha de contacto local.
Foram integradas doze; os óculos não foram usados porque não acrescentavam
informação visual necessária às ferramentas e à peça vestível já ilustradas.
Não foram criadas nem procuradas imagens externas.

| Área | Cartão | Imagens adicionais |
| --- | --- | --- |
| Papelaria | Calendário de mesa | Régua, organizador e estojo nos dois guias |
| Tecnologia | Dispositivo e telemóvel | Mostrador e base com cabo |
| Bebidas | Canecas | Copos e recipiente com pega |
| Sacos | Sacos de duas alças | Cordões e pasta |
| Têxtil | T-shirt | Vestuário desportivo e bonés |
| Casa | Manta enrolada com peluche | Luvas de cozinha, sem garantia térmica |
| Desporto | Cadeira dobrável | Saco de desporto |
| Eventos | Porta-cartões | Medalhas e placa transparente |
| Mobilidade | Ferramenta dobrável | Fita graduada e peça vestível amarela |
| Embalagem | Caixa com pega | Embalagem alta com pegas |

Todos os cartões têm imagem adequada, embora nenhuma foto ilustre todos os
tipos da sua área. Os artigos incluem dezoito imagens; o manifesto tem 29
ficheiros distintos, contando os cartões próprios de onze guias de família.
Os nomes públicos são neutros; originais e integridade binária foram mantidos.
Não se inferiram composição, número de funções, homologação ou certificação
dos nomes originais. Foram atualizados os créditos e o manifesto editorial.
Autoria e licença individual continuam sem identificação nos registos;
não se inventou atribuição ou licença aberta.

## Validação e limites

- Geração normal, limitada a Produtos para preservar o âmbito.
- verificar.py: 114 páginas, mais de 4300 ligações/recursos locais válidos.
- verificar_produtos.py: dez cartões completos, destinos próprios, doze artigos,
  fontes, relações recebidas pelos novos guias, pesquisa e JSON consistentes.
- verificar_produtos_imagens.py: 29 ficheiros decodificados, dimensões,
  integridade, seleção por pasta, alt e créditos válidos.
- pesquisa.test.cjs: doze testes, com novos casos para os cinco guias e para
  variantes acrescentadas aos guias existentes.
- Formatação HTML verificada pelo Prettier.

Não existe navegador disponível através da ferramenta de revisão visual nesta
sessão. A grelha e os breakpoints existentes foram preservados; não se afirma
validação visual de layout em desktop ou telemóvel nesta execução.

Não faltam imagens para os dez cartões. Continuam dependentes de documentação
do artigo concreto: conservação térmica, estanquidade, alimentação, protocolos,
carga, resistência, contacto alimentar, função de proteção, precisão e cuidados.
Essas lacunas são explicadas como critérios, não preenchidas com garantias.
Sem commit, push ou publicação.
