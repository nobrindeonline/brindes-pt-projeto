"""Áreas editoriais de produto; associação documentada sem ranking."""
FONTES_AREAS = {
 'bic_empresa': ('BIC Graphic — Identidade e atividade', 'https://www.bicgraphic.com/gb/why-bic-graphic.html'),
 'bic_historia': ('BIC Graphic — História do grupo e da divisão promocional', 'https://www.bicgraphic.com/gb/our-history.html'),
 'bic_tecnicas': ('BIC Graphic — Técnicas de personalização', 'https://www.bicgraphic.com/gb/printing-techniques.html'),
 'bic_areas': ('BIC Graphic — Áreas de escrita e papelaria', 'https://www.bicgraphic.com/gb/'),
 'giving_empresa': ('Giving Europe — Atividade, sede e operação', 'https://www.givingeurope.com/global/en/about-us-giving-europe'),
 'giving_missao': ('Giving Europe — Missão e visão', 'https://www.givingeurope.com/global/en/about-giving-europe/mission-vision'),
 'giving_fsc': ('Giving Europe — Certificado de cadeia de custódia publicado', 'https://webshop.favoritegifts.eu/media/wysiwyg/Givingeurope/Taking-care/FSC_Certificate_910066_FL-B.V.pdf'),
 'tela_empresa': ('Tela — História e produção', 'https://www.tela.pt/pt/sobre-nos'),
 'tela_operacao': ('Tela — Serviços de fornecimento e logística', 'https://www.tela.pt/pt/tela360'),
 'plural_empresa': ('Plural — Apresentação da empresa', 'https://www.plural.com.pt/pt/sobre-nos'),
 'plural_areas': ('Plural — Áreas de atividade promocional', 'https://www.plural.com.pt/pt/brindes'),
 'plural_condicoes': ('Plural — Modelo de encomenda e personalização', 'https://www.plural.com.pt/pt/termos-e-condies'),
 'plural_local': ('Plural — Localização publicada', 'https://www.plural.com.pt/pt/contatos-e-mapa'),
 'goya_empresa': ('Goya Importaciones — Atividade e personalização', 'https://www.ggoya.com/es/goya'),
 'goya_areas': ('Goya Importaciones — Famílias e necessidades sazonais', 'https://www.ggoya.com/es/'),
 'goya_legal': ('Goya Importaciones y Distribuciones — Identificação legal', 'https://www.ggoya.com/es/aviso-legal'),
 'goya_preparacao': ('Goya — Manipulação especial de pedidos', 'https://www.ggoya.com/es/manipulado-especial'),
 'xd_empresa': ('XD Connects — História e desenvolvimento', 'https://www.xdconnects.com/en-gb/about-us'),
 'xd_relatorio': ('XD Connects — Annual Impact Report 2024', 'https://media.xdconnects.com/Downloads/ESG/Report/Annual_Impact_Report_2024.pdf'),
 'xd_operacao': ('XD Connects — Fornecimento e personalização', 'https://www.xdconnects.com/'),
 'aodaci_relatorio': ('AODACi — Relatório de sustentabilidade 2024, publicado em setembro de 2025', 'https://catalog.aodaci.com/view/307252347/1/'),
 'aodaci_atividade': ('AODACi — Apresentação institucional e famílias de produtos', 'https://www.linkedin.com/company/aodaci'),
 'aodaci_lancamento': ('eppi Magazine — Entrevista sobre o lançamento, 11/01/2024', 'https://www.eppi-online.com/2024/01/11/the-time-is-right-for-a-new-approach/'),
 'pf_empresa': ('PF Concept — Identidade e modelo profissional', 'https://www.pfconcept.com/en_nl/about-pf-concept'),
 'pf_areas': ('PF Concept — Áreas de atividade', 'https://www.pfconcept.com/en_nl/?locale=en_US'),
 'pf_sustentabilidade': ('PF Concept — Estratégia e progresso de sustentabilidade', 'https://www.pfconcept.com/en_nl/sustainability-report_about-pf-concept'),
 'pf_transparencia': ('PF Concept — Transparência e documentação de produto', 'https://www.pfconcept.com/nl_nl/sustainability-overview'),
 'velilla_historia': ('Velilla Group — História e marcas', 'https://www.velilla-group.com/es/nuestra-historia'),
 'velilla_mukua': ('Velilla Group — Atividade MUKUA em PROMOGIFT, 12/01/2026', 'https://www.velilla-group.com/es/velilla-group-presenta-las-novedades-de-mukua'),
 'velilla_ambiente': ('Velilla Group — Green Project', 'https://www.velilla-group.com/es/greenproject'),
 'velilla_independente': ('Cinco Días — Evolução da Velilla Group, 19/04/2025', 'https://cincodias.elpais.com/companias/2025-04-19/velilla-group-la-empresa-que-viste-a-la-industria-y-a-la-hosteleria-en-espana-cuadruplica-sus-ventas-en-diez-anos.html'),
 'tejo_areas': ('TejoBrinde — Impacto Gift: marca e áreas de produto', 'https://www.tejobrinde.pt/pt-pt/impacto-gift'),
 'solo_areas': ('Solo midocean — Famílias e possibilidades de personalização', 'https://www.midocean.com/uk/gb/eur/content/more-than-gifts'),
}

