"""Transfers: processos documentados e designações comerciais por confirmar."""

FONTES_TRANSFERS = {
    'trmimaki': ('Mimaki — TxF150-75: What is DTF? e consumíveis', 'https://mimaki.com/product/inkjet/dtf/txf150-75/'),
    'trgoof': ('Transfer Express — Goof Proof: transfers serigráficos de plastisol', 'https://www.transferexpress.com/heat-press-transfers/goof-proof-screen-printed-transfers'),
    'traplicar': ('Transfer Express — Instruções de aplicação por produto', 'https://www.transferexpress.com/application-instructions'),
    'trpapel': ('Avient — Technical Tips for Transfer Printing: papel de libertação e registo', 'https://www.avient.com/technical-tips-transfer-printing'),
    'tradesivo': ('Avient — Union Ink: adesivos para transfers', 'https://www.avientspecialtyinks.com/products-brand/union-ink/union-ink-transfer-inks'),
    'trfalhas': ('Avient — Transfer Troubleshooting: verificações de processo', 'https://www.avient.com/transfer-troubleshooting'),
    'trdigital': ('Siser — Digital Printing: materiais para impressão e corte', 'https://www.siser.com/digital-printing/'),
    'trfilmes': ('Siser — Filmes imprimíveis brancos e transparentes', 'https://www.siser.com/news/printable-white-films-printable-transparent-films/'),
    'trbase': ('FOREVER — Laser-Dark (No-Cut): A-Foil e revestimento branco do B-Paper', 'https://www.forever-ots.com/product/laser-dark-no-cut-cmyw/'),
}

IDS = ['transfer-serigrafico', 'transfer-digital', 'transfer-digital-com-base', 'dtf']
TITULOS = ['Transfer Serigráfico', 'Transfer Digital', 'Transfer Digital com Base', 'DTF — Direct to Film']

# Utilização autorizada expressamente pelo utilizador em 30/09/2026.
# Seleção visual: não usar duplicados nem esquemas com etapas incorretas.
IMAGENS_TRANSFERS = {
    'transfer-serigrafico': {
        'processo': ('Transfer Serigrafico/unnamed.jpg', 474, 438, 'Rodo sobre uma tela de serigrafia com tinta amarela e um desenho tipográfico.', 'Exemplo de impressão por tela. A imagem não identifica o suporte nem a formulação da tinta.'),
        'materiais': ('Transfer Serigrafico/unnamed (20).jpg', 474, 474, 'Prensa térmica plana preta com pega e vários acessórios apresentados ao lado.', 'Exemplo de prensa e acessórios. O equipamento, isoladamente, não identifica o tipo de transfer ou a compatibilidade do artigo.'),
    },
    'transfer-digital': {
        'processo': ('Transfer Digital/unnamed (23).jpg', 474, 266, 'Impressora de grande formato com um rolo de material impresso com imagens coloridas.', 'Exemplo de impressão em rolo. A fotografia não permite identificar o material nem confirmar a sua aplicação têxtil.'),
    },
    'dtf': {
        'processo': ('DTF/unnamed (27).jpg', 474, 469, 'Montagem com impressora de mesa, rolo branco, folha com desenho colorido, equipamento plano e frascos de tinta.', 'Conjunto ilustrativo de equipamento e consumíveis. As referências e a compatibilidade entre componentes devem ser confirmadas.'),
        'materiais': ('DTF/unnamed (28).jpg', 474, 474, 'Montagem com equipamentos de impressão em rolo e duas t-shirts, uma branca e outra preta, com motivos coloridos.', 'Equipamento e exemplos ilustrativos de vestuário. A montagem não comprova a composição dos tecidos nem o desempenho após aplicação.'),
    },
}

