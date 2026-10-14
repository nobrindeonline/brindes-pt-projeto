"""Conteúdo editorial em português de Portugal. Não contém dados internos."""
from conteudos.produtos import NOVOS_ARTIGOS, FONTES_PRODUTOS, PRODUTOS
from conteudos.bordado import BORDADO, FONTES_BORDADO
from conteudos.termogravura import TERMOGRAVURA, FONTES_TERMOGRAVURA
from conteudos.ideias import IDEIAS
from conteudos.novidades import NOVIDADES
from conteudos.publicos import PUBLICOS
DATA_REVISAO = '2026-09-24'
FONTES = {
 'pad': ('midocean — Tampografia', 'https://www.midocean.com/benelux/us/eur/content/printing-technique-pad-print'),
 'screen': ('midocean — Serigrafia', 'https://www.midocean.com/benelux/us/eur/content/printing-technique-screen-print'),
 'laser': ('midocean — Gravação a laser', 'https://www.midocean.com/benelux/us/eur/content/printing-technique-laser-engraving'),
 'uv': ('midocean — Impressão digital', 'https://www.midocean.com/benelux/us/eur/content/printing-technique-digital-print'),
 'emb': ('midocean — Bordado', 'https://www.midocean.com/benelux/us/eur/content/printing-technique-embroidery'),
 'marabu': ('Marabu — Tintas e auxiliares de tampografia', 'https://www.marabu.com/printing-inks/service-support/knowledge-base/pad-printing-auxiliaries-and-additives'),
 'rotary': ('Trotec — Acessórios de gravação circular', 'https://www.troteclaser.com/en-us/resources/faqs/dimension-rotary-engraving-attachments'),
 'roland': ('Roland DG — Tintas ECO-UV', 'https://www.rolanddg.eu/en-gb/products/inks/eco-uv-inks'),
 'primer': ('Roland DG — Primário e ensaio de impressão', 'https://downloadcenter.rolanddg.com/contents/manuals/LO-640_USE_EN/qyd1700786817898.html'),
 'madeira': ('Madeira — Perguntas técnicas sobre bordado', 'https://www.madeira.com/en-in/service/support/faq'),
 'stabilizer': ('Madeira — Estabilizadores de bordado', 'https://www.madeira.com/hk-en/embroidery-supplies/embroidery-stabilisers'),
 'screenhelp': ('ScreenPrinting.com — Preparação e impressão de t-shirts', 'https://www.screenprinting.com/blogs/news/a-how-to-for-screen-printing-t-shirts'),
}

FONTES.update({k: (f['entidade'] + ' — ' + f['titulo'], f['url']) for k, f in FONTES_PRODUTOS.items()})

