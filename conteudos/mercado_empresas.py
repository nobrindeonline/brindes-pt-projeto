"""Dados públicos para cartões de exemplos; funções distintas de produção."""
EMPRESAS = {
    'stricker': dict(nome='Stricker', local='Coimbra, Portugal · sede', papel='Desenvolvimento de produto e distribuição',
        atividade='Declara criação e desenvolvimento de brindes, stock e distribuição a profissionais do setor. A fonte não identifica o fabricante de cada artigo.', fontes=['stricker']),
    'tejobrinde': dict(nome='TejoBrinde', local='Prior Velho, Portugal · sede', papel='Fornecimento de brindes e exportação',
        atividade='Descreve fornecimento nacional e exportação, com stock em Lisboa e serviço de gravações. O perfil distingue estes serviços atuais da informação histórica sobre importação.', fontes=['tejo', 'tejo_servicos']),
    'th-clothes': dict(nome='TH Clothes / Organizações Biscana', local='Batalha, Portugal · sede da titular', papel='Marca de vestuário promocional',
        atividade='A TH Clothes é detida pela Organizações Biscana. A história da marca descreve desenvolvimento de produto, stock e distribuição, sem comprovar confeção própria de todas as peças.', fontes=['th']),
    'roly': dict(nome='Roly / Gor Factory', local='Fortuna, Murcia, Espanha · sede da sociedade', papel='Fornecimento de vestuário e distribuição',
        atividade='O site da Gor Factory descreve, para Roly, encomendas por cor e tamanho, consulta de stock e coordenação entre armazém e transportadores.', fontes=['roly', 'roly_identidade']),
    'dimatur': dict(nome='Dimatur', local='Turquel, Portugal · sede logística e administrativa', papel='Fornecedor de materiais e equipamentos',
        atividade='Documenta matérias-primas, consumíveis e tecnologia para comunicação visual e transformação, acompanhados de assistência técnica e formação.', fontes=['dimatur', 'dimatur_historia']),
    'eurovinil': dict(nome='Eurovinil', local='Maia, Portugal · localização publicada', papel='Distribuição de consumíveis e equipamentos',
        atividade='Descreve fornecimento para comunicação visual, serigrafia e impressão digital, com suporte técnico e formação. Fornecer materiais e máquinas não equivale a executar a personalização dos artigos.', fontes=['eurovinil', 'eurovinil_local']),
    'solo-midocean': dict(nome='Solo midocean', local='Países Baixos · sede', papel='Fornecimento, impressão e logística',
        atividade='Identifica instalações próprias de logística e impressão na Polónia. Documenta também dobragem, etiquetas e embalagem, com opções que variam por pedido e região.', fontes=['solo_locais', 'solo_preparacao']),
}

# Seleção por função documentada, sem ordenação comercial.
EXEMPLOS = {
    'distribuicao-e-importacao': ['stricker', 'tejobrinde', 'solo-midocean'],
    'desenvolvimento-e-marcas': ['stricker', 'th-clothes'],
    'vestuario-promocional-profissional': ['th-clothes', 'roly'],
    'personalizacao-impressao-acabamento': ['solo-midocean'],
    'materias-primas-consumiveis-equipamentos': ['dimatur', 'eurovinil'],
    'logistica-e-encomendas': ['solo-midocean', 'roly'],
}

# Logótipos locais: a identificação visual distingue marca e sociedade titular.
LOGOS = {
    'stricker': ('Stricker/images.jpg', 360, 465, 'Logótipo da Stricker'),
    'tejobrinde': ('TejoBrinde/images.png', 263, 157, 'Logótipo da TejoBrinde'),
    'th-clothes': ('THClothes/THClothes.png', 500, 500, 'Logótipo da marca TH Clothes'),
    'roly': ('Roly/images.jpg', 600, 300, 'Logótipo da marca Roly, da Gor Factory'),
    'dimatur': ('Dimatur/2016_logo dimatur.jpg', 567, 378, 'Logótipo da Dimatur'),
    'eurovinil': ('Eurovinil/images.jpg', 446, 448, 'Logótipo da Eurovinil'),
    'solo-midocean': ('MidOcean/midocean_logo.jpg', 200, 200, 'Logótipo da Solo midocean'),
}

from conteudos.mercado_novos_perfis import NOVOS
from conteudos.mercado_areas import ASSOCIACOES
for id, data in NOVOS.items():
    EMPRESAS[id] = dict(nome=data['nome'], local=data['local'], papel=data['papel'],
                       atividade=data['resumo'], fontes=list(dict.fromkeys(key for s in data['seccoes'] for key in s['fontes'])))
EXEMPLOS.update({id:list(companies) for id,companies in ASSOCIACOES.items()})
LOGOS.update({
    'nobrinde': ('Nobrinde/images.jpg',200,200,'Logótipo da Nobrinde'),
    'aodaci': ('AODACI/images.jpg',400,400,'Logótipo da AODACi'),
    'bic-graphic': ('BICGraphic/bicgraphiclogo3_8205b0d5b4.png',294,294,'Logótipo da BIC Graphic'),
    'giving-europe': ('Giving Europe/images.jpg',200,200,'Logótipo da Giving Europe'),
    'goya': ('Goya/goya-logo-png_seeklogo-62373.png',600,600,'Logótipo da Goya Importaciones'),
    'pf-concept': ('PF Concept/PF-Concept.png',800,418,'Logótipo da PF Concept'),
    'plural': ('Plural/images.jpg',447,447,'Logótipo da Plural'),
    'tela': ('Tela/Header_Logo.png',548,284,'Logótipo da Tela'),
    'velilla-group': ('Velilla/images.png',678,294,'Logótipo Velilla, do grupo titular de MUKUA'),
    'xd-connects': ('XD Connects/images.png',658,466,'Logótipo da XD Connects'),
})