# Limites da consulta: os excertos públicos indexados não incluem áreas reservadas.
NOTAS_FONTES = {
    key: 'Conteúdo consultado na indexação pública da página oficial; a abertura direta não respondeu nesta consulta.'
    for key in ('pf_empresa','pf_areas','pf_sustentabilidade','pf_transparencia','velilla_historia','velilla_mukua','velilla_ambiente','xd_relatorio')
}
NOTAS_FONTES.update({
    'xd_empresa': 'Texto institucional consultado na indexação pública; a página direta depende de JavaScript.',
    'xd_operacao': 'Descrição institucional consultada na indexação pública; a página direta depende de JavaScript.',
    'aodaci_lancamento': 'Entrevista consultada através do excerto público indexado; abertura direta indisponível.',
})

def area(id, titulo, resumo, texto, criterios, relacionados):
    return dict(id=id, sec='mercado', tipo='area-mercado', titulo=titulo, resumo=resumo,
                seccoes=[('Compreender esta área',texto),('Critérios de leitura',criterios)],
                fontes=[], relacionados=relacionados, problemas=[], ancoras=[], tags=titulo)

AREAS = [
 area('papelaria-e-escritorio','Papelaria e Escritório',
      'Escrita, cadernos e organização do trabalho: empresas com atividade documentada neste segmento.',
      'Esta área reúne instrumentos de escrita, suportes em papel e acessórios de organização. O mesmo fornecedor pode desenvolver um produto, distribuí-lo ou aplicar uma identidade visual. Os exemplos ajudam a distinguir essas funções.',
      'A oferta de papelaria não comprova produção própria de papel ou de todos os objetos. A origem, a composição, o acabamento e a eventual certificação devem ser lidos no contexto do produto. A seleção abaixo é editorial e não estabelece uma ordem de qualidade.',
      ['canetas-e-escrita','papel-e-cartao']),
 area('tecnologia-e-acessorios-digitais','Tecnologia e Acessórios Digitais',
      'Energia portátil, áudio e acessórios de utilização digital como suportes de comunicação promocional.',
      'Carregamento, áudio e acessórios para dispositivos são famílias presentes na oferta promocional. Nesta área importa distinguir a seleção ou o desenvolvimento do objeto da impressão de uma marca e da fabricação dos componentes eletrónicos.',
      'Compatibilidade, utilização e documentação técnica são específicas de cada produto. Ter uma oferta tecnológica não comprova fabricar baterias ou circuitos. Os perfis identificam os processos divulgados e os pontos que não puderam ser confirmados.',
      ['tecnologia','impressao-uv']),
 area('casa-lazer-e-bebidas','Casa, Lazer e Bebidas',
      'Recipientes para bebidas, utensílios e artigos para casa e lazer: modelos de fornecimento e personalização.',
      'Esta área reúne recipientes para bebidas, utensílios de casa e artigos de lazer. A associação das empresas apoia-se em famílias publicamente identificadas; não significa que todas fabriquem os objetos ou cubram todas as necessidades.',
      'Capacidade, materiais, conservação e adequação ao uso devem ser confirmadas por artigo. A oferta de uma garrafa ou caneca não permite generalizar origem de fabrico, desempenho térmico ou documentação a toda a gama.',
      ['garrafas-copos-e-canecas','vidro-e-ceramica']),
 area('textil-e-vestuario','Têxtil e Vestuário',
      'Marcas e fornecedores de peças promocionais, desportivas e profissionais, com funções diferentes na cadeia.',
      'O vestuário pode apoiar identificação, campanhas e contextos profissionais. As empresas desta área trabalham a definição de modelos, o fornecimento de tamanhos e cores e a distribuição. Marca, confeção e personalização não são a mesma atividade.',
      'A composição e a construção da peça condicionam a aplicação gráfica. Vestuário de trabalho não implica automaticamente proteção individual. MUKUA é apresentada no perfil da Velilla Group, sua titular, sem criar uma página duplicada para a marca.',
      ['materiais-texteis','bordado','transfers']),
 area('sazonalidade-e-clima','Sazonalidade e Clima',
      'Artigos relacionados com sol, chuva, frio e épocas do ano, considerados pelo contexto de utilização.',
      'Bonés, artigos de praia, guarda-chuvas e peças para dias frios respondem a contextos sazonais diferentes. A categoria relaciona a utilização com a época e o clima; não descreve uma especialização exclusiva das empresas apresentadas.',
      'O momento de utilização e a preparação de uma campanha devem ser distinguidos da disponibilidade em stock. Um artigo para chuva ou sol não comprova, por si só, uma característica de proteção. A imagem do segmento é apenas ilustrativa.',
      ['texteis','da-ideia-a-entrega']),
 area('brindes-ecologicos','Brindes Ecológicos',
      'Uma leitura transversal de materiais, rastreabilidade e políticas ambientais documentadas pelos fornecedores.',
      '“Brindes Ecológicos” é uma designação editorial transversal. Reúne empresas com informação pública sobre materiais, origem, rastreabilidade ou redução de impacto. Uma empresa pode aparecer também em Papelaria, Tecnologia, Casa ou Têxtil.',
      'A inclusão não certifica a empresa nem torna toda a sua oferta ambientalmente superior. Material reciclado, conteúdo orgânico, possibilidade de reutilização e certificação são afirmações diferentes. Devem ser verificadas quanto a objeto, âmbito e validade; não se comparam desempenhos sem base equivalente.',
      ['como-escolher-o-material','papel-e-cartao','madeira-e-bambu']),
]

