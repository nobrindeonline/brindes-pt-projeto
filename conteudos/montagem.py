"""União e acabamento: fontes consultadas e imagens observadas em 7-10-2026."""

HUB_ID = 'costura-argolagem-e-encadernacao'
FONTES_MONTAGEM = {
    'montschmetz': ('SCHMETZ — Sewing Focus: Luggage, Bags, Travel and Leather Accessories', 'https://www.schmetz.com/mm/media/en/web/7_tochtergesellschaften/bilder_18/schmetz/pdfs_4/sewing_focus/SewingFocus_23_3075-26_Gepaeck_D.pdf'),
    'montpontos': ('Coats — Basic Stitch Types', 'https://www.coats.com/en-us/info-hub/Basic-stitch-types/'),
    'montcosturas': ('Coats — Seam Types', 'https://www.coats.com/en-us/info-hub/seam-types/'),
    'montespiral': ('MyBinding — How to Use a Coil Binding Machine', 'https://www.mybinding.com/a/knowledge-base/coil-binding/how-to-use-a-coil-binding-machine'),
    'montsappi': ('Sappi — The Standard 6: Binding', 'https://cdn-s3.sappi.com/s3fs-public/sappietc/sappi_standard06.pdf'),
    'montadesiva': ('HEIDELBERG — C.P. Bourg Perfect Binder', 'https://www.heidelberg.com/global/en/print_and_packaging/products/digital_printing/postpress_for_digital_printing/cp_bourg_perfect_binder.jsp'),
}
BASE_IMAGENS = 'assets/tecnicas/Costura_Argolagem_Encardenacao/'
IMAGENS_MONTAGEM = {
    'tecnica-costura-industrial': ('Costura_Industrial/unnamed (37).jpg', 474, 266,
        'Agulha e calcador de uma máquina junto a tecido com linhas marcadas, guiado por uma mão.',
        'Pormenor da costura à máquina num tecido. A imagem não permite identificar a composição nem a resistência da união.'),
    'argolagem': ('Argolagem/unnamed (41).jpg', 474, 487,
        'Equipamento de bancada com alavanca, espirais pretas e alicate de cabos vermelhos.',
        'Equipamento com espirais contínuas e alicate. O material dos consumíveis e o modelo da máquina não são confirmados pela fotografia.'),
    'encadernacao': ('Encardenacao/unnamed (45).jpg', 474, 474,
        'Mãos a trabalhar com linha na lombada de um conjunto de cadernos de papel sobre uma base verde.',
        'Trabalho manual com linha na lombada de cadernos de papel. Ilustra encadernação costurada, não encadernação adesiva industrial.'),
}

def artigo(id, titulo, resumo, seccoes, fontes, relacionados, tags):
    return dict(id=id, sec='tecnicas', tipo='tecnica', titulo=titulo, resumo=resumo,
        montagem=True, data_revisao='2026-10-07', data_revisao_texto='7 de outubro de 2026',
        ids_seccoes=[s[0] for s in seccoes], seccoes=[(s[1], s[2]) for s in seccoes],
        fontes=fontes, problemas=[], relacionados=relacionados,
        ancoras=['tecnicas/index.html#montagem'], tags=tags)

HUB = artigo(HUB_ID, 'Costura, Argolagem e Encadernação',
    'Três caminhos para unir, montar ou finalizar um produto. Comece pelo objeto, pelos materiais e pela forma como será utilizado.', [
    ('relacao', 'O que liga estes processos?',
     'A costura industrial une ou reforça componentes têxteis com pontos e linhas. [montcosturas] A argolagem prende folhas e capas por furos, usando espiral ou argolas compatíveis com o sistema. A encadernação reúne e fixa folhas para formar um conjunto, por diferentes métodos. [montsappi]\n\nPartilham um objetivo de montagem ou acabamento, mas não são versões do mesmo processo nem soluções intercambiáveis. A argolagem é uma família de encadernação mecânica; a costura de um saco e a costura de um livro têm contextos distintos.'),
    ('escolher', 'Comece pelo resultado pretendido',
     'Para um saco ou uma mochila, identifique os componentes e as zonas de união. Para um bloco ou agenda, descreva como pretende virar as folhas. Para um livro, catálogo ou dossier, indique a organização do conteúdo, a capa e a necessidade de substituir páginas. Estas perguntas orientam a escolha; não confirmam que uma solução esteja disponível para qualquer produto.\n\nOs guias apresentam princípios e critérios de avaliação. Confirme com a Nobrinde os processos disponíveis, materiais, formatos e condições de cada trabalho.')],
    ['montcosturas', 'montsappi'], ['montagem-e-acabamentos', 'como-avaliar-uma-maquete'],
    'costura industrial argolagem encadernação montagem acabamento união espiral livros sacos')