# Cada grupo origina uma entrada real no índice, nunca uma página vazia.
SECCOES = [
 {'id':'tecnicas','titulo':'Técnicas de personalização','curto':'Técnicas','icone':'✦','resumo':'Do logótipo ao objeto: conheça o processo, o acabamento e as condições de cada técnica.', 'grupos':[
 ('impressao','Impressão direta','Comece pela forma do objeto, pela superfície e pela imagem que pretende reproduzir. Compare os guias disponíveis antes de escolher.', 'Tampografia|Serigrafia|Serigrafia circular|Impressão digital UV|Impressão digital circular'),
 ('gravacao','Gravação e relevo','Confirme o efeito pretendido numa amostra do artigo: cor, textura e profundidade não são escolhas equivalentes.', 'Gravação a laser|Gravação circular|Termogravura|Baixo-relevo e relevo'),
 ('textil','Têxteis e transferências','Indique a composição da peça, a cor, o local de aplicação e os cuidados de lavagem previstos.', 'Bordado|Transfers|Sublimação|Transferência cerâmica'),
 ('acabamentos','Outras aplicações','O formato final e os componentes do produto fazem parte da escolha do processo.', 'Doming|Troquelagem|Crachás tipo pin/botão'),
 ('montagem','Costura, Argolagem e Encadernação','Explore os processos de união, montagem e acabamento conforme o produto e os materiais.', 'Costura, Argolagem e Encadernação')]},
 {'id':'materiais','titulo':'Materiais','curto':'Materiais','icone':'▥','resumo':'O nome do material é o ponto de partida. O acabamento e a construção do artigo também contam.', 'grupos':[
 ('plasticos','Plásticos','Peça a identificação do polímero e do revestimento. ABS, PP, PVC, PET e Tritan não devem ser tratados como uma superfície única; confirme a tinta e o tratamento com quem vai produzir.', 'ABS|PP|PVC|PET|Tritan'),
 ('metais','Metais','Distinga o metal de base do acabamento visível. Uma caneta pintada e uma superfície metálica sem revestimento podem exigir decisões diferentes.', 'Alumínio|Aço inoxidável|Ferro|Zamak'),
 ('naturais','Madeira e bambu','Observe uma amostra real e a variação entre peças. Na escolha do desenho, pergunte como o veio e o acabamento interferem com a leitura.', 'Madeira|Bambu'),
 ('texteis','Têxteis','Confirme a composição, a estrutura, as costuras e os revestimentos. Softshell e canvas descrevem construções têxteis, pelo que é necessário conhecer também as fibras.', 'Algodão|Poliéster|Softshell|Canvas'),
 ('pele','Pele e imitação de pele','Identifique a composição e o acabamento antes de testar calor, pressão ou tinta. Não presuma equivalência entre pele e materiais que imitam a sua aparência.', 'Pele|Imitação de pele'),
 ('vidro-ceramica','Vidro e cerâmica','Confirme o revestimento, a área utilizável e os cuidados previstos. Peça validação específica para lavagem e para a utilização final do artigo.', 'Vidro|Cerâmica')]},
 {'id':'produtos','titulo':'Produtos','curto':'Produtos','icone':'◈','resumo':'Escolha pela utilização, pelo material e pelo espaço disponível para a sua mensagem.', 'grupos':[
 ('canetas','Canetas e escrita','Compare o corpo, o mecanismo e a posição do clip. O guia de canetas ajuda a preparar a escolha da personalização.', 'Canetas e escrita'),
 ('bebidas','Garrafas, copos e canecas','Indique a capacidade, o tipo de tampa, o material e a forma de lavagem. Confirme onde pode ficar a marca sem interferir com o uso.', 'Garrafas, copos e canecas'),
 ('texteis','Têxteis','Defina o uso, a composição e a gama de tamanhos. Compare bordado e serigrafia tendo em conta a posição e a dimensão do desenho.', 'Têxteis'),
 ('sacos','Sacos e mochilas','Considere o conteúdo a transportar, as costuras, os bolsos e o acesso à zona de personalização.', 'Sacos e mochilas'),
 ('tecnologia','Tecnologia','Confirme a função e a superfície exterior do modelo escolhido. Separe a avaliação da personalização da verificação das características eletrónicas.', 'Tecnologia'),
 ('escritorio','Artigos de escritório','Pense no uso diário e na visibilidade da marca. Capas, folhas e componentes podem precisar de processos diferentes.', 'Artigos de escritório'),
 ('premium','Brindes premium','Defina o que valoriza: utilidade, apresentação, acabamento ou embalagem. Peça uma amostra que permita avaliar o conjunto.', 'Brindes premium')]},
 {'id':'guias','titulo':'Guias práticos e problemas','curto':'Guias','icone':'⌁','resumo':'Perguntas concretas para preparar a arte, comparar opções e rever a maquete.', 'grupos':[
 ('escolher','Escolher e preparar','Reúna informação sobre o produto e o resultado esperado antes de definir a técnica.', 'Como escolher a técnica|Como preparar um logótipo|Ficheiros vetoriais e imagens|Resolução e pormenores mínimos'),
 ('cor','Cor e área de aplicação','Compare a referência de cor, a simulação e uma amostra no suporte final. Registe o que foi aprovado.', 'Pantone e CMYK|Diferenças de cor entre ecrã, maquete e produto|Escolha da área de personalização'),
 ('qualidade','Verificar o resultado','Descreva o defeito observado e as condições de uso. Uma fotografia isolada pode não explicar a causa.', 'Durabilidade|Tratamento de superfícies|Erros frequentes|Falhas de impressão|O que confirmar numa maquete antes de produzir')]},
 {'id':'publicos','titulo':'Para quem','curto':'Para quem','icone':'◎','resumo':'Guias para relacionar destinatários, ocasiões, locais e épocas com famílias de artigos que podem ser avaliadas.', 'grupos':[
 ('empresas','Empresas','Integração, reuniões, formação, visitas e encontros de equipa.', 'Empresas'),
 ('municipios','Câmaras municipais','Iniciativas culturais e desportivas, feiras locais e receção de visitantes.', 'Câmaras municipais'),
 ('escolas','Escolas','Alunos, docentes, famílias e equipas, com atenção à idade e ao contexto.', 'Escolas'),
 ('clubes','Clubes desportivos','Atletas, voluntários, participantes e adeptos; separar lembranças de equipamento técnico.', 'Clubes desportivos'),
 ('revendedores','Revendedores','Preparação de propostas e comparação de famílias genéricas por contexto.', 'Revendedores'),
 ('eventos','Eventos','Congressos, conferências, feiras, festivais e eventos desportivos.', 'Eventos'),
 ('turismo-alojamento','Turismo e alojamento','Acolhimento de hóspedes, visitas guiadas e programas culturais.', 'Turismo e alojamento'),
 ('associacoes','Associações e organizações comunitárias','Voluntariado, sensibilização e atividades comunitárias.', 'Associações e organizações comunitárias')]},
 {'id':'industria','titulo':'Indústria, processos e história','curto':'Indústria','icone':'⚙','resumo':'Acompanhe as etapas de um trabalho e relacione cada máquina com o processo que executa.', 'grupos':[
 ('fluxo','Da arte à expedição','Uma sequência de referência para conversar com a produção: validar o pedido, preparar a arte, aprovar a maquete, produzir, verificar, embalar e expedir. A sequência concreta depende do trabalho.', 'Funcionamento de uma fábrica|Fluxo de produção|Preparação de artes|Impressão|Acabamento|Controlo de qualidade|Expedição'),
 ('maquinas','Máquinas e processos','Nos guias de técnicas encontra o papel dos equipamentos de tampografia, serigrafia, laser, UV e bordado. Modelos e capacidades devem ser confirmados para cada operação.', 'Máquinas de tampografia|Máquinas de serigrafia|Máquinas laser|Máquinas UV|Máquinas DTF|Equipamentos de sublimação|Máquinas de troquelagem|Máquinas de bordado|Máquinas de costura|Máquinas de crachás'),
 ('montagem','Montagem e acabamento','Costura industrial, argolagem e encadernação terão tratamento próprio quando existirem exemplos e documentação suficientes.', 'Costura industrial|Argolagem|Encadernação'),
 ('historia','História dos brindes','Esta área reunirá cronologias documentadas sobre brindes corporativos e técnicas de personalização, incluindo contexto português quando houver fontes.', 'História dos brindes|Brindes corporativos em Portugal|História das técnicas de personalização')]},
 {'id':'mercado','titulo':'Mercado e fornecedores','curto':'Mercado','icone':'◇','resumo':'Um espaço editorial para compreender a cadeia de fornecimento e os seus intervenientes.', 'grupos':[
 ('cadeia','Compreender a cadeia','Ao analisar um interveniente, procure distinguir fabrico do artigo, importação, distribuição, personalização e revenda. Confirme quais dessas funções são documentadas publicamente.', 'Cadeia de fornecimento'),
 ('regioes','Portugal e outros mercados','A organização editorial contempla Portugal, Península Ibérica, Europa e mercado mundial. Ainda não existem perfis de empresas nesta biblioteca.', 'Portugal|Mercado ibérico|Europa|Mundo'),
 ('criterios','Como serão preparados os perfis','Cada perfil deverá identificar a atividade, as fontes públicas e a data de revisão. Contactos privados, condições comerciais e dados internos não fazem parte desta área.', 'Perfis de fornecedores')]},
 {'id':'tendencias','titulo':'Artigos e ideias','curto':'Tendências','icone':'↗','resumo':'Artigos e sugestões de utilização de brindes, com exemplos documentados e conselhos para adaptar ao seu contexto.', 'grupos':[
 ('sustentabilidade','Sustentabilidade e materiais','Ao avaliar uma alegação ambiental, peça o âmbito e a documentação: refere-se ao material, ao artigo, à embalagem ou a uma etapa de produção? Evite concluir a partir de uma palavra isolada.', 'Sustentabilidade|Materiais e circularidade'),
 ('novidades','Tecnologia e novidades','As novidades devem indicar a data, a origem da informação e a aplicação concreta. Ainda não existem notícias publicadas nesta biblioteca.', 'Tecnologia|Novidades do setor|Tendências anuais')]},
]