CHECKLIST = [
    ('Artigo real', 'Registar referência, composição, cor, elasticidade, revestimentos e zona de aplicação. Verificar o acesso da prensa e o efeito de costuras, bolsos e fechos.'),
    ('Sistema identificado', 'Obter fabricante, referência do transfer, consumíveis e ficha de aplicação em vigor. O nome da técnica, isoladamente, não é uma especificação.'),
    ('Arte aprovada', 'Fixar dimensão, posição, cores, fundo, contornos e versão do ficheiro. Rever letras, espaços e pormenores à escala final.'),
    ('Aplicação documentada', 'Confirmar temperatura, tempo, pressão, eventual pré-prensagem, modo de destacar o suporte e acabamento final na ficha específica. Não copiar parâmetros de outra modalidade. [traplicar]'),
    ('Amostra e utilização', 'Avaliar cor, aderência, toque, flexibilidade e comportamento no uso previsto numa peça representativa. Acordar critérios de aceitação e ensaios, incluindo lavagem quando pertinente.'),
    ('Cuidados e alterações', 'Obter instruções de lavagem do transfer e do artigo, confirmar a compatibilidade entre ambas e entregar os cuidados da peça personalizada. Mudanças de tecido, cor ou consumível exigem reavaliação.'),
]

COMPARACOES = {
    'transfer-serigrafico': 'No serigráfico, a imagem é produzida por telas num suporte intermédio; no exemplo digital de impressão e corte, a imagem é impressa digitalmente num material próprio. «Digital com Base» acrescenta uma característica ainda por definir pelo fornecedor. O DTF tem uma sequência documentada de impressão em filme e preparação de adesivo em pó. Compare a mesma arte e peça: preparação, número de cores, área coberta e volume alteram a escolha.',
    'transfer-digital': 'O serigráfico forma a imagem por serigrafia, enquanto o exemplo desta página utiliza impressão digital e corte. «Digital com Base» exige esclarecer a camada ou o material que o fornecedor chama base; não é automaticamente uma tecnologia separada. O DTF também é digital, mas identifica um fluxo próprio com filme e pó termofusível. Não transfira as regras de corte, espelhamento ou aplicação de um sistema para outro.',
    'transfer-digital-com-base': 'O transfer serigráfico identifica a forma de imprimir; «Transfer Digital» identifica de modo amplo a origem digital da imagem; DTF identifica o fluxo em filme com adesivo em pó. «Com Base» pode descrever uma característica que existe em mais de um sistema. Estas quatro entradas organizam a consulta, mas não são quatro famílias necessariamente exclusivas. A referência do fornecedor é indispensável para uma comparação técnica.',
    'dtf': 'O transfer serigráfico usa telas para produzir a imagem. O exemplo de transfer digital por impressão e corte usa um material imprimível que precisa da preparação indicada pelo fabricante. «Digital com Base» permanece uma designação por definir; a presença de branco, por si só, não distingue esse nome de DTF. Compare preparação, cobertura, toque e ensaios no mesmo artigo, sem atribuir uma vantagem universal ao DTF.',
}


def guia(id, resumo, passos, seccoes, problemas, fontes, especifico):
    return {
        'id': id, 'sec': 'tecnicas', 'tipo': 'tecnica', 'titulo': TITULOS[IDS.index(id)],
        'resumo': resumo, 'data_revisao': '2026-09-30', 'data_revisao_texto': '30 de setembro de 2026',
        'transfer': True, 'passos': passos,
        'ids_seccoes': ['definicao', 'processo', 'materiais', 'resultado', 'arte', 'vantagens-limites', 'confirmar', 'comparar'],
        'seccoes': seccoes + [
            ('Verificações antes da produção', 'Use esta lista para preparar uma prova representativa. As perguntas são orientação editorial; não constituem uma ficha de produção.'),
            ('Comparar as quatro modalidades', COMPARACOES[id]),
        ],
        'checklist': [especifico] + CHECKLIST,
        'problemas': problemas, 'fontes': fontes,
        'relacionados': ['transfers'] + [other for other in IDS if other != id],
        'ancoras': ['materiais/index.html#texteis', 'produtos/index.html#texteis', 'produtos/index.html#sacos'],
        'tags': 'transfers transferências calor pressão prensa tecido lavagem ' + TITULOS[IDS.index(id)] + ' ' + especifico[1],
    }