COSTURA = artigo('tecnica-costura-industrial', 'Costura Industrial',
    'Como as costuras participam na montagem de sacos, mochilas e acessórios, e o que definir antes de aprovar uma peça.', [
    ('o-que-e', 'Unir e construir a peça',
     'Uma costura mantém camadas de material unidas por pontos. Numa peça montada, essa união pode suportar esforços e participar na sua estrutura. A construção da costura, o ponto e a linha devem corresponder à aplicação. [montcosturas]\n\nAqui tratamos da construção de peças. O bordado tem outro objetivo: aplicar motivos decorativos por pontos. Um logótipo bordado não substitui a avaliação das costuras que montam o artigo.'),
    ('processo', 'Como se forma a costura',
     'A agulha atravessa o tecido levando a linha. Ao subir, forma-se uma laçada, recolhida pelo mecanismo da máquina; conforme o ponto, as linhas entrelaçam-se de modos diferentes. A repetição forma a sequência de pontos. [montpontos]\n\nPreparar componentes → posicionar camadas → executar as uniões previstas → acabar e rever. Este percurso simplificado serve para compreender o trabalho, não para regular uma máquina.'),
    ('aplicacoes', 'Sacos, mochilas e reforços',
     'A SCHMETZ documenta a costura de malas, sacos, mochilas e acessórios, incluindo materiais têxteis, revestidos e pele. A agulha deve ser escolhida em função do material, número de camadas e combinação usada. [montschmetz]\n\nNum pedido de saco, assinale a união dos painéis, a posição das alças, os bolsos e as zonas que pretende reforçar. Numa mochila, descreva o conteúdo a transportar e os pontos de apoio. São exemplos de especificação a discutir, não garantias de carga ou de execução local.'),
    ('escolha', 'Ponto, linha, agulha e construção',
     'O tipo de ponto descreve a formação das linhas; a construção da costura descreve como os componentes se juntam. Por exemplo, camadas sobrepostas podem ser unidas junto ao bordo com uma ou mais filas de pontos. [montcosturas]\n\nA SCHMETZ relaciona a qualidade com o conjunto material, agulha, linha e regulação. Espessuras acumuladas e revestimentos exigem atenção: podem surgir falhas de ponto, quebra de linha ou danos no material. [montschmetz] Não existe nesta página uma agulha, linha ou densidade de pontos universal.'),
    ('limites', 'Vantagens, limitações e amostra',
     'A costura permite reunir componentes e definir o acabamento das uniões. Uma fita dobrada sobre os bordos, por exemplo, pode ser cosida para os rematar. [montcosturas]\n\nPeça uma amostra com os materiais finais. Observe alinhamento, regularidade, remates, aspeto interior e exterior e acesso aos bolsos. Peça avaliação das zonas espessas e das ligações às alças. A aparência, por si só, não comprova resistência: se houver requisitos de carga ou uso intensivo, solicite critérios e ensaios adequados ao produto.'),
    ('preparar', 'O que entregar e confirmar',
     'Entregue desenho com dimensões finais, identificação dos componentes, materiais e revestimentos, posição das uniões, alças, fechos e personalização. Indique que costuras ficam visíveis e o aspeto pretendido da linha.\n\nCombine as margens de montagem e tolerâncias com a produção. Antes de aprovar, confirme a sequência entre personalização e montagem, os cuidados do artigo completo e as diferenças aceitáveis face à amostra.'),
    ('perguntas', 'Perguntas frequentes',
     'Mais pontos significam sempre maior resistência? Não escolha apenas por esse número: peça validação da construção completa para a utilização indicada.\n\nPosso mudar o tecido mantendo o desenho? Submeta novamente material, camadas e acabamento à produção; a validação anterior não deve ser transferida automaticamente.\n\nÉ possível bordar depois de montar? Confirme o acesso à área e a sequência de trabalho antes de fechar o modelo; consulte também o guia de Bordado.')],
    ['montcosturas', 'montpontos', 'montschmetz'],
    [HUB_ID, 'costura-industrial', 'bordado', 'sacos-e-mochilas', 'materiais-texteis', 'pele-e-imitacao-de-pele'],
    'costura industrial coser agulha linha ponto camadas alças reforços sacos mochilas')