# Secções de texto: (título, texto). Problemas: (sinal, verificação sugerida).
ARTIGOS = PUBLICOS + IDEIAS + NOVIDADES + NOVOS_ARTIGOS + [
 {'id':'tampografia','sec':'tecnicas','tipo':'tecnica','titulo':'Tampografia','resumo':'Um tampão de silicone transfere tinta para o objeto. Uma opção a considerar em pequenas áreas e formas que exigem adaptação à superfície.',
 'seccoes':[
 ('Como funciona','O desenho é preparado num cliché. O tampão recolhe a tinta e transfere-a para a peça; a impressão de várias cores envolve passagens e alinhamento próprios. [pad]'),
 ('Equipamentos','O conjunto inclui máquina de tampografia, cliché, tampão e suporte de fixação. Antes de produzir, peça confirmação da área acessível e da estabilidade da peça.'),
 ('Materiais e produtos','Pode ser considerada para canetas e pequenos objetos de plástico ou metal. A compatibilidade depende do artigo e do sistema de tinta, não apenas do nome do material. [pad]'),
 ('Cores e acabamentos','É frequente trabalhar com cores diretas. A midocean anuncia até quatro cores e ausência de degradês no seu serviço; esse limite não define toda a técnica nem as capacidades da Nobrinde. [pad]'),
 ('Preparação da arte','Entregue o logótipo original, as dimensões pretendidas e as referências de cor. Peça avaliação dos espaços vazios e dos elementos finos à escala final.'),
 ('Condições a confirmar','Identifique polímero, pintura ou revestimento; confirme tinta, eventual pré-tratamento e cura. A Marabu documenta que viscosidade, limpeza e preparação do suporte influenciam transferência e aderência. [marabu]'),
 ('Limitações','A forma da peça e o alcance do tampão condicionam a aplicação. Não escolha apenas pela dimensão exterior do artigo: confirme a área efetivamente imprimível.'),
 ('Comparar alternativas','Para uma imagem com muitas cores, explore UV. Para uma marca sem tinta num artigo compatível, compare laser. Solicite uma avaliação do mesmo desenho no mesmo produto antes de decidir.')],
 'problemas': [('Tinta não adere','Verificar limpeza, tinta e preparação da superfície com a produção; adicionar catalisador não é uma solução universal. [marabu]'),('Transferência incompleta','Pedir verificação da viscosidade e das condições de transferência antes de alterar a arte. [marabu]')],
 'fontes':['pad','marabu'],'relacionados':['serigrafia','impressao-uv','gravacao-a-laser','canetas-e-escrita','como-escolher-a-tecnica'],'ancoras':['materiais/index.html#plasticos','materiais/index.html#metais'],'tags':'tampao cliché canetas plastico metal pantone aderencia'},
 {'id':'serigrafia','sec':'tecnicas','tipo':'tecnica','titulo':'Serigrafia','resumo':'A tinta atravessa as zonas abertas de uma tela para formar a imagem. A escolha da tela, da tinta e da cura acompanha o produto.',
 'seccoes':[
 ('Como funciona','Uma máscara bloqueia parte da tela. O rodo faz passar tinta nas zonas do desenho. A impressão de várias cores exige separação e alinhamento. [screen]'),
 ('Equipamentos','Tela, rodo, sistema de fixação e equipamento de cura fazem parte do processo. Em têxteis, a preparação inclui a criação da tela e o posicionamento da peça na máquina. [screenhelp]'),
 ('Materiais e produtos','T-shirts e sacos são aplicações possíveis. A serigrafia circular adapta o processo a certos objetos cilíndricos, com rotação durante a impressão. [screen]'),
 ('Cores e acabamentos','Cores diretas são uma possibilidade habitual. A midocean limita o seu serviço descrito a Pantone sem degradês; não se deve transformar essa oferta numa proibição universal. [screen]'),
 ('Preparação da arte','Envie uma versão legível do desenho, com tamanho e posição. Peça confirmação das separações de cor e da eventual necessidade de base.'),
 ('Condições a confirmar','Defina a referência do artigo, a cor do suporte e o uso previsto. Confirme tinta e condições de cura; a aparência seca não substitui a verificação do processo. [screenhelp]'),
 ('Limitações','Pergunte como costuras e irregularidades afetam a área disponível. Num desenho com várias cores, avalie também o alinhamento entre elas.'),
 ('Comparar alternativas','Em têxteis, compare o aspeto da impressão com o relevo do bordado. Para objetos pequenos, consulte tampografia; para imagem digital num suporte compatível, consulte UV.')],
 'problemas':[('Cores desalinhadas','Pedir revisão do registo das telas e do posicionamento da peça. [screenhelp]'),('Resultado não resiste ao uso previsto','Confirmar a tinta, a cura e o ensaio adequado antes de repetir a produção. [screenhelp]')],
 'fontes':['screen','screenhelp'],'relacionados':['tampografia','bordado','como-escolher-a-tecnica'],'ancoras':['materiais/index.html#texteis','produtos/index.html#sacos'],'tags':'tela rodo tshirt camisola saco algodao circular pantone'},
 {'id':'gravacao-a-laser','sec':'tecnicas','tipo':'tecnica','titulo':'Gravação a laser','resumo':'O laser modifica a superfície para criar a marca. O resultado visual deve ser avaliado no material e no acabamento do artigo escolhido.',
 'seccoes':[
 ('Como funciona','A máquina recebe o desenho digital e o feixe atua na superfície. A alteração cria a marca sem a aplicação de tinta de impressão. [laser]'),
 ('Equipamentos','CO₂ e fibra são exemplos de fontes utilizadas para diferentes materiais. Certos sistemas dispõem de acessórios rotativos para peças redondas; dimensões e peso admissíveis variam com a configuração. [laser] [rotary]'),
 ('Materiais e produtos','Canetas metálicas e caixas de madeira são exemplos de aplicações a considerar. A adequação do material e do revestimento precisa de confirmação. [laser]'),
 ('Cores e acabamentos','O aspeto resulta da interação com a superfície. Peça uma amostra de contraste e acabamento; não use uma referência Pantone como garantia do resultado gravado.'),
 ('Preparação da arte','Indique dimensão, orientação e posição. Peça uma prova que permita verificar letras pequenas e áreas preenchidas na escala real.'),
 ('Condições a confirmar','Confirme a composição do artigo, o revestimento e a configuração disponível. Em peças cilíndricas, verifique fixação, diâmetro e alcance do equipamento. [rotary]'),
 ('Limitações','Não é correto excluir todas as superfícies curvas: existem sistemas rotativos. Também não é prudente prometer um resultado idêntico em todos os lotes de madeira. [rotary] [laser]'),
 ('Comparar alternativas','Se a prioridade for reproduzir cores de marca, compare tampografia e UV num artigo compatível. Se valorizar o efeito do próprio material, avalie uma amostra de laser.')],
 'problemas':[('Contraste abaixo do esperado','Comparar a amostra com o acabamento real; pedir à produção avaliação do resultado antes de aprovar o lote.'),('Desenho não cabe na volta do objeto','Confirmar área disponível e capacidade do acessório rotativo, em vez de usar apenas o diâmetro como critério. [rotary]')],
 'fontes':['laser','rotary'],'relacionados':['tampografia','impressao-uv','canetas-e-escrita','como-escolher-a-tecnica'],'ancoras':['materiais/index.html#metais','materiais/index.html#naturais'],'tags':'laser fibra co2 gravacao circular aluminio inox madeira'},
 {'id':'impressao-uv','sec':'tecnicas','tipo':'tecnica','titulo':'Impressão digital UV','resumo':'Impressão digital direta com tintas curadas por luz UV. Permite explorar imagens a cores em artigos cuja superfície e geometria sejam compatíveis.',
 'seccoes':[
 ('Como funciona','As cabeças depositam tinta para construir a imagem; a luz UV participa na cura. A configuração do equipamento determina as tintas e os efeitos disponíveis. [uv] [roland]'),
 ('Equipamentos','Existem impressoras de mesa e soluções para outras geometrias. A distância à cabeça de impressão e a fixação do objeto fazem parte da avaliação. [uv]'),
 ('Materiais e produtos','Blocos, tampas e artigos tecnológicos com áreas adequadas são possibilidades a avaliar. Não basta a superfície parecer plana: confirme o revestimento e a aderência. [uv] [primer]'),
 ('Cores e acabamentos','CMYK, branco e verniz existem em configurações específicas. A Roland descreve branco opaco e verniz para efeitos; não são funções obrigatórias de todas as máquinas. [roland]'),
 ('Preparação da arte','Entregue a imagem na dimensão pretendida e peça instruções para camadas de branco ou verniz, quando aplicáveis. Confirme a reprodução da cor numa prova.'),
 ('Condições a confirmar','A Roland recomenda ensaio mesmo quando é usado primário: o seu efeito varia com o material. Confirme também a área utilizável e o acabamento final. [primer]'),
 ('Limitações','A midocean não garante correspondência exata a Pantone na sua impressão digital. Geometrias curvas pedem uma configuração adequada, não a simples aplicação de condições de mesa plana. [uv]'),
 ('Comparar alternativas','Para cores diretas, consulte tampografia ou serigrafia. Para uma marca sem tinta, compare laser. Decida com base no desenho e numa amostra do artigo.')],
 'problemas':[('Aderência insuficiente','Pedir ensaio do conjunto superfície, tinta e primário. Um primário não garante compatibilidade universal. [primer]'),('Cor diferente da expectativa','Rever a referência aprovada e a prova no suporte; distinguir cor de ecrã e reprodução por CMYK. [uv]')],
 'fontes':['uv','roland','primer'],'relacionados':['tampografia','gravacao-a-laser','como-escolher-a-tecnica'],'ancoras':['materiais/index.html#plasticos','produtos/index.html#tecnologia'],'tags':'digital uv cmyk branco verniz fotografia degradês primer'},
 BORDADO,

]

