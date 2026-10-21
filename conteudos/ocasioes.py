"""Ocasiões e Sazonalidade: contextos documentados e orientação editorial."""
DATA = '2026-10-21'

def fonte(titulo, entidade, url, ambito):
    return dict(titulo=titulo, entidade=entidade, url=url, ambito=ambito, data_consulta=DATA)

FONTES_OCASIOES = {
 'tudor': fonte('Celebrações e presentes na corte Tudor', 'Historic Royal Palaces',
    'https://www.hrp.org.uk/blog/christmas-in-the-tudor-court/',
    'Corte inglesa no século XVI; não é uma origem universal dos presentes.'),
 'vitoriano': fonte('Tradições natalícias vitorianas', 'Victoria and Albert Museum',
    'https://www.vam.ac.uk/articles/victorian-christmas-traditions',
    'Transformações no Natal britânico do século XIX, sem extrapolação para Portugal.'),
 'clima': fonte('Normais climatológicas', 'IPMA',
    'https://www.ipma.pt/pt/oclima/normais.clima/',
    'Médias climatológicas por estação de observação; não são previsão para um evento.'),
 'torres': fonte('O Carnaval Torriense: as origens de uma tradição antiga', 'Câmara Municipal de Torres Vedras',
    'https://cm-tvedras.pt/artigos/detalhes/carnaval-torriense-as-origens-de-uma-tradicao-antiga',
    'História local de Torres Vedras; não descreve todos os carnavais portugueses.'),
 'podence': fonte('Festa de Carnaval dos Caretos de Podence', 'MatrizPCI — Inventário Nacional do Património Cultural Imaterial',
    'https://matrizpci.patrimoniocultural.gov.pt/InventarioNacional/DetalheFicha/461',
    'Manifestação da comunidade de Podence, incluindo formas locais de participação.'),
 'calor': fonte('Recomendações à população sobre calor', 'Direção-Geral da Saúde',
    'https://www.dgs.pt/em-destaque/recomendacoes-a-populacao-calor.aspx',
    'Orientação de saúde pública; não comprova a proteção de qualquer artigo.'),
 'circular': fonte('Economia circular', 'Agência Europeia do Ambiente',
    'https://www.eea.europa.eu/en/topics/in-depth/circular-economy',
    'Enquadramento geral de utilização prolongada de produtos e materiais.'),
}

def secao(id, titulo, *paragrafos):
    return dict(id=id, titulo=titulo, paragrafos=list(paragrafos))

def foto(url, alt, width, height, legenda):
    return dict(url=url, alt=alt, width=width, height=height, legenda=legenda)

def artigo(id, titulo, resumo, imagem, conteudo, faq, fontes, relacionados, tags):
    return dict(id=id, sec='ocasioes', tipo='ocasiao', titulo=titulo, resumo=resumo,
        imagem=imagem, conteudo=conteudo, perguntas_frequentes=faq, fontes=fontes,
        relacionados=relacionados, tags=tags, data_revisao=DATA, problemas=[], ancoras=[],
        seccoes=[(s['titulo'], ' '.join(s['paragrafos'])) for s in conteudo] +
                [('Perguntas frequentes', ' '.join(p + ' ' + r for p, r in faq))])

