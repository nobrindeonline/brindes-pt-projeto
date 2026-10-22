"""Seleção explícita das imagens locais autorizadas para Mercado."""
IMAGENS = {
    'distribuicao-e-importacao': {
        'cartao': ('DistribuicaoImportacao/armazem-2.jpg', 426, 320, 'Espaço de trabalho com artigos e caixas organizados.'),
        'corpo': ('DistribuicaoImportacao/armazem-2.jpg', 426, 320, 'Vista de um espaço de trabalho e armazenamento com caixas e equipamentos.'),
    },
    'desenvolvimento-e-marcas': {
        'cartao': ('visuais/desenvolvimento-e-marcas-cartao.jpg', 678, 452, 'Ilustração de uma equipa a trabalhar numa proposta de produto.'),
        'corpo': ('visuais/desenvolvimento-e-marcas-corpo.jpg', 800, 500, 'Esquema com ideia, estudo de viabilidade, desenvolvimento do produto, desenho do processo, plano de marketing e venda.'),
    },
    'vestuario-promocional-profissional': {
        'cartao': ('Vestuario/caroussel_categ_2025_vestuario_2.jpg', 1920, 1079, 'Quatro pessoas com camisas e calças em diferentes combinações.'),
        'corpo': ('Vestuario/9ae8a200-a385-11f0-86c5-0a58a9feac02.jpg', 240, 240, 'Peças de vestuário brancas com exemplos de aplicação gráfica.'),
    },
    'personalizacao-impressao-acabamento': {
        'cartao': ('PersonalizaoImpressaoAcabamento/timprexe-2000m2-home_18738370716552166dcc49b.jpg', 1440, 900, 'Espaço de produção com máquinas de impressão e bancadas.'),
        'corpo': ('PersonalizaoImpressaoAcabamento/mba-nobrinde-instalacoes-13_229814281652d5122a21c3.jpg', 750, 500, 'Equipamento de impressão com rolos de material ao fundo.'),
    },
    'materias-primas-consumiveis-equipamentos': {
        'cartao': ('MateriasConsumiveisEquipamentos/main_image_1765096775_69353d47a5a08.webp', 768, 428, 'Cortiça em diferentes formas junto de equipamento.'),
        'corpo': ('MateriasConsumiveisEquipamentos/mba-nobrinde-instalacoes-14_1964925630652d512870e3f.jpg', 750, 500, 'Rolos de material e equipamentos num espaço de trabalho.'),
    },
    'logistica-e-encomendas': {
        'cartao': ('LogisticaPreparacao/mba-nobrinde-instalacoes-24_1769148676652d515be29fb.jpg', 750, 500, 'Estantes de armazenamento com caixas e corredores de circulação.'),
        'corpo': ('LogisticaPreparacao/mba-nobrinde-instalacoes-19_1534709515652d5142477da.jpg', 750, 500, 'Pessoa junto de uma bancada num espaço de armazenamento.'),
    },
}

LEGENDAS = {
    'desenvolvimento-e-marcas': 'Esquema ilustrativo de etapas do desenvolvimento de produto. O percurso pode variar e não descreve a operação de uma empresa deste artigo.',
    'distribuicao-e-importacao': 'Armazenamento e organização de artigos. Imagem de contexto, sem atribuição às empresas citadas.',
    'vestuario-promocional-profissional': 'Exemplos visuais de aplicação gráfica em vestuário. Não representam produtos das empresas citadas.',
    'personalizacao-impressao-acabamento': 'Equipamento e materiais num espaço de impressão. Imagem de contexto, sem atribuição às empresas citadas.',
    'materias-primas-consumiveis-equipamentos': 'Materiais e equipamentos num espaço de trabalho. Imagem de contexto, sem atribuição às empresas citadas.',
    'logistica-e-encomendas': 'Bancada de trabalho junto de uma zona de armazenamento. Imagem de contexto, sem atribuição às empresas citadas.',
}

def destino(id, uso):
    from pathlib import PurePosixPath
    return 'assets/mercado/visuais/' + id + '-' + uso + PurePosixPath(IMAGENS[id][uso][0]).suffix

# Reutilização de imagens locais já existentes, inspecionadas para os novos temas.
IMAGENS.update({
    'papelaria-e-escritorio': {'cartao': ('../produtos/visuais/escritorio-cartao.jpg',300,300,'Calendário de secretária sobre fundo branco.')},
    'tecnologia-e-acessorios-digitais': {'cartao': ('../produtos/visuais/tecnologia-cartao.jpg',300,301,'Dispositivos de energia portátil sobre fundo branco.')},
    'casa-lazer-e-bebidas': {'cartao': ('../produtos/visuais/bebidas-cartao.jpg',300,301,'Canecas de cerâmica com interiores de cores diferentes.')},
    'textil-e-vestuario': {'cartao': ('Vestuario/caroussel_categ_2025_vestuario_2.jpg',1920,1079,'Pessoas com diferentes combinações de vestuário.')},
    'sazonalidade-e-clima': {'cartao': ('../produtos/visuais/texteis-bones.jpg',300,300,'Bonés em diferentes cores, como exemplo de acessórios sazonais.')},
    'brindes-ecologicos': {'cartao': ('../produtos/visuais/canetas-cartao.jpg',300,300,'Estojo aberto com instrumentos de escrita de corpo claro; imagem de contexto, sem comprovar atributos ambientais.')},
})

def preparar(root):
    """Copia os bytes originais para URLs neutros; não transforma as imagens."""
    for id, images in IMAGENS.items():
        for uso, (src, _, _, _) in images.items():
            source = root / 'assets/mercado' / src
            target = root / destino(id, uso)
            if not source.is_file():
                raise FileNotFoundError(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            data = source.read_bytes()
            if not target.is_file() or target.read_bytes() != data:
                target.write_bytes(data)