from conteudos.industria import INDUSTRIA, FONTES_INDUSTRIA, AREAS_INDUSTRIA, GRUPOS_INDUSTRIA
ARTIGOS += INDUSTRIA + AREAS_INDUSTRIA
FONTES.update(FONTES_INDUSTRIA)
from conteudos.tampografia import INTRO, SECCOES as SECCOES_TAMPOGRAFIA
FONTES.update({
 'inkcups': ('Inkcups — Pad Printing 101', 'https://www.inkcups.com/pad-printing-guide/'),
 'padmanual': ('Inkcups — manual ICN-2200-PS, página 3: ligação à relojoaria suíça', 'https://tagless.inkcups.com/wp-content/uploads/2017/08/ICN-2200-PS-manual-2.pdf'),
 'padapresentacao': ('midocean — apresentação das técnicas de impressão (alternativa à página técnica)', 'https://public.midocean.com/NE_Marketing/PrintingPresentation.pdf')})
tampografia = next(a for a in ARTIGOS if a['id']=='tampografia')
tampografia.update(seccoes=SECCOES_TAMPOGRAFIA, introducao=INTRO, fontes=['inkcups','pad','padapresentacao','marabu','padmanual'])
from conteudos.serigrafia import INTRO as INTRO_SERIGRAFIA, SECCOES as SECCOES_SERIGRAFIA
FONTES['screen'] = ('midocean — Serigrafia', 'https://www.midocean.com/export/us/eur/content/printing-technique-screen-print')
FONTES['screenhelp'] = ('ScreenPrinting.com — Como imprimir t-shirts', 'https://help.screenprinting.com/en-US/how-to-screen-print-t-shirts-114141')
FONTES['marabuscreen'] = ('Marabu — Tintas e cura', 'https://www.marabu.com/printing-inks/service-support/knowledge-base/auxiliaries-for-uv-curable-screen-printing-inks')
serigrafia = next(a for a in ARTIGOS if a['id']=='serigrafia')
serigrafia.update(seccoes=SECCOES_SERIGRAFIA, introducao=INTRO_SERIGRAFIA, fontes=['screen','screenhelp','marabuscreen'])
serigrafia['relacionados'] += ['dtf-e-prensas-termicas','impressao-uv']
from conteudos.impressao_uv import INTRO as INTRO_UV, SECCOES as SECCOES_UV
FONTES['inkcupsuv'] = ('Inkcups — Impressão UV', 'https://www.inkcups.com/moving-from-pad-printing-to-uv-inkjet-printing/')
FONTES['rolanddireta'] = ('Roland DG — Impressão direta UV', 'https://www.rolanddg.com/products/printers/versaobject-io-300')
impressao_uv = next(a for a in ARTIGOS if a['id']=='impressao-uv')
impressao_uv.update(introducao=INTRO_UV, seccoes=SECCOES_UV, fontes=['inkcupsuv','rolanddireta'], problemas=[('Aderência insuficiente','Confirmar superfície, preparação, tinta e cura; pedir um ensaio antes de avançar com a produção.'),('Cor ou detalhe diferentes do esperado','Comparar com a prova aprovada, rever o ficheiro à escala final e avaliar o fundo e o acabamento do artigo.')])
impressao_uv['relacionados'].append('serigrafia')
from conteudos.guias import GUIAS, FONTES_GUIAS, GRUPOS_GUIAS, RESUMO_GUIAS
from copy import deepcopy
FONTES.update(FONTES_GUIAS)
ARTIGOS.extend(deepcopy(GUIAS))
sec_guias = next(s for s in SECCOES if s['id']=='guias')
sec_guias['titulo'] = 'Guias práticos'
sec_guias['resumo'] = RESUMO_GUIAS
sec_guias['grupos'] = [(id,t,d,'|'.join(a['titulo'] for a in ARTIGOS if a['sec']=='guias' and a.get('tema')==tema)) for id,t,d,tema in GRUPOS_GUIAS]
sec_industria = next(s for s in SECCOES if s['id']=='industria')
sec_industria['resumo'] = 'Equipamentos, operações e organização da produção, com guias sobre impressão, processos têxteis, corte, montagem e acabamento.'
sec_industria['grupos'] = [
 ('impressao-marcacao','Impressão e marcação','Equipamentos e operações para aplicar ou alterar uma imagem.','|'.join(next(a['titulo'] for a in INDUSTRIA + AREAS_INDUSTRIA if a['id']==id) for id in GRUPOS_INDUSTRIA[0][3])),
 ('processos-texteis','Processos têxteis','Bordado decorativo e costura estrutural, com funções distintas.','|'.join(next(a['titulo'] for a in INDUSTRIA + AREAS_INDUSTRIA if a['id']==id) for id in GRUPOS_INDUSTRIA[1][3])),
 ('corte-montagem-acabamento','Corte, montagem e acabamento','Preparação de formas, união de componentes e apresentação.','|'.join(next(a['titulo'] for a in INDUSTRIA + AREAS_INDUSTRIA if a['id']==id) for id in GRUPOS_INDUSTRIA[2][3]))]
