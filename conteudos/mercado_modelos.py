"""Modelos de atividade: classificação editorial apoiada em funções documentadas."""
DATA_MODELOS='2026-10-22'
IMAGENS_CARTOES={
 'distribuicao-e-importacao':('images.jpg',623,357,'Ilustração de espaços de exposição com artigos promocionais.'),
 'fabricantes-e-produtores':('16fba9a6-12a1-4da5-8bb9-5289a80ff6f3.jpg',1024,1024,'Ilustração de uma oficina com equipamentos e pessoas a trabalhar em artigos promocionais.'),
 'personalizacao-impressao-acabamento':('altronix-producao-3-3-1024x698.webp',1024,698,'Equipamentos de impressão e pessoas a trabalhar numa área de produção.'),
 'empresas-de-atividade-mista':('images.jpg',426,320,'Espaço de trabalho com bancadas, caixas e zonas de circulação.'),
}
FONTES_MODELOS={
 'modelo_velilla':('Velilla Group — apresentação institucional','https://es.linkedin.com/company/velilla-group'),
 'modelo_pf':('PF Concept — About PF Concept, incluindo PF Manufactured','https://www.pfconcept.com/ru_ru/about-pf'),
}
ROTULOS={'distribuicao':'Distribuição e armazenamento','fabrico':'Fabrico de artigos','personalizacao':'Impressão e personalização'}
ROTULOS['mista']='Atividade mista'

def empresa(principal, especialidades, texto, limite, funcoes, **extra):
    return dict(principal=principal,especialidades=especialidades,texto=texto,limite=limite,funcoes=funcoes,**extra)