SERIGRAFICO = guia(
    'transfer-serigrafico',
    'Imagem produzida por serigrafia num suporte de libertação e aplicada com prensa térmica. Tintas, adesivo e resultado dependem do sistema escolhido.',
    ['Preparar a arte e as separações', 'Imprimir no suporte de libertação', 'Preparar tinta e adesivo segundo a ficha', 'Prensar, destacar e avaliar a amostra'],
    [
        ('O que é', 'Certos transfers são produzidos por serigrafia num papel ou suporte de libertação, com tintas adequadas e uma camada adesiva. A aplicação ao artigo ocorre depois, numa prensa térmica. A Avient documenta papéis de transferência e adesivos próprios para esta utilização. [trpapel] [tradesivo]\n\nA Transfer Express descreve Goof Proof como um transfer com tinta plastisol serigráfica. É um exemplo identificado, não a composição de todos os transfers serigráficos nem uma garantia de durabilidade para qualquer peça. [trgoof]'),
        ('Como funciona', 'Preparam-se as cores e o registo do desenho, imprime-se a imagem no suporte intermédio e prepara-se o sistema tinta/adesivo conforme as respetivas fichas. A Avient apresenta adesivo imprimível e adesivo em pó; não se deve assumir que todos os produtos usam a mesma construção. [tradesivo]\n\nNa aplicação, posiciona-se o transfer e usa-se calor e pressão para o fixar ao artigo. O momento e o modo de retirar o suporte dependem do produto. As instruções Goof Proof distinguem condições consoante a variante e o tecido: não se publica aqui uma receita genérica. [trgoof] [traplicar]'),
        ('Materiais e artigos a considerar', 'No caso Goof Proof, o fabricante indica algodão, poliéster e misturas de algodão/poliéster nas instruções de aplicação. Isso não valida todos os artigos feitos com essas fibras. [trgoof]\n\nT-shirts, sweatshirts ou painéis de sacos podem ser candidatos a avaliar. Peça confirmação para a referência concreta: revestimentos, elasticidade, espessura e acesso à prensa podem alterar a viabilidade. Não deduza a adequação a nylon, tecidos impermeabilizados ou peças sensíveis ao calor a partir de uma aprovação em algodão.'),
        ('Cores, definição e toque', 'Peça as referências de tinta e uma prova para as cores da marca. Avalie o alinhamento entre cores, a leitura de letras pequenas e os espaços vazios. A Avient assinala a importância do papel e da sua estabilidade para o registo. [trpapel]\n\nO desenho acrescenta uma camada à superfície. Confirme cobertura, relevo, flexibilidade e toque no tamanho final; uma área cheia e um desenho com espaços não devem ser avaliados apenas pela mesma amostra reduzida. O toque anunciado para um produto não caracteriza toda a família.'),
        ('Preparar a arte e escolher', 'Entregue o original, as dimensões finais e as referências de cor. Peça ao produtor as regras para separações, linhas finas, espaços negativos e eventuais meios-tons. Se o desenho incluir fotografia ou degradés, confirme como serão preparados e aceite uma prova antes de decidir. Não converta automaticamente qualquer arte numa promessa de reprodução fotográfica.\n\nCompare propostas com o mesmo artigo, número de posições, dimensão e volume. O número de cores e a preparação necessária entram na avaliação, mas não permitem concluir que esta modalidade é sempre mais barata ou preferível para grandes quantidades.'),
        ('Vantagens e limitações', 'A produção da imagem num suporte separado permite distinguir a impressão da aplicação ao artigo. Pode ser útil quando se pretende aprovar previamente o motivo; armazenamento e utilização posterior exigem condições confirmadas pelo fornecedor.\n\nA aplicação continua dependente da peça e da prensa. Registo, libertação do papel, aderência e comportamento na lavagem precisam de validação. A comparação de durabilidade deve usar ensaios e condições equivalentes, não apenas o nome da técnica.'),
    ],
    [
        ('Cores desalinhadas', 'Comparar o transfer antes da aplicação com a arte. Rever registo, papel e controlo de humidade com o produtor. [trpapel]'),
        ('Libertação incompleta ou fraca aderência', 'Identificar suporte, tinta, preparação e ficha de prensagem. A Avient apresenta várias causas possíveis; não aumentar a temperatura sem diagnóstico. [trfalhas]'),
        ('Falhas após uso ou lavagem', 'Guardar amostra e registo do lote; confirmar aplicação, tecido e cuidados seguidos. Solicitar análise antes de atribuir o problema apenas à tinta ou ao utilizador.'),
    ],
    ['trgoof', 'trpapel', 'tradesivo', 'trfalhas', 'traplicar'],
    ('Construção serigráfica', 'Confirmar tinta, suporte de libertação, adesivo, separações de cor e estado de preparação em que o transfer é fornecido.'),
)