OCASIOES = [
 artigo('natal','Natal',
  'Prepare agradecimentos e encontros de fim de ano, relacionando destinatário, utilidade, mensagem e apresentação, sem presumir uma celebração igual para todos.',
  foto('assets/produtos/visuais/casa-cartao.jpg','Manta clara enrolada com uma figura de peluche castanha com hastes.',700,700,
       'Objeto de apresentação com motivo figurativo. A imagem não comprova composição, cuidados ou adequação infantil.'),
  [secao('contexto','Natal e encontros de fim de ano',
    'Uma oferta pode integrar um agradecimento, um encontro de equipa, uma atividade de associação ou uma entrega de fim de ano. Comece pelo gesto pretendido: agradecer uma colaboração não exige o mesmo artigo que apoiar uma oficina ou acolher participantes.',
    'Confirme se a referência ao Natal faz sentido para quem recebe. Uma mensagem de agradecimento ou de fim de ano pode permitir uma participação mais inclusiva, sem reduzir todas as pessoas a uma tradição religiosa ou familiar.'),
   secao('historia','Presentes: histórias diferentes, sem origem única',
    'A troca de presentes não começou na época vitoriana. Historic Royal Palaces documenta ofertas de Ano Novo na corte inglesa de Henrique VIII, no século XVI. Trata-se de um contexto de corte, anterior ao século XIX, não de uma descrição de todas as famílias ou países. [tudor]',
    'O V&A descreve a crescente centralidade do Natal na Grã-Bretanha vitoriana e a deslocação de práticas de oferta ligadas ao Ano Novo para a celebração natalícia. A mudança britânica não estabelece uma origem universal nem explica, por si só, as práticas portuguesas. [vitoriano]',
    'As tradições pessoais e familiares e o uso contemporâneo de artigos em ações de comunicação são planos diferentes. As fontes históricas consultadas não demonstram a data de início de brindes promocionais de Natal em Portugal.'),
   secao('destinatarios','Quem oferece, quem recebe e com que objetivo',
    'Equipas podem agradecer a trabalhadores, colaboradores ou clientes; escolas e associações podem preparar encontros para famílias e participantes; municípios podem apoiar iniciativas comunitárias. A escolha deve partir da relação concreta e do modo como a pessoa receberá o objeto.',
    'Diferencie uma entrega individual de uma mesa de materiais numa atividade aberta. Num agradecimento, a mensagem pessoal pode ter mais significado que acrescentar peças a um conjunto. Num encontro, a prioridade pode ser facilitar a participação, sem oferta para levar.'),
   secao('artigos','Exemplos ligados à ocasião',
    'Caderno e instrumento de escrita: podem acompanhar uma mensagem de continuidade para o ano seguinte, quando a pessoa usa apontamentos. Uma agenda datada exige confirmar o período e a rotina; não é equivalente a um caderno sem datas.',
    'Caneca ou outro recipiente: pode fazer sentido numa pausa ou contexto doméstico, avaliando pega, limpeza e instruções. A apresentação natalícia não demonstra aptidão para bebidas quentes ou conservação térmica.',
    'Manta, pequeno objeto para casa ou conjunto de uso pessoal: considere o espaço que ocupa e o que a pessoa terá de transportar. Uma caixa e um cartão podem reunir peças complementares; não é preciso aumentar o conjunto para tornar o agradecimento claro.'),
   secao('escolha','Escolher pelo uso e pela forma de entrega',
    'Confirme destinatários, variantes e necessidades de acessibilidade. Num grupo, podem existir preferências culturais e formas de utilização diferentes; permita recusar a oferta sem prejudicar a participação.',
    'Observe o objeto e a apresentação juntos. Teste abertura, leitura da mensagem, espaço interior e transporte até casa. Separe entrega em mão de envio: uma caixa de apresentação não demonstra proteção durante expedição.'),
   secao('planeamento','Planear mensagem, preparação e distribuição',
    'Defina primeiro a ocasião de entrega e confirme, para esse projeto, tempos de aprovação, personalização, montagem e transporte. Não há um prazo universal de produção aplicável a todos os artigos.',
    'Reveja nomes, idiomas, data e lista de destinatários antes da aprovação. Se houver vários locais ou turnos, prepare identificação dos conjuntos e responsáveis pela entrega. Decida antecipadamente o destino de artigos não levantados.'),
   secao('impactos','Agradecimento, inclusão e responsabilidade',
    'O objetivo de agradecer não prova fidelização, notoriedade ou vendas. Pode recolher apreciações voluntárias sobre utilidade e apresentação, sem tratar a entrega como evidência de um resultado promocional.',
    'A Agência Europeia do Ambiente enquadra a utilização prolongada de produtos e materiais na economia circular. [circular] Para esta oferta, avalie necessidade, embalagem, cuidados e uso posterior; um motivo festivo ou material não comprova menor impacto ambiental.'),
   secao('personalizacao','Mensagem e personalização',
    'Escolha uma mensagem legível à dimensão real e confirme se deve aparecer no objeto ou apenas no cartão. Uma apresentação que se retira depois da entrega pode permitir que o artigo continue a ser usado noutros contextos.',
    'Identifique material, acabamento e zona antes de escolher a técnica. Em conjuntos, cada componente pode exigir uma avaliação diferente; a compatibilidade não se transfere automaticamente do artigo para a embalagem.')],
  [('Oferecer no Natal exige uma mensagem religiosa?','Não. Confirme o contexto e os destinatários; um agradecimento de fim de ano pode corresponder melhor à iniciativa.'),
   ('Uma oferta de fim de ano tem de ser um conjunto?','Não. Um artigo útil, uma mensagem ou uma atividade sem objeto podem cumprir o propósito escolhido.'),
   ('A prática de oferecer presentes nasceu no século XIX?','Não. As fontes aqui usadas documentam contextos britânicos anteriores e transformações vitorianas, sem uma origem universal.')],
  ['tudor','vitoriano','circular'],
  ['embalagem-e-apresentacao','casa-decoracao-e-cuidados-pessoais','artigos-de-escritorio','empresas','associacoes-organizacoes-comunitarias','como-avaliar-uma-maquete','montagem-embalagem-expedicao'],
  'Natal fim de ano agradecimento presentes apresentação embalagem encontros'),

 artigo('inverno','Inverno',
  'Pense nas deslocações, no frio, na chuva e no contraste entre espaços interiores e exteriores. A estação orienta perguntas, sem garantir propriedades dos artigos.',
  foto('assets/produtos/visuais/bebidas-cartao.jpg','Três canecas brancas com pegas e interiores azul, vermelho e preto.',300,301,
       'Recipientes para contextos de pausa. A imagem não comprova limites de temperatura ou conservação térmica.'),
  [secao('contexto','Uma estação, várias condições de utilização',
    'Uma receção em espaço aquecido, uma deslocação diária e um evento no exterior colocam perguntas diferentes. Identifique onde o artigo será usado e se a pessoa terá de o transportar, guardar molhado ou utilizar com outras peças de roupa.',
    'O IPMA disponibiliza normais climatológicas de temperatura e precipitação por locais de observação. São uma referência de clima, não uma previsão para a data da atividade. Consulte também a informação meteorológica pertinente ao planeamento. [clima]'),
   secao('historia','Contexto climático sem uma tradição inventada',
    'As fontes selecionadas para este guia não estabelecem uma tradição geral de oferecer brindes no Inverno. O foco é a preparação de atividades e deslocações, e não uma suposta origem histórica da oferta sazonal.',
    'Uma campanha de acolhimento, uma formação ou um encontro comunitário podem decorrer nesta estação sem partilharem a mesma história ou finalidade. Quando uma iniciativa invoca um costume local, deve identificar a comunidade e a fonte que o documenta.'),
   secao('destinatarios','Quem organiza e quem utiliza',
    'Organizações, escolas, associações e municípios podem preparar materiais para equipas, visitantes ou participantes. Distinga quem permanece no interior, quem entra e sai e quem trabalha num espaço exterior.',
    'Os objetivos podem ser acolher, organizar o transporte de materiais ou identificar uma equipa. A decisão de oferecer um objeto deve acompanhar esses objetivos; não substitui a organização do local nem os equipamentos necessários à atividade.'),
   secao('artigos','Artigos para situações concretas',
    'Canecas e recipientes com tampa: para pausas ou deslocações, avalie o local de consumo, a abertura e a limpeza. A tampa pode servir apenas para beber e não tornar o recipiente estanque dentro de um saco.',
    'Peças têxteis e acessórios: num encontro ou uso diário, o corte e as medidas devem permitir o movimento previsto com outras camadas. A aparência espessa não comprova proteção contra frio, chuva ou vento.',
    'Sacos e bolsas: podem organizar documentos e equipamento no percurso. Confirme acessos e dimensões úteis; a construção visual ou um revestimento não provam impermeabilidade do conjunto.',
    'Cadernos e materiais de reunião: em atividades interiores, podem ser mais pertinentes que um artigo associado ao frio. A estação não obriga a que todas as escolhas tenham uma função climática.'),
   secao('escolha','Avaliar utilização, conforto e limites',
    'Observe como se abre, segura e guarda o objeto nas condições previstas. Numa peça vestível, ensaie posição da mensagem e ajuste; num saco, verifique fechos e o espaço para o conteúdo habitual.',
    'Se for necessária proteção profissional ou um desempenho perante intempéries, procure a documentação aplicável ao artigo. Não apresente vestuário promocional como equipamento de proteção apenas por ser usado no exterior.'),
   secao('planeamento','Planear alternativas para o local e a entrega',
    'Defina um ponto de entrega adequado ao percurso e uma alternativa se a atividade mudar de espaço. Confirme armazenamento, acesso ao recinto e distribuição por turnos, evitando que a recolha de um artigo dificulte a circulação.',
    'Aprove variantes e medidas antes de confirmar a personalização. Valide prazos de cada etapa e do transporte para o projeto concreto; o calendário deve comportar as aprovações necessárias, sem prometer um tempo fixo de produção.'),
   secao('impactos','Utilidade depois da estação',
    'Pergunte se o objeto continuará a ser usado quando a atividade terminar. A utilização prolongada integra o enquadramento de circularidade da Agência Europeia do Ambiente. [circular] Isso não demonstra uma vantagem ambiental do artigo escolhido.',
    'Analise embalagem, possibilidade de limpeza, armazenamento e destino final. Não confunda a intenção de apoiar participantes com proteção efetivamente prestada ou com satisfação demonstrada; recolha informação sobre uso e dificuldades se quiser avaliar a iniciativa.'),
   secao('personalizacao','Personalizar sem comprometer utilização',
    'Observe a mensagem com a peça vestida ou com o recipiente na posição de consumo. Punhos, costuras, pegas e fechos podem reduzir a área visível ou acessível.',
    'Confirme a técnica no material e acabamento concretos, incluindo o cuidado posterior. Não cubra instruções, marcações ou zonas funcionais para aumentar a área do desenho.')],
  [('Um saco revestido é impermeável?','Não se conclui isso do revestimento. Fechos, costuras e condições de utilização do artigo completo precisam de documentação.'),
   ('Uma caneca é obrigatória numa oferta de Inverno?','Não. Escolha pela rotina e pelo local de utilização; um material de reunião pode ser mais útil.'),
   ('As médias de clima permitem garantir o tempo no dia do evento?','Não. Normais climatológicas e previsão para uma data têm funções diferentes. [clima]')],
  ['clima','circular'],
  ['garrafas-copos-e-canecas','texteis','sacos-e-mochilas','mobilidade-ferramentas-e-seguranca','eventos','como-escolher-o-material','materiais-texteis'],
  'Inverno frio chuva deslocações interiores exterior camadas roupa transporte'),

 artigo('carnaval','Carnaval',
  'Relacione tradições locais, desfiles e participação com identificação, materiais de apoio e recordações, distinguindo-os de máscaras, fantasias e equipamentos.',
  foto('assets/para_quem/visuais/contexto-identificacao.jpg','Pulseiras de várias cores com um fecho escuro, com uma pulseira azul em primeiro plano.',300,300,
       'Exemplo de identificação de participantes; não é uma fotografia de uma tradição carnavalesca nem prova controlo de acesso.'),
  [secao('contexto','Organização e participação em celebrações locais',
    'Desfiles, festas de associação, atividades escolares e encontros comunitários podem reunir participantes, equipas e público visitante com necessidades diferentes. Comece pelo programa e pelo papel de cada pessoa.',
    'O Carnaval não é apresentado aqui como uma ocasião universal de troca de presentes. Um artigo pode apoiar a identificação, reunir materiais de uma oficina ou recordar uma participação, mas pode também ser desnecessário.'),
   secao('historia','Carnavais portugueses: exemplos com território',
    'A história municipal de Torres Vedras distingue a festa de rua organizada em 1912 da organização continuada a partir de 1923. Esta cronologia descreve o caso torriense, não uma data de nascimento de todos os carnavais. [torres]',
    'O Inventário Nacional de Património Cultural Imaterial situa a Festa de Carnaval dos Caretos de Podence na comunidade desta aldeia de Macedo de Cavaleiros, no ciclo festivo de Inverno. Documenta também a participação comunitária e atividades paralelas. [podence]',
    'Estes exemplos mostram por que é necessário confirmar tradições, linguagem e imagem com a organização local. O facto de uma celebração ter história documentada não prova uma tradição de distribuição de brindes nem autoriza a usar qualquer símbolo fora do seu contexto.'),
   secao('destinatarios','Papéis diferentes dentro do evento',
    'Associações e grupos podem preparar materiais para quem desfila; escolas podem organizar oficinas e saídas; municípios e organizadores podem apoiar equipas de acolhimento e participantes. Os visitantes não precisam necessariamente do mesmo conjunto.',
    'Defina se pretende identificar uma função, facilitar uma atividade ou criar uma memória. Não prometa que um objeto aumenta participação ou preserva uma tradição: esses resultados exigem observação e evidência próprias.'),
   secao('artigos','Exemplos pela função que cumprem',
    'Fitas, cartões e pulseiras: podem diferenciar grupos ou apoiar a receção. A cor e a impressão devem ser legíveis, mas o objeto não garante autenticidade ou controlo de acesso sem um processo definido.',
    'Têxteis para equipas: uma mensagem comum pode ajudar a reconhecer quem presta apoio. Considere a peça vestida com outras camadas e o movimento durante o percurso, em vez de avaliar apenas a peça pousada.',
    'Sacos e cadernos de atividade: podem reunir materiais ou guardar registos numa oficina. Para uma recordação, uma peça gráfica pode relacionar-se com a edição e com a comunidade, desde que a imagem e o texto sejam revistos localmente.'),
   secao('escolha','Separar comunicação, disfarce e proteção',
    'Um artigo promocional não equivale a uma máscara, fantasia ou equipamento de proteção. Visibilidade, ajuste, materiais e condições de utilização devem ser avaliados no objeto concreto; a mensagem festiva não demonstra adequação.',
    'Quando participam crianças, confirme idades, avisos, acompanhamento e o modo de entregar cada peça ao adulto responsável. A distribuição indiferenciada pode ignorar as diferenças entre o público de uma oficina e o de um desfile.'),
   secao('planeamento','Programa, edição e distribuição',
    'Confirme o calendário e o percurso da edição em causa com a organização. Este guia não fixa datas anuais nem substitui o programa local.',
    'Reveja nomes dos grupos, idiomas, cores de identificação e forma de entrega. Ensaie a receção com os materiais colocados como serão usados. Confirme tempos de aprovação e preparação para cada projeto e preveja alterações de percurso ou local.'),
   secao('impactos','Respeito cultural e destino dos materiais',
    'Evite reduzir uma tradição local a uma imagem genérica de festa. Ouça a organização e permita formas de participação sem receber ou vestir um artigo.',
    'O enquadramento da economia circular valoriza usar produtos e materiais durante mais tempo. [circular] Decida que partes podem voltar a ser utilizadas noutra edição e quais necessitam de atualização. Uma mensagem datada pode limitar esse uso, mas não há um resultado ambiental quantificado sem avaliação.',
    'Separe objetivos promocionais da participação observada. Contar peças distribuídas não explica quem as utilizou nem qual foi o significado cultural da iniciativa.'),
   secao('personalizacao','Personalizar para leitura em movimento',
    'Use hierarquia simples: função da equipa ou grupo primeiro, informação complementar depois. Teste a leitura à distância prevista e com o artigo na posição real de utilização.',
    'A técnica deve ser avaliada no suporte e no acabamento concretos. Em peças vestíveis, preserve zonas funcionais e avisos; no cartão, não cubra furos, fechos ou informação necessária.')],
  [('Todos os carnavais portugueses têm as mesmas tradições?','Não. Os exemplos de Torres Vedras e Podence têm contextos próprios; confirme a tradição e a programação locais.'),
   ('Uma pulseira garante acesso ao desfile ou recinto?','Não. Só pode ter esse papel dentro do processo definido pela organização, sem garantia automática pela cor ou pela impressão.'),
   ('É necessário distribuir uma recordação?','Não. Materiais partilhados numa atividade, informação ou participação sem oferta podem corresponder melhor ao objetivo.')],
  ['torres','podence','circular'],
  ['eventos-identificacao-e-premios','texteis','sacos-e-mochilas','criancas','associacoes-organizacoes-comunitarias','camaras-municipais','serigrafia'],
  'Carnaval Entrudo Podence Torres Vedras desfiles máscaras grupos participação pulseiras'),

 artigo('verao','Verão',
  'Prepare artigos para turismo, viagens, praia, festivais e atividades ao ar livre, pensando no percurso completo e nas condições documentadas de utilização.',
  foto('assets/produtos/visuais/texteis-bones.jpg','Quatro bonés nas cores branca, preta, azul-escura e verde-escura.',300,300,
       'Exemplos de acessórios de vestuário. A fotografia não demonstra proteção solar ou desempenho perante calor e água.'),
  [secao('contexto','Atividades e percursos de utilização',
    'Uma visita turística, uma sessão desportiva, um festival e um dia de praia têm transportes, permanências e locais de entrega diferentes. Escolha pelo percurso: levar, utilizar, limpar e voltar a guardar.',
    'Não se estabelece neste guia uma tradição histórica comum de oferecer brindes de Verão. Turismo, lazer e campanhas sazonais têm contextos próprios; não foi encontrada, nas fontes selecionadas, uma origem única que justifique essa afirmação.'),
   secao('destinatarios','Quem prepara a ação e quem recebe',
    'Equipas de alojamento podem acolher hóspedes; associações e municípios podem apoiar atividades; clubes e organizadores podem preparar materiais para participantes e voluntários. Distinga quem chega de viagem de quem permanece no recinto.',
    'Acolher, informar e identificar são objetivos diferentes. Um material de orientação pode ser mais pertinente na chegada; uma recordação pode ser avaliada no final, quando a pessoa já conhece o peso e o espaço de que dispõe.'),
   secao('artigos','Exemplos de artigos e razões de escolha',
    'Garrafas e recipientes: podem acompanhar uma rotina de bebida quando há condições para os encher e limpar. Observe abertura, transporte e utilização indicada. A capacidade, a tampa ou a aparência não comprovam estanquidade ou conservação térmica.',
    'Sacos e bolsas: podem reunir objetos num passeio ou organizar equipamento numa viagem. Escolha pela dimensão do conteúdo e pelo acesso; não deduza proteção contra água, areia ou quedas pelo nome da bolsa.',
    'Bonés, t-shirts e toalhas: podem apoiar identificação de equipa ou uma atividade de lazer. Avalie ajuste, medidas e cuidados; a utilização ao sol não demonstra proteção solar.',
    'Jogos e acessórios de exterior: relacione-os com espaço, tempo de preparação e possibilidade de guardar depois da atividade. Uma cadeira ou saco volumoso pode ser inadequado para quem se desloca a pé ou tem bagagem limitada.'),
   secao('escolha','Calor, sol, água e alimentação',
    'As recomendações da DGS para o calor incluem informação sobre hidratação e exposição solar. [calor] A organização deve consultar a orientação atual para a atividade; distribuir um artigo não equivale a assegurar proteção ou condições de saúde.',
    'Confirme instruções de exposição, limpeza e armazenamento do artigo concreto. Num recipiente de refeição ou bebida, o contacto alimentar e a temperatura permitida não se deduzem do material aparente. Se o uso exigir proteção solar ou resistência à água, procure documentação específica.'),
   secao('planeamento','Entregar no momento em que faz sentido',
    'Mapeie pontos de chegada, atividade e saída. Um objeto entregue cedo pode acompanhar a atividade, mas também aumentar o que a pessoa transporta; uma entrega final pode ser mais simples se não for necessário durante o programa.',
    'Confirme acesso ao recinto, armazenamento e entrega por grupos ou turnos. Valide, por projeto, aprovação da arte, preparação, montagem e transporte. Não presuma um prazo universal nem um calendário turístico igual em todos os destinos.'),
   secao('impactos','Utilidade, participação e responsabilidade',
    'A reutilização e a utilização prolongada integram o enquadramento de economia circular. [circular] Verifique se há condições reais de limpeza, transporte e uso posterior, em vez de tratar a palavra reutilizável como prova de menor impacto.',
    'Considere embalagem, recolha de sobras e destino no fim de vida. Permita participar sem receber um artigo e reveja idiomas e acessibilidade da mensagem para visitantes.',
    'Se avaliar a ação, distinga quantidade entregue de utilização observada. Registe como recolheu opiniões e a quem perguntou; esses dados não demonstram automaticamente efeitos em vendas ou fidelização.'),
   secao('personalizacao','Mensagem que acompanha o uso',
    'Num saco ou boné, observe a posição do desenho com o objeto utilizado. Numa garrafa, avalie a área exterior e a leitura ao segurar, preservando zonas de contacto e informação técnica.',
    'Confirme a técnica, o acabamento e os cuidados do conjunto personalizado. O comportamento documentado do objeto sem personalização não permite concluir o comportamento de qualquer aplicação.')],
  [('Um boné promocional garante proteção solar?','Não. A imagem ou a utilização em atividades de Verão não comprovam esse desempenho.'),
   ('Uma garrafa resolve o planeamento de hidratação de um evento?','Não. A disponibilidade de bebida, o local e a atividade exigem organização própria e consulta das orientações pertinentes.'),
   ('Um artigo reutilizável tem sempre menor impacto?','Não se estabelece uma conclusão sem âmbito e avaliação. Considere produção, transporte, uso, cuidados e destino final do artigo concreto.')],
  ['calor','circular'],
  ['desporto-lazer-e-exterior','garrafas-copos-e-canecas','sacos-e-mochilas','texteis','turismo-alojamento','clubes-desportivos','como-escolher-brindes-para-um-evento'],
  'Verão turismo praia viagens festivais calor sol água transporte atividades exterior'),
]