CLASSIFICACOES={
 'stricker':empresa('distribuicao','Desenvolvimento de brindes, impressão e logística',
   'Desenvolve e distribui produtos promocionais a profissionais, com uma oferta de impressão e logística.',
   'A personalização documentada não identifica quem fabrica cada objeto de base.',
   {'distribuicao':['stricker'],'personalizacao':['stricker']},desenvolvimento=True),
 'tejobrinde':empresa('distribuicao','Brindes, stock e gravações',
   'Publica fornecimento com stock em Lisboa e disponibilidade de serviços de gravação.',
   'A disponibilização do serviço não esclarece a repartição entre execução interna e contratação externa.',
   {'distribuicao':['tejo_servicos'],'personalizacao':['tejo_servicos']}),
 'th-clothes':empresa('distribuicao','Vestuário promocional e desenvolvimento têxtil',
   'A marca da Organizações Biscana desenvolve uma oferta de vestuário e organiza o seu fornecimento.',
   'Desenvolvimento de produto e titularidade da marca não confirmam confeção própria.',
   {'distribuicao':['th']},desenvolvimento=True),
 'roly':empresa('distribuicao','Vestuário casual, profissional e desportivo',
   'A Gor Factory apresenta venda e distribuição de vestuário e artigos promocionais através das suas marcas.',
   'Não se atribui fabrico espanhol nem impressão interna a todas as peças.',
   {'distribuicao':['gor_empresa']},desenvolvimento=True),
 'dimatur':empresa('distribuicao','Materiais, consumíveis, equipamentos e assistência',
   'Fornece materiais e tecnologia a profissionais de comunicação visual e transformação.',
   'Fornecer os meios de produção não equivale a fabricar ou personalizar o brinde acabado.',
   {'distribuicao':['dimatur']}),
 'eurovinil':empresa('distribuicao','Serigrafia, impressão digital e apoio técnico',
   'Documenta venda e distribuição de consumíveis e equipamentos para publicidade e comunicação visual.',
   'As máquinas e os materiais fornecidos são utilizados por outros profissionais; não provam fabrico próprio.',
   {'distribuicao':['eurovinil']}),
 'solo-midocean':empresa('distribuicao','Artigos promocionais, impressão e preparação',
   'Combina fornecimento com instalações próprias de logística e impressão na Polónia.',
   'Essas instalações não demonstram fabrico polaco de todos os objetos fornecidos.',
   {'distribuicao':['solo_locais'],'personalizacao':['solo_locais']}),
 'bic-graphic':empresa('fabrico','Instrumentos de escrita e decoração promocional',
   'A oferta identifica instrumentos de escrita fabricados e impressos em fábricas BIC.',
   'A indicação é específica dos artigos assinalados; não atribui o mesmo fabrico a toda a divisão ou oferta.',
   {'fabrico':['bic_areas'],'personalizacao':['bic_tecnicas','bic_areas']}),
 'tela':empresa('personalizacao','Impressão, gravação, têxtil e comunicação visual',
   'Publica várias técnicas de personalização e uma operação de impressão promocional em Sintra.',
   'A produção gráfica declarada não confirma o fabrico de todos os artigos de base.',
   {'distribuicao':['tela_empresa'],'personalizacao':['tela_empresa']}),
 'giving-europe':empresa('distribuicao','Grossista de brindes, impressão e logística',
   'Apresenta fornecimento promocional articulado com impressão e centro logístico na Polónia.',
   'Armazenar e imprimir não são sinónimos de fabricar o artigo.',
   {'distribuicao':['giving_empresa'],'personalizacao':['giving_empresa']}),
 'goya':empresa('distribuicao','Importação, marcação e preparação de pedidos',
   'Fornece distribuidores e profissionais, publicando importação, distribuição e técnicas de personalização.',
   'A origem do artigo e a entidade que executa cada operação dependem do pedido.',
   {'distribuicao':['goya_empresa'],'personalizacao':['goya_empresa']}),
 'plural':empresa('personalizacao','Brindes personalizados, impressão e acabamentos',
   'Publica fornecimento de brindes personalizados e técnicas de impressão e acabamento.',
   'A divisão entre operações internas e subcontratação não está discriminada por artigo.',
   {'distribuicao':['plural_empresa'],'personalizacao':['plural_empresa']}),
 'xd-connects':empresa('distribuicao','Desenho, aprovisionamento e soluções promocionais',
   'O perfil documentado reúne desenvolvimento, fornecimento e personalização numa cadeia internacional.',
   'A página institucional depende de JavaScript; a execução de cada etapa e o fabricante devem ser confirmados por artigo.',
   {'distribuicao':['xd_empresa'],'personalizacao':['xd_operacao']},desenvolvimento=True,consulta='2026-10-14'),
 'aodaci':empresa('distribuicao','Desenvolvimento, armazenagem e personalização',
   'Apresenta atividade grossista de produtos promocionais com opções de personalização.',
   'A descrição não demonstra fabrico integral próprio. A localização não é usada para inferir origem dos produtos.',
   {'distribuicao':['aodaci_atividade'],'personalizacao':['aodaci_atividade']},desenvolvimento=True),
 'pf-concept':empresa('distribuicao','Fornecimento profissional, impressão e linhas fabricadas',
   'Publica distribuição, uma unidade de impressão na Polónia e fabrico PF Manufactured no Reino Unido.',
   'O fabrico refere-se à operação identificada, não a todos os produtos nem à produção dos componentes.',
   {'distribuicao':['modelo_pf'],'personalizacao':['modelo_pf'],'fabrico':['modelo_pf']}),
 'velilla-group':empresa('fabrico','Vestuário profissional e têxtil promocional MUKUA',
   'O grupo declara desenho, fabrico e distribuição de vestuário, incluindo a marca MUKUA.',
   'A declaração institucional não confirma confeção interna ou origem espanhola de todas as peças.',
   {'fabrico':['modelo_velilla'],'distribuicao':['modelo_velilla']},desenvolvimento=True),
}

CLASSIFICACOES['nobrinde']=empresa('mista','Brindes, desenvolvimento à medida e impressão',
 'Combina distribuição de artigos, produção de projetos à medida e personalização numa operação com impressão própria.',
 'O fabrico próprio abrange projetos e coleções específicos. A execução interna é declarada pela empresa; as fontes não discriminam eventuais operações externas por encomenda.',
 {'distribuicao':['nobrinde_empresa'],'fabrico':['nobrinde_empresa','nobrinde_colecoes'],'personalizacao':['nobrinde_impressao','nobrinde_tecnicas']},
 etiquetas=['Distribuição','Produção à medida','Personalização interna'])