for guia in INDUSTRIA:
    if guia.get("foto_tecnica"):
        next(a for a in ARTIGOS if a["id"] == guia["foto_tecnica"])["relacionados"].append(guia["id"])

from conteudos.materiais import MATERIAIS, FONTES_MATERIAIS
ARTIGOS.extend(MATERIAIS)
FONTES.update(FONTES_MATERIAIS)
sec_materiais = next(s for s in SECCOES if s['id'] == 'materiais')
sec_materiais['grupos'] = [(a['ancora'], a['titulo'], a['resumo'], a['titulo']) for a in MATERIAIS]
next(a for a in ARTIGOS if a['id'] == 'como-escolher-o-material')['relacionados'] += [a['id'] for a in MATERIAIS]

# Técnica e guia de equipamentos usam IDs distintos para preservar as ligações existentes.
from conteudos.sublimacao import SUBLIMACAO, FONTES_SUBLIMACAO
ARTIGOS.append(SUBLIMACAO)
FONTES.update(FONTES_SUBLIMACAO)
for artigo in ARTIGOS:
    if artigo['id'] in ('sublimacao', 'como-escolher-a-tecnica', 'serigrafia', 'impressao-uv', 'materiais-texteis', 'vidro-e-ceramica', 'garrafas-copos-e-canecas', 'texteis'):
        artigo['relacionados'].append(SUBLIMACAO['id'])