ARGOLAGEM = artigo('argolagem', 'Argolagem',
    'Encadernação mecânica por espiral ou argolas: preparação das folhas, perfuração e escolha de um sistema compatível.', [
    ('o-que-e', 'O sistema descrito neste guia',
     'Neste projeto, «argolagem» designa a encadernação mecânica por argolas ou espiral. O percurso explicado abaixo é o da espiral contínua, que atravessa sucessivamente os furos junto à margem. Não descreve o mecanismo de argolas de abrir de um dossier. [montsappi]\n\nA fotografia mostra espirais contínuas, mas não permite confirmar a sua composição. O exemplo técnico consultado na MyBinding descreve espiral plástica. Não se atribui esse material à imagem apenas pela aparência. [montespiral]'),
    ('processo', 'Das folhas soltas ao conjunto',
     'Organizar folhas e capas → perfurar com alinhamento → inserir a espiral → acabar as extremidades → conferir. No sistema descrito pela MyBinding, o passo da perfuração tem de corresponder à espiral, que avança por rotação. As extremidades recebem acabamento para impedir a saída do conjunto. [montespiral]\n\nO tamanho do consumível e a capacidade de perfuração devem ser confirmados para as folhas e capas escolhidas. Este resumo não substitui o manual do equipamento.'),
    ('sistemas', 'Espiral contínua e argola dupla',
     'Uma espiral contínua não é igual à argola dupla metálica, também conhecida por Wire-O: esta utiliza laçadas pré-formadas. São sistemas distintos e não consumíveis intercambiáveis. [montsappi]\n\nNão há uma imagem de argola dupla selecionada neste guia. As outras fotografias locais com pentes de plástico não ilustram o processo por espiral e foram deixadas de fora.'),
    ('aplicacoes', 'Manuseamento e aplicações',
     'A Sappi documenta a espiral em manuais e apresentações, permitindo voltar as páginas sobre o próprio conjunto. [montsappi]\n\nUm bloco de formação ou uma agenda são propostas editoriais para avaliar com a produção: experimente a escrita, o virar das folhas, o transporte e a posição do elemento de união. A abertura efetiva depende do conjunto; peça uma amostra com as capas finais antes de prometer um comportamento específico.'),
    ('limites', 'O que condiciona a escolha',
     'Confirme formato, espessura total, papel, capas, padrão de furos e consumível. A MyBinding recomenda verificar a passagem da espiral por todas as folhas, o acabamento das pontas e a abertura do documento. [montespiral]\n\nA perfuração ocupa uma margem do trabalho. Peça avaliação de separadores e folhas de formatos diferentes. Não deduza a capacidade da máquina pela fotografia nem escolha uma espiral apenas pela cor ou pelo diâmetro aparente.'),
    ('preparar', 'Preparar páginas e grafismo',
     'Envie o documento pela ordem de leitura, incluindo páginas em branco intencionais, capa, contracapa e separadores identificados. Indique o lado da união e o sentido de abertura. Peça o gabarito da perfuração antes de fechar o grafismo.\n\nReserve a margem acordada para os furos e afaste texto, logótipos e números dessa zona. Reveja frente e verso e confirme qualquer imagem que atravesse duas páginas. Não são indicados valores universais de margem.'),
    ('perguntas', 'Perguntas frequentes',
     'Posso usar qualquer espiral numa perfuração existente? Não presuma compatibilidade: confirme o sistema e os consumíveis.\n\nPosso acrescentar páginas mais tarde? Indique essa necessidade no pedido; não trate uma espiral acabada como um mecanismo de dossier que abre.\n\nUma capa mais espessa mantém o mesmo resultado? Peça nova avaliação do conjunto e uma amostra; confirme perfuração, abertura e consumível.')],
    ['montespiral', 'montsappi'], [HUB_ID, 'encadernacao', 'encadernacao-e-argolagem', 'artigos-de-escritorio', 'papel-e-cartao', 'como-avaliar-uma-maquete'],
    'argolagem espiral coil wire-o argola dupla perfuração bloco agenda folhas capas')