def modelo(id,titulo,resumo,tipo,visual,distincao,pergunta):
    return dict(id=id,titulo=titulo,resumo=resumo,sec='mercado',tipo='modelo-mercado',
        funcao=tipo,visual=visual,distincao=distincao,pergunta=pergunta,
        seccoes=[('Papel na cadeia',resumo),('O que distinguir',distincao),('O que confirmar',pergunta)],
        fontes=[],problemas=[],ancoras=[],relacionados=[],tags=titulo,
        empresas=[id for id,c in CLASSIFICACOES.items() if (len(c['funcoes'])>=2 if tipo=='mista' else tipo in c['funcoes'])])

MODELOS=[
 modelo('distribuicao-e-importacao','Armazenistas e distribuidores',
   'Disponibilizam uma oferta de artigos, através de stock, importação ou redes de fornecedores. Os produtos podem ser fabricados por outras empresas.',
   'distribuicao',('Artigos','Rede de fornecimento'),
   'Distribuir é colocar artigos ou meios de produção à disposição de outros profissionais. A existência de armazém, importação ou marca própria não comprova fabrico. Dimatur e Eurovinil representam o fornecimento de materiais e equipamentos a montante do brinde acabado.',
   'Onde está o stock? Quem fornece o artigo e de onde parte o pedido? A personalização e a preparação são executadas pela mesma entidade?'),
 modelo('fabricantes-e-produtores','Fabricantes e produtores',
   'Fabricam artigos ou componentes, ou documentam controlo de etapas produtivas. O âmbito deve ser identificado por linha, operação ou produto.',
   'fabrico',('Materiais','Artigo'),
   'Fabrico transforma materiais e componentes. Desenvolver o desenho, deter uma marca ou organizar compras não demonstra execução própria. Nos exemplos, distingue-se a produção de instrumentos de escrita, vestuário ou linhas identificadas; a impressão sobre um objeto é apresentada na categoria de personalização.',
   'Que artigo, componente ou etapa é produzido? A execução é interna ou contratada? Qual a instalação e a origem documentada para o produto concreto?'),
 modelo('personalizacao-impressao-acabamento','Personalizadores e especialistas em impressão',
   'Aplicam impressão, gravação, bordado ou outros acabamentos ao artigo. A aplicação da identidade visual distingue-se do fabrico do suporte.',
   'personalizacao',('Artigo','Identidade visual'),
   'Personalizar acrescenta ou altera uma imagem, inscrição ou acabamento. O artigo de base pode ter sido fabricado por terceiros. A publicação de um serviço não confirma automaticamente execução interna; quando há instalações próprias documentadas, o âmbito é indicado no cartão da empresa.',
   'Quem executa a técnica e em que local? Que suporte recebe a aplicação? Como são validadas arte, amostra e acabamento?'),
 modelo('empresas-de-atividade-mista','Empresas de atividade mista',
   'Combinam duas ou mais funções documentadas de distribuição, fabrico e personalização. A integração pode reunir operações próprias e serviços articulados com terceiros.',
   'mista',('Várias etapas','Uma operação articulada'),
   'Nesta classificação, atividade mista exige pelo menos duas das três funções documentadas. Desenho e desenvolvimento são assinalados separadamente, sem serem contados como fabrico. Cada empresa mantém um perfil único e uma atividade principal editorial, mesmo quando surge em vários modelos.',
   'Quais as etapas próprias? Quais são contratadas ou apenas coordenadas? Quem responde pelo controlo, preparação e entrega?'),
]
MODELOS_POR_ID={a['id']:a for a in MODELOS}
DESTAQUES=['stricker','bic-graphic','tela','solo-midocean','velilla-group','dimatur','nobrinde']
ETAPAS=[('Desenvolvimento','Definir desenho e requisitos.'),('Fabrico','Transformar materiais e componentes.'),('Distribuição','Disponibilizar artigos e gerir fornecimento.'),('Personalização','Aplicar uma identidade ao artigo.'),('Preparação e entrega','Conferir, embalar e encaminhar o pedido.')]