FONTES.update(FONTES_BORDADO)
ARTIGOS.append(TERMOGRAVURA)
FONTES.update(FONTES_TERMOGRAVURA)
from conteudos.transfers import TRANSFERS, FONTES_TRANSFERS
from conteudos.troquelagem import TROQUELAGEM, FONTES_TROQUELAGEM
from conteudos.crachas import CRACHAS, FONTES_CRACHAS
from conteudos.montagem import MONTAGEM, FONTES_MONTAGEM, HUB_ID
ARTIGOS.extend(MONTAGEM)
FONTES.update(FONTES_MONTAGEM)
for artigo in ARTIGOS:
    if artigo['id'] in ('costura-industrial', 'encadernacao-e-argolagem', 'montagem-e-acabamentos'):
        artigo['relacionados'].append(HUB_ID)
ARTIGOS.append(CRACHAS)
FONTES.update(FONTES_CRACHAS)
for artigo in ARTIGOS:
    if artigo['id'] == 'producao-de-crachas':
        artigo['relacionados'].append(CRACHAS['id'])
ARTIGOS.append(TROQUELAGEM)
FONTES.update(FONTES_TROQUELAGEM)
for artigo in ARTIGOS:
    if artigo['id'] in ('troquelagem', 'termogravura', 'papel-e-cartao'):
        artigo['relacionados'].append(TROQUELAGEM['id'])