# Texto e fontes específicos de cada associação, sem replicar o perfil completo.
ASSOCIACOES = {
 'papelaria-e-escritorio': {
   'bic-graphic': ('A divisão promocional do grupo BIC documenta personalização de instrumentos de escrita e oferta de cadernos.', ['bic_empresa','bic_areas']),
   'stricker': ('A página de personalização identifica esferográficas como suporte de aplicação, no seu fornecimento a revendedores.', ['stricker_impressao','stricker_profissionais']),
   'tela': ('A oferta pública inclui escrita, cadernos e organização de secretária, com personalização e acompanhamento do pedido.', ['tela_operacao','tela_empresa']),
   'giving-europe': ('O grossista identifica escrita e escritório entre as suas áreas e documenta impressão e logística próprias.', ['giving_empresa']),
 },
 'tecnologia-e-acessorios-digitais': {
   'xd-connects': ('Desenvolve e seleciona brindes, com oferta tecnológica e operação de personalização descritas nas fontes institucionais.', ['xd_empresa','xd_relatorio','xd_operacao']),
   'aodaci': ('O relatório institucional identifica soluções tecnológicas no desenvolvimento de brindes; a apresentação inclui colunas de áudio.', ['aodaci_relatorio','aodaci_atividade']),
   'plural': ('A área tecnológica publicada abrange energia portátil, memória e acessórios para dispositivos, com personalização para campanhas.', ['plural_areas']),
   'solo-midocean': ('A oferta identifica tecnologia como família de fornecimento, apoiada por personalização e logística.', ['solo_areas','solo_locais']),
 },
 'casa-lazer-e-bebidas': {
   'goya': ('As famílias publicadas incluem canecas, garrafas, utensílios de casa e artigos de lazer, com importação e personalização documentadas.', ['goya_areas','goya_empresa']),
   'stricker': ('A página de personalização identifica canecas, garrafas e termos entre os suportes possíveis de aplicação.', ['stricker_impressao']),
   'tejobrinde': ('A marca própria Impacto Gift identifica copos, garrafas e canecas entre as suas áreas de fornecimento.', ['tejo_areas']),
   'pf-concept': ('A oferta pública identifica recipientes para bebidas, casa, cozinha e lazer; o modelo integra fornecimento e personalização.', ['pf_areas','pf_empresa']),
 },
 'textil-e-vestuario': {
   'th-clothes': ('Marca da Organizações Biscana com desenvolvimento, stock e distribuição de vestuário promocional documentados.', ['th']),
   'roly': ('Marca da Gor Factory para oferta têxtil, com encomendas por variante e preparação logística documentadas.', ['gor_marcas','roly']),
   'velilla-group': ('MUKUA é a marca de têxtil promocional da Velilla Group, distinta das suas linhas de vestuário profissional e calçado.', ['velilla_historia','velilla_mukua']),
 },
 'sazonalidade-e-clima': {
   'stricker': ('A página de personalização identifica guarda-chuvas, bonés e mantas como suportes de aplicação, adequados a contextos sazonais distintos.', ['stricker_impressao']),
   'solo-midocean': ('A apresentação de famílias inclui artigos sazonais, guarda-chuvas e vestuário para chuva.', ['solo_areas']),
   'goya': ('A navegação pública distingue verão e inverno, com leques, acessórios de praia, guarda-chuvas e mantas.', ['goya_areas']),
   'tejobrinde': ('A apresentação da Impacto Gift identifica inverno, chapéus de chuva e impermeáveis, além de bonés e chapéus.', ['tejo_areas']),
 },
 'brindes-ecologicos': {
   'aodaci': ('O relatório de sustentabilidade descreve seleção de materiais, fornecedores e desenho do produto. São declarações institucionais com âmbito próprio.', ['aodaci_relatorio']),
   'pf-concept': ('Publica estratégia ambiental, documentação e critérios de transparência de materiais e produtos, sem cobertura uniforme de toda a oferta.', ['pf_sustentabilidade','pf_transparencia']),
   'giving-europe': ('Documenta uma seleção de produtos com cadeia de custódia FSC e disponibiliza o certificado para verificar o âmbito.', ['giving_empresa','giving_fsc']),
   'stricker': ('Publica políticas de sustentabilidade aplicadas à conceção e comercialização. A associação não equivale a certificar todos os brindes.', ['stricker_politicas']),
 },
}