IMAGENS_CARTOES = {
 'natal': foto('assets/ocasioes/Natal/brindesparaonatal_cabazdenatal.jpg',
    'Dois cabazes com alimentos embalados, laços e figuras decorativas natalícias.',700,325,
    'Imagem ilustrativa de apresentação natalícia.'),
 'inverno': foto('assets/ocasioes/Inverno/ChatGPT-Image-18-de-fev.-de-2026-15_33_35.jpg',
    'Gorro, luvas, manta, chinelos, caderno, calendário, recipientes e saco sobre uma superfície clara.',1536,1024,
    'Composição ilustrativa de artigos num contexto de Inverno.'),
 'carnaval': foto('assets/ocasioes/Carnaval/-1576168.jpg',
    'Copos e fitas com padrões coloridos e mensagens de Carnaval.',1080,1080,
    'Exemplos visuais de artigos com motivos de Carnaval, sem representar uma tradição local portuguesa.'),
 'verao': foto('assets/ocasioes/Verao/images.jpg',
    'Chapéu, toalha azul, óculos escuros e copo de água sobre madeira junto ao mar.',738,387,
    'Composição de praia; não comprova proteção solar dos acessórios.'),
}
for a in OCASIOES:
    a['imagem_cartao'] = IMAGENS_CARTOES[a['id']]