ARTIGOS.extend(TRANSFERS)
FONTES.update(FONTES_TRANSFERS)
for artigo in ARTIGOS:
    if artigo['id'] in ('bordado', 'serigrafia', 'tecnica-sublimacao', 'materiais-texteis', 'texteis', 'sacos-e-mochilas', 'como-escolher-a-tecnica'):
        artigo['relacionados'].append('transfers')
    if artigo['id'] in ('dtf-e-prensas-termicas', 'serigrafia'):
        artigo['relacionados'].append('dtf')
for artigo in ARTIGOS:
    if artigo['id'] in ('gravacao-a-laser', 'impressao-uv', 'serigrafia', 'papel-e-cartao', 'pele-e-imitacao-de-pele', 'artigos-de-escritorio', 'como-escolher-a-tecnica', 'como-preparar-um-logotipo', 'como-avaliar-uma-maquete'):
        artigo['relacionados'].append('termogravura')
for artigo in ARTIGOS:
    if artigo["id"] in ("materiais-texteis", "texteis", "sacos-e-mochilas", "tecnica-sublimacao", "como-avaliar-uma-maquete") and "bordado" not in artigo["relacionados"]:
        artigo["relacionados"].append("bordado")

# Produtos deriva da fonte sem?ntica; as ?ncoras antigas mant?m-se.
sec_produtos = next(s for s in SECCOES if s['id'] == 'produtos')
sec_produtos['resumo'] = 'Compreenda e compare famílias de brindes pela utilização, construção e personalização.'
sec_produtos['grupos'] = [(g['ancora'], g['titulo'], g['resumo'], g['titulo']) for g in PRODUTOS]

from conteudos.mercado import MERCADO, AREAS as TEMAS_MERCADO
ARTIGOS.extend(MERCADO)
sec_mercado = next(s for s in SECCOES if s['id'] == 'mercado')
sec_mercado['resumo'] = 'Seis áreas editoriais para conhecer empresas de papelaria, tecnologia, casa, têxtil, sazonalidade e informação ambiental de brindes.'
sec_mercado['grupos'] = [(a['id'], a['titulo'], a['resumo'], a['titulo']) for a in TEMAS_MERCADO]