DIGITAL = guia(
    'transfer-digital',
    'Uma designação ampla que exige identificar o sistema. Conheça um exemplo documentado de impressão digital num material de transferência e os critérios a confirmar.',
    ['Identificar o sistema digital', 'Imprimir no material compatível', 'Preparar o motivo conforme o sistema', 'Aplicar segundo a ficha e avaliar'],
    [
        ('O que significa «Transfer Digital»', 'A designação, sem uma ficha que identifique fornecedor, tinta e suporte, não define um processo. O sistema utilizado pela Nobrinde continua por confirmar. Aqui explica-se apenas um exemplo documentado: a Siser disponibiliza materiais próprios para impressão digital e corte, incluindo Colorprint PU. Este exemplo não identifica o serviço da Nobrinde. [trdigital]\n\nNão se deve interpretar automaticamente o nome como DTF, sublimação, vinil de recorte ou impressão direta no tecido. O vinil apenas recortado não recebe a imagem por impressão; a impressão direta dispensa o suporte intermédio deste exemplo.'),
        ('Como funciona no exemplo de impressão e corte', 'A imagem é impressa digitalmente num material de transferência compatível com a impressora e a tinta. O motivo é preparado para aplicação e transferido para o artigo com calor e pressão segundo a ficha do material. A família Siser inclui construções diferentes, pelo que a referência faz parte da descrição do processo. [trdigital]\n\nPara os filmes brancos descritos pela Siser, há impressão, corte, remoção do excedente e utilização de película de aplicação. Nos transparentes descritos na mesma fonte, a impressão é espelhada e não se usa essa película. Não aplique uma destas sequências a todo o «transfer digital». [trfilmes]'),
        ('Materiais e tipos de artigos', 'Vestuário e painéis têxteis de sacos são possibilidades a discutir com o fornecedor, não compatibilidades confirmadas pelo nome. Indique composição, tratamento superficial, cor e elasticidade; confirme também se o artigo tolera a aplicação e se a zona permite contacto uniforme.\n\nNo exemplo Siser, os filmes brancos são apresentados para tecidos claros e escuros, enquanto os transparentes são indicados para claros. Essa distinção de cor não substitui a aprovação da composição e do revestimento para a referência selecionada. [trfilmes]'),
        ('Cores, definição e aspeto', 'Peça uma prova para imagens multicolores, fotografias e degradés: ficheiro, impressão, material e cor da peça participam no resultado. Avalie a definição real dos contornos e a diferença entre a imagem no ecrã e a amostra. Não existe reprodução «perfeita» garantida.\n\nNeste exemplo, reveja também o contorno cortado e a eventual área de material que acompanha a imagem. A extensão dessa área interessa para o toque, a flexibilidade e o aspeto. Aprove o acabamento na dimensão pretendida e não apenas numa pequena amostra de cor.'),
        ('Preparar a arte e escolher', 'Entregue um ficheiro nítido à dimensão final, identifique o fundo que deve desaparecer e confirme a necessidade de contorno de corte. Peça requisitos de resolução, perfil de cor, margens e espelhamento para o sistema concreto. A regra de espelhamento pode variar com o material. [trfilmes]\n\nSe houver elementos isolados, letras finas ou transparências, confirme como serão preparados e transferidos. Compare o desenho já aplicado, incluindo as zonas sem impressão que possam permanecer, antes de aprovar a solução.'),
        ('Vantagens e limitações', 'Uma imagem preparada digitalmente permite trabalhar a composição e rever variantes no ficheiro. Isso não elimina preparação, corte ou outras operações quando o sistema as exige. A vantagem prática depende do desenho e do fluxo documentado.\n\nA principal limitação da designação isolada é não permitir prever o toque, a opacidade, o recorte ou a compatibilidade. Preço, volume adequado, resistência e cuidados só podem ser discutidos com um sistema identificado e uma prova representativa.'),
    ],
    [
        ('Fundo ou contorno indesejado', 'Rever transparência do ficheiro, linha de corte, remoção do excedente e área efetivamente transferida no sistema selecionado.'),
        ('Imagem invertida ou elementos em falta', 'Confirmar orientação e sequência de preparação da referência usada. Filmes diferentes podem exigir fluxos diferentes. [trfilmes]'),
        ('Bordos levantados ou peça marcada', 'Conferir compatibilidade e contacto da prensa, incluindo costuras e acessórios. Pedir análise com a ficha do material e o registo de aplicação; não repetir uma receita de DTF por semelhança de nome.'),
    ],
    ['trdigital', 'trfilmes', 'traplicar'],
    ('Definição comercial pendente', 'Pedir à Nobrinde o fabricante e a referência que chama «Transfer Digital»; confirmar se envolve impressão e corte, toner ou outro sistema documentado.'),
)