from conteudos.ocasioes_exemplos import integrar
integrar(OCASIOES, FONTES_OCASIOES, fonte)

SECCAO_OCASIOES = dict(id='ocasioes', titulo='Ocasiões e Sazonalidade', curto='Ocasiões',
    icone='◷', resumo='Relacione épocas e celebrações com utilização, mensagem, planeamento e distribuição de artigos.',
    grupos=[(a['id'], a['titulo'], a['resumo'], a['titulo']) for a in OCASIOES])

CREDITOS = ('<section id="ocasioes-ilustrativas"><h2>Imagens de Ocasiões e Sazonalidade</h2>'
 '<p>Os cartões usam as quatro imagens locais de assets/ocasioes: cabazes natalícios, '
 'uma composição de artigos de Inverno, copos e fitas de Carnaval e acessórios junto '
 'ao mar. São ilustrações temáticas, sem comprovar características dos artigos '
 'ou representar todas as tradições locais.</p>'
 '<p>Os exemplos comentados nos guias usam também imagens locais de ornamentos, '
 'adereços, gorro, manta, meias, máscara, pintura, capa, chinelos, almofadas, discos '
 'e conjuntos de praia. Foram preparadas cópias integrais sob nomes neutros, sem '
 'alterar os originais.</p>'
 '<p>Nos corpos dos guias são reutilizadas fotografias locais de uma manta com figura de peluche, canecas, '
 'pulseiras e bonés, já usadas na biblioteca. Ilustram possibilidades de utilização, '
 'não celebrações históricas nem propriedades técnicas. Os originais foram preservados.</p>'
 '<p>Autoria individual e licença de terceiros não identificadas nos registos disponíveis. '
 'Não se atribui uma licença aberta. As imagens não comprovam proteção, composição '
 'ou adequação universal a uma época.</p></section>')