ENCADERNACAO = artigo('encadernacao', 'Encadernação',
    'Reunir folhas e escolher como as fixar: métodos, capa, abertura e preparação de livros e documentos.', [
    ('o-que-e', 'Uma família de processos',
     'Encadernar é reunir e fixar folhas num produto manuseável. Pode envolver adesivo, linha ou sistemas mecânicos; não significa apenas colar uma lombada ou aplicar capa dura. A argolagem é uma das possibilidades, tratada num guia próprio. [montsappi]'),
    ('processo', 'Preparar, reunir e finalizar',
     'Comece por definir o método com a produção, antes de fechar os ficheiros. Confirme a sequência das páginas, a divisão em cadernos quando aplicável, o papel e a capa. Peça uma prova completa para verificar a leitura.\n\nNa solução adesiva C.P. Bourg apresentada pela HEIDELBERG, o bloco é fixado e a lombada preparada por fresagem e rugosidade antes da aplicação do adesivo e da capa. O corte final e a reunião de folhas podem integrar módulos próprios. Esta configuração é um exemplo industrial, não a descrição de todos os métodos. [montadesiva]'),
    ('metodos', 'Adesiva, costurada ou mecânica',
     'Na encadernação adesiva, o adesivo participa na fixação do bloco à capa. A HEIDELBERG apresenta opções PUR e EVA no sistema consultado. A escolha deve ser validada para o trabalho concreto, sem declarar uma solução sempre superior. [montadesiva]\n\nNa encadernação costurada em cadernos, a linha une conjuntos de folhas dobradas; podem seguir-se operações de colagem e aplicação da capa. A fotografia mostra trabalho manual com linha, não uma linha industrial. [montsappi]\n\nSe pretende união por furos e espiral, consulte Argolagem. A decisão sobre a capa é separada da decisão sobre como fixar o miolo.'),
    ('aplicacoes', 'Livros, catálogos e documentos',
     'A solução adesiva consultada é apresentada para livros de capa flexível, manuais e relatórios. [montadesiva]\n\nPara um catálogo, defina a frequência de consulta e se precisa de apresentar imagens junto à lombada. Para um dossier com conteúdo atualizável, explique a necessidade de retirar e acrescentar folhas: peça avaliação de um sistema adequado em vez de assumir que um bloco colado satisfaz esse uso. Estes são critérios editoriais de encomenda, não serviços confirmados da Nobrinde.'),
    ('escolha', 'Vantagens e limites a comparar',
     'Compare uma amostra pela leitura junto à margem interior, facilidade de abrir, comportamento da capa, manuseamento e acabamento. Uma lombada com bom aspeto não prova a qualidade da fixação.\n\nIndique número de páginas, tipo e espessura do papel, formato, capa e utilização prevista. Pergunte que método se adapta ao conjunto, como deve ser manuseado e que critérios serão usados na aprovação. Não escolha apenas pela expressão «capa dura» ou pelo nome do adesivo.'),
    ('preparar', 'Preparar os ficheiros',
     'Entregue páginas na ordem de leitura, identifique brancas intencionais e separe miolo e capa conforme as instruções recebidas. Confirme se a imposição — a distribuição técnica das páginas para impressão e dobra — será feita pela produção.\n\nPeça o gabarito da capa e a medida de lombada calculada para o conjunto final. Acorde margens interiores, sangrias e posição de elementos que atravessam duas páginas. Se alterar papel ou paginação, peça nova validação antes de reutilizar a capa.'),
    ('perguntas', 'Perguntas frequentes',
     'Capa dura quer dizer miolo costurado? Não conclua o método pela capa: peça a descrição da construção.\n\nO livro vai abrir completamente na horizontal? Confirme essa necessidade através de uma amostra do método e materiais escolhidos.\n\nPosso mudar o número de páginas depois de aprovar? Peça revisão do miolo, lombada, capa e orçamento antes de produzir.\n\nA fotografia mostra o serviço da Nobrinde? Não. É uma imagem local ilustrativa; equipamento, método e disponibilidade precisam de confirmação interna.')],
    ['montsappi', 'montadesiva'], [HUB_ID, 'argolagem', 'encadernacao-e-argolagem', 'papel-e-cartao', 'artigos-de-escritorio', 'como-avaliar-uma-maquete'],
    'encadernação encadernacao adesiva colagem costurada livro catálogo miolo lombada capa PUR EVA')

MONTAGEM = [HUB, COSTURA, ARGOLAGEM, ENCADERNACAO]