BASE = guia(
    'transfer-digital-com-base',
    '«Base» precisa de uma definição do fornecedor. Saiba o que confirmar sobre opacidade, camadas, cobertura e toque antes de escolher para um tecido escuro.',
    ['Identificar o significado de base', 'Confirmar a construção do transfer', 'Preparar e aplicar segundo essa referência', 'Comparar opacidade e toque numa prova'],
    [
        ('Uma designação ainda por definir', 'Mesmo a expressão «Transfer digital com base branca» exige uma ficha que identifique a construção. Não está confirmado se a Nobrinde se refere a tinta branca sob CMYK, a um material branco imprimível ou a outro sistema. Por isso, este guia não atribui composição nem sequência de fabrico à designação.\n\nA informação abaixo distingue exemplos documentados e perguntas de escolha. Não confirma que uma camada branca seja o significado comercial pretendido.'),
        ('Como pode funcionar uma camada de opacidade', 'A FOREVER documenta um exemplo específico, Laser-Dark (No-Cut): imprime-se o motivo em A-Foil, prensa-se com B-Paper e, ao separar, o revestimento branco do B-Paper passa para as áreas com toner. A imagem preparada é depois transferida para o artigo. O fabricante associa esse revestimento à opacidade e à vivacidade das cores sobre tecidos escuros. [trbase]\n\nEste exemplo não prova que «com Base» signifique tinta branca impressa sob CMYK na Nobrinde. A Siser descreve ainda filmes brancos imprimíveis, uma construção diferente. Se o fornecedor confirmar uma camada branca sob a imagem CMYK, a função de opacidade deverá ser explicada na ficha desse sistema, com as suas condições. [trfilmes]'),
        ('Materiais e artigos a avaliar', 'Uma peça escura não é, por si só, indicação suficiente. Registe a composição de t-shirts, sweatshirts ou sacos candidatos, o acabamento, a elasticidade e a posição. Peça compatibilidade escrita para o conjunto artigo/transfer.\n\nNão importe para uma modalidade indefinida a lista de materiais de Laser-Dark ou de um filme Siser. Mesmo que a base ajude a ocultar o fundo, isso não confirma aderência, tolerância ao calor ou bloqueio de migração de corantes.'),
        ('Cores, pormenor, toque e cobertura', 'Uma camada branca de opacidade, quando confirmada para o sistema, reduz a influência visual do fundo escuro; o efeito documentado pela FOREVER aplica-se ao seu revestimento. [trbase] A correspondência de cor deve ser aprovada numa prova sobre a cor real da peça.\n\nPeça para observar bordos, pormenores e zonas vazias. Se existirem camadas sobrepostas, confirme alinhamento e se a base fica visível fora da imagem. A construção e a área coberta precisam de avaliação tátil: «com base» não permite concluir que o resultado é sempre mais espesso, mais rígido ou mais resistente.'),
        ('Arte e critérios de escolha', 'Antes de fechar a arte, obtenha a definição de base e a responsabilidade pela sua preparação. Se for uma camada branca sob CMYK, peça uma prova dessa separação, dos recuos nos contornos e das zonas que devem ficar sem branco. Se for um material branco recortado, confirme o perímetro que permanece.\n\nAprove letras pequenas, transparências e espaços negativos na escala final. Uma maquete em fundo branco não permite avaliar a opacidade sobre uma peça escura; use uma amostra representativa.'),
        ('Vantagens possíveis e limites de decisão', 'A opacidade pode ser útil quando o fundo interfere com a imagem, se esse for o papel confirmado da base. Não equivale a uma garantia de bloquear migração, melhorar lavagem ou aderir a qualquer tecido.\n\nEnquanto faltar a referência, não é rigoroso comparar custo, durabilidade ou quantidades com as outras modalidades. A decisão exige conhecer o sistema, a preparação, o aspeto e o toque que a amostra realmente apresenta.'),
    ],
    [
        ('Halo branco ou perda de detalhe', 'Se houver uma separação branca, pedir revisão da relação entre base e imagem. Se for material recortado, rever o contorno. Primeiro identificar qual destas construções existe.'),
        ('Imagem pouco opaca', 'Comparar com a prova aprovada na mesma cor de tecido e pedir confirmação da construção. Não assumir que acrescentar uma camada resolve o problema sem alterar o resultado.'),
        ('Alteração de cor ou toque inesperado', 'Registar quando surge a alteração, composição e acabamento da peça, consumíveis e aplicação. Confirmar se o sistema contempla o comportamento observado; branco opaco não demonstra uma barreira à migração.'),
    ],
    ['trbase', 'trfilmes', 'traplicar'],
    ('O que é a base?', 'Confirmar fabricante, referência, composição documentada e função: branco de opacidade sob CMYK, material branco imprimível ou outra construção. Identificar como é criada e quais as zonas que permanecem na peça.'),
)

DTF = guia(
    'dtf',
    'Impressão em filme, aplicação de adesivo termofusível e transferência por prensa. Conheça a sequência e as verificações para o tecido e o acabamento.',
    ['Imprimir a imagem no filme DTF', 'Aplicar o pó termofusível', 'Preparar termicamente o adesivo', 'Transferir na prensa e retirar o filme conforme a ficha'],
    [
        ('O que é DTF', 'DTF significa Direct to Film: a imagem é impressa num filme intermédio e posteriormente transferida para o tecido. Não é impressão direta no artigo. A Mimaki descreve este processo para a TxF150-75 e identifica tintas CMYK e branca no seu sistema. [trmimaki]'),
        ('Sequência documentada', 'Na descrição da Mimaki, imprime-se no filme DTF, aplica-se pó adesivo termofusível e aquece-se/seca-se o conjunto para formar a camada transferível. Segue-se a transferência para o tecido com prensa térmica. A preparação térmica do adesivo, frequentemente designada cura, deve seguir o conjunto de consumíveis escolhido. [trmimaki]\n\nConfirmar com o fabricante o filme, o pó, as tintas, a preparação térmica e a remoção do suporte. Esta sequência não fornece temperatura, tempo, pressão, modo de destaque nem cuidados de lavagem universais.'),
        ('Tecidos e artigos a considerar', 'A Mimaki apresenta t-shirts e vestuário desportivo entre as aplicações do equipamento. Isso não significa que o sistema sirva para qualquer têxtil. [trmimaki]\n\nPara vestuário ou painéis de sacos, registe composição, cor, elasticidade e revestimentos e peça uma prova. Avalie o acesso à zona e a tolerância do artigo e dos seus acessórios à aplicação. Tecidos tratados, peças com costuras salientes e fundos suscetíveis de alterar a cor exigem confirmação específica; uma aprovação noutro tecido não basta.'),
        ('Cores, definição e toque', 'O sistema Mimaki citado combina CMYK e branco. [trmimaki] A imagem final deve ser avaliada sobre o tecido escolhido: verifique cores, contornos, detalhes isolados e eventuais bordos brancos. Não prometa equivalência perfeita a uma fotografia ou à cor do ecrã.\n\nO motivo transferido constitui uma camada na superfície. Peça uma prova de toque e flexibilidade à escala final, incluindo áreas cheias e pormenores. Tinta, adesivo, preparação, área coberta e tecido fazem parte dessa avaliação; «DTF» não determina um único acabamento.'),
        ('Preparar a arte e decidir', 'Forneça o original com dimensão final, posição e fundo pretendido. Confirme resolução, gestão de cor, orientação de impressão e preparação do branco com quem produz o filme. Reveja linhas finas, vazios e transparências; peça prova quando pormenor, cor ou conforto forem decisivos.\n\nA escolha deve considerar o conjunto desenho/artigo, as posições e o volume. Compare a amostra com alternativas e obtenha uma proposta para o trabalho concreto, sem presumir que DTF é sempre mais barato ou que dispensa preparação.'),
        ('Vantagens e limitações', 'A impressão no filme separa a criação do motivo da aplicação ao tecido. O processo pode ser considerado quando essa separação se ajusta ao trabalho, desde que armazenamento e utilização do transfer sejam confirmados.\n\nA aderência e o comportamento no uso dependem da composição e do acabamento do artigo, filme, pó, tinta, processo e cuidados. Aprove uma peça personalizada e critérios de ensaio. Nem a presença de tinta branca nem uma imagem visualmente correta garantem resistência à lavagem ou compatibilidade universal.'),
    ],
    [
        ('Bordos a levantar ou transferência incompleta', 'Pedir revisão da compatibilidade e do registo de preparação térmica, prensagem e destaque. Comparar os consumíveis usados com os aprovados, sem corrigir por tentativa com uma regra de outro transfer.'),
        ('Resíduos em zonas sem desenho', 'Pedir verificação da preparação do filme e da aplicação do adesivo, preservando uma amostra antes de prensar. A inspeção orienta a análise; não demonstra uma causa única.'),
        ('Falhas de cor ou contornos brancos', 'Comparar a imagem no filme com a arte e rever impressão, branco e preparação do ficheiro. A Mimaki documenta mecanismos de controlo de bicos e circulação de branco no seu equipamento; isso não elimina a necessidade de verificar a impressão. [trmimaki]'),
        ('Mudança de cor, fissuras ou falhas após lavagem', 'Registar tecido, lote de consumíveis, parâmetros e cuidados aplicados. Solicitar análise e ensaio representativo; não prometer um número de lavagens sem validação do conjunto.'),
    ],
    ['trmimaki', 'traplicar'],
    ('Conjunto DTF', 'Identificar impressora, tinta, filme, pó e preparação térmica compatíveis. Obter as instruções de prensagem e destaque para esse conjunto.'),
)

ENTRADA = {
    'id': 'transfers', 'sec': 'tecnicas', 'tipo': 'tecnica', 'titulo': 'Transfers',
    'resumo': 'Um nome comum para processos diferentes. Compare como o motivo é preparado, o papel do suporte intermédio e o que confirmar antes de aplicar ao artigo.',
    'data_revisao': '2026-09-30', 'data_revisao_texto': '30 de setembro de 2026',
    'transfer': True, 'ids_seccoes': ['familia', 'modalidades', 'escolher'],
    'seccoes': [
        ('O que têm em comum', 'Nestes processos, o motivo é preparado num suporte intermédio antes de ser aplicado ao artigo. Os exemplos documentados usam calor e pressão na transferência, mas diferem na impressão, no suporte e no adesivo. A existência de uma prensa não identifica a técnica. [trgoof] [trmimaki]\n\nAs quatro entradas abaixo ajudam a comparar. «Transfer Digital» é uma designação ampla e «com Base» descreve uma característica por validar; não são necessariamente famílias independentes de DTF.'),
        ('Quatro entradas para compreender e comparar', 'Comece pelo processo ou pela designação que recebeu. Cada guia distingue o que está documentado das informações que precisam de confirmação para a referência concreta.'),
        ('Como escolher sem depender apenas do nome', 'Reúna composição, cor, revestimento, dimensão e posição do desenho. Peça a identificação do sistema, uma amostra e instruções de aplicação e lavagem. Compare definição, cobertura, toque e comportamento no uso previsto.\n\nNão existe uma classificação universal por custo, durabilidade ou quantidade. A comparação depende do sistema, arte, tecido, parâmetros e volume. As fichas da Transfer Express mostram que as condições de aplicação variam por produto. [traplicar]'),
    ],
    'problemas': [], 'fontes': ['trgoof', 'trmimaki', 'traplicar'],
    'relacionados': ['bordado', 'serigrafia', 'tecnica-sublimacao', 'dtf-e-prensas-termicas'],
    'ancoras': ['tecnicas/index.html#textil'], 'tags': 'transfer transfers transferência serigráfico digital base branca DTF',
}

TRANSFERS = [ENTRADA, SERIGRAFICO, DIGITAL, BASE, DTF]
