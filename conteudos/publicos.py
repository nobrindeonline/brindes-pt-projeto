"""Guias editoriais por destinatário, ocasião e contexto de utilização."""

DATA_REVISAO_PUBLICOS = '2026-10-14'

FONTES_PUBLICOS = {
    'dia-educacao': {
        'titulo': 'Dia Internacional da Educação',
        'entidade': 'Nações Unidas',
        'url': 'https://www.un.org/en/observances/education-day',
        'data_consulta': '2026-10-14',
        'ambito': 'A Assembleia Geral das Nações Unidas proclamou 24 de janeiro como Dia Internacional da Educação.',
    },
    'dia-desporto': {
        'titulo': 'Dia Internacional do Desporto para o Desenvolvimento e a Paz',
        'entidade': 'Nações Unidas',
        'url': 'https://www.un.org/en/observances/sport-day',
        'data_consulta': '2026-10-14',
        'ambito': 'A página identifica 6 de abril como Dia Internacional do Desporto para o Desenvolvimento e a Paz.',
    },
    'dia-turismo': {
        'titulo': 'Dia Mundial do Turismo',
        'entidade': 'ONU Turismo',
        'url': 'https://www.untourism.int/world-tourism-day-2026',
        'data_consulta': '2026-10-14',
        'ambito': 'Página oficial da celebração de 2026; a referência à data serve apenas para localizar uma ocasião possível.',
    },
    'dia-voluntariado': {
        'titulo': 'Dia Internacional dos Voluntários',
        'entidade': 'Nações Unidas',
        'url': 'https://www.un.org/en/observances/volunteer-day',
        'data_consulta': '2026-10-14',
        'ambito': 'A página das Nações Unidas refere a celebração anual do Dia Internacional dos Voluntários a 5 de dezembro.',
    },
}


def imagem(url, alt, width, height):
    return dict(url='assets/para_quem/visuais/' + url, alt=alt, width=width, height=height)


def imagem_contexto(url, alt, legenda, width, height):
    return dict(**imagem(url, alt, width, height), legenda=legenda)


def texto_lista_editorial(valor):
    valores = valor if isinstance(valor, list) else [valor]
    valores = [item[:1].lower() + item[1:] for item in valores]
    if len(valores) < 2:
        return valores[0]
    return ', '.join(valores[:-1]) + ' e ' + valores[-1]


def texto_destinatarios_editorial(valor):
    valores = valor if isinstance(valor, list) else [valor]
    formas = {
        'Cliente': 'a clientes',
        'Comunidade': 'à comunidade',
        'Comunidade educativa': 'à comunidade educativa',
        'Equipa responsável': 'à equipa responsável',
        'Organização': 'à organização',
        'Pessoa que avalia a proposta': 'a quem avalia a proposta',
        'Pessoa que prepara a proposta': 'a quem prepara a proposta',
    }
    destinatarios = [
        formas.get(item, 'a ' + item[:1].lower() + item[1:])
        for item in valores
    ]
    if len(destinatarios) < 2:
        return destinatarios[0]
    return ', '.join(destinatarios[:-1]) + ' e ' + destinatarios[-1]


def ocasiao(destinatario, ocasiao, local, epoca, objetivo):
    objetivo_editorial = objetivo.rstrip()
    if objetivo_editorial.endswith('.'):
        objetivo_editorial = objetivo_editorial[:-1]
    return dict(
        destinatário=destinatario,
        ocasião=ocasiao,
        local=local,
        época=epoca,
        objetivo=objetivo,
        texto_editorial=(
            'A ocasião destina-se '
            + texto_destinatarios_editorial(destinatario)
            + ' e pode decorrer em contextos como '
            + texto_lista_editorial(local)
            + '. O momento — '
            + epoca[:1].lower()
            + epoca[1:]
            + ' — ajuda a enquadrar o objetivo de '
            + objetivo_editorial[:1].lower()
            + objetivo_editorial[1:]
            + '.'
        ),
    )


def publico(
    id,
    titulo,
    resumo,
    destinatarios,
    ocasioes,
    familias_de_artigos,
    distribuicao,
    criterios,
    perguntas_frequentes,
    fontes=(),
    relacionados=(),
    etiquetas=(),
    ancora=None,
    fotografia=None,
    imagens_contexto=(),
):
    return dict(
        id=id,
        sec='publicos',
        tipo='publico',
        titulo=titulo,
        resumo=resumo,
        destinatário=destinatarios,
        ocasiões=ocasioes,
        famílias_de_artigos=familias_de_artigos,
        distribuição=distribuicao,
        critérios=criterios,
        perguntas_frequentes=perguntas_frequentes,
        fontes=list(fontes),
        relacionados=list(relacionados),
        etiquetas=list(etiquetas),
        imagem=fotografia,
        imagens_contexto=list(imagens_contexto),
        ancora=ancora or id,
        data_revisao=DATA_REVISAO_PUBLICOS,
        seccoes=[
            ('Destinatários e necessidades', ' '.join(item['necessidade'] for item in destinatarios)),
            ('Ocasiões, locais e épocas', ' '.join(item['objetivo'] for item in ocasioes)),
            ('Distribuição e critérios', ' '.join(distribuicao + criterios)),
        ],
        tags=' '.join(etiquetas),
    )


PUBLICOS = [
    publico(
        'empresas',
        'Empresas',
        'Ideias para acolhimento de equipas, reuniões, formação, visitas e encontros de trabalho.',
        [
            dict(destinatário='Novos colaboradores', necessidade='Podem precisar de informação de boas-vindas e de elementos úteis ao contexto de integração.'),
            dict(destinatário='Equipas e participantes', necessidade='Em reuniões e formação, considere quem participa, a duração e se a atividade envolve apontamentos ou materiais de apoio.'),
            dict(destinatário='Visitantes e clientes', necessidade='Uma lembrança deve corresponder ao motivo da visita e ao modo como será entregue, sem presumir que todas as pessoas querem o mesmo artigo.'),
        ],
        [
            ocasiao(['Novos colaboradores'], 'Integração de uma pessoa na equipa', 'Receção, local de trabalho ou sessão de acolhimento', 'Ao longo do ano, antes ou no momento de chegada', 'Facilitar uma receção organizada e identificar informação que a pessoa possa consultar.'),
            ocasiao(['Equipas', 'Formadores e participantes'], 'Reunião, formação ou encontro de equipa', 'Sala de reunião, espaço de formação ou local do encontro', 'Na data definida pela organização; encontros de fim de ano variam entre equipas', 'Apoiar a participação sem substituir o material necessário à atividade.'),
            ocasiao(['Visitantes', 'Clientes'], 'Visita, aniversário de equipa ou encontro institucional', 'Receção, instalações ou espaço de evento', 'Conforme a agenda da organização; não existe uma época universal', 'Assinalar o contexto da visita ou do encontro, quando uma oferta fizer sentido.'),
        ],
        [
            dict(destinatário='Novos colaboradores', objetivo='Acolhimento e consulta', famílias=['Material de escrita', 'Cadernos e material de organização', 'Sacos para reunir informação']),
            dict(destinatário='Equipas e participantes', objetivo='Reuniões e formação', famílias=['Material de escrita', 'Cadernos', 'Artigos para identificação da equipa']),
            dict(destinatário='Visitantes e clientes', objetivo='Lembrança de visita ou encontro', famílias=['Sacos', 'Têxteis', 'Artigos de hidratação']),
        ],
        [
            'Prepare lotes por equipa ou sessão e identifique claramente qualquer material que não seja para distribuição geral.',
            'Se houver nomes, tamanhos ou versões diferentes, separe-os antes da entrega e defina como corrigir uma troca.',
            'Num encontro de fim de ano, confirme a data, os destinatários e o local concretos; não trate a ocasião como uma recomendação automática de oferta.',
        ],
        [
            'Quem recebe: equipa inteira, participantes, visitantes ou um grupo específico?',
            'Que necessidade concreta pretende apoiar e durante quanto tempo será usado o artigo?',
            'Como será transportado, guardado e distribuído no local?',
            'Que mensagem, identidade visual, quantidade e variantes precisam de aprovação?',
            'As famílias de artigos são possibilidades editoriais; confirme sempre a adequação, a personalização e as condições da opção concreta.',
        ],
        [
            dict(pergunta='É necessário preparar a mesma oferta para todas as pessoas?', resposta='Não necessariamente. Defina primeiro os destinatários e a ocasião; uma solução comum só é adequada se corresponder às necessidades do grupo.'),
            dict(pergunta='Os encontros de fim de ano têm uma data fixa?', resposta='Não. A data e o formato dependem da organização e da equipa; confirme a agenda antes de planear uma distribuição.'),
        ],
        relacionados=[
            dict(titulo='Como preparar um logótipo para personalização', url='guias/como-preparar-um-logotipo.html'),
            dict(titulo='Como escolher a técnica', url='guias/como-escolher-a-tecnica.html'),
            dict(titulo='Materiais', url='materiais/index.html'),
        ],
        etiquetas=['integração de colaboradores', 'reuniões', 'formação', 'visitas', 'equipas'],
        imagens_contexto=[
            imagem_contexto('empresas-organizacao.jpg', 'Dois instrumentos de escrita dentro de uma caixa aberta de cartão.', 'Para reuniões e formação, vale a pena planear o que os participantes devem encontrar à chegada.', 300, 301),
            imagem_contexto('empresas-distribuicao.jpg', 'Saco de tecido claro apresentado isoladamente sobre fundo branco.', 'A forma como os materiais são reunidos e entregues também faz parte da preparação de uma receção.', 300, 301),
        ],
        fotografia=imagem('empresas.jpg', 'Cadernos escuros e canetas dispostos em filas sobre uma mesa.', 500, 500),
    ),
    publico(
        'camaras-municipais',
        'Câmaras municipais',
        'Ideias para iniciativas culturais e desportivas, feiras locais, informação pública e receção de visitantes.',
        [
            dict(destinatário='Participantes e famílias', necessidade='Podem precisar de informação clara sobre a iniciativa e de uma forma simples de a levar consigo.'),
            dict(destinatário='Voluntários e equipas organizadoras', necessidade='Podem beneficiar de identificação funcional e de uma distribuição coordenada com as tarefas do evento.'),
            dict(destinatário='Visitantes', necessidade='Considere a língua, o contexto local e a facilidade de transporte, sem presumir as necessidades de cada pessoa.'),
        ],
        [
            ocasiao(['Participantes', 'Famílias'], 'Atividade cultural, desportiva ou familiar', 'Biblioteca, equipamento cultural, espaço público ou recinto desportivo', 'Datas e programação dependem do município e da iniciativa; confirme a agenda local', 'Apoiar a participação ou disponibilizar informação relevante para a atividade.'),
            ocasiao(['Visitantes', 'Expositores', 'Organização'], 'Feira local ou receção de visitantes', 'Recinto da feira, posto de receção ou espaço municipal', 'Calendário definido localmente e sujeito a atualização', 'Orientar a participação e distinguir os materiais destinados a cada público.'),
            ocasiao(['Voluntários', 'Equipas organizadoras'], 'Ação de informação ou reconhecimento', 'Ponto de encontro, balcão de acolhimento ou local da ação', 'Conforme o calendário e as prioridades de cada iniciativa', 'Facilitar identificação, distribuição ou reconhecimento, conforme o objetivo escolhido.'),
        ],
        [
            dict(destinatário='Participantes e famílias', objetivo='Participação e informação', famílias=['Material de escrita', 'Sacos para documentos', 'Artigos para atividades']),
            dict(destinatário='Voluntários e organização', objetivo='Identificação e coordenação', famílias=['Têxteis identificativos', 'Artigos de identificação', 'Material de apoio à equipa']),
            dict(destinatário='Visitantes', objetivo='Receção e informação local', famílias=['Mapas ou material informativo', 'Sacos', 'Artigos de hidratação']),
        ],
        [
            'Separe materiais para participantes, voluntários e equipas organizadoras; a oferta ou identificação destinada a um grupo não deve ser presumida para os restantes.',
            'Defina um ponto de entrega, uma pessoa responsável e uma forma de gerir sobras ou entregas tardias.',
            'Nas festas e feiras locais, confirme datas, locais, acessos e programação junto da entidade organizadora: variam por município e por ano.',
        ],
        [
            'Qual é o objetivo público da iniciativa e quem é responsável pela distribuição?',
            'A mensagem é legível e adequada ao espaço, ao idioma e ao público previsto?',
            'Há variantes por equipa, atividade ou local que devam ser separadas?',
            'Como serão armazenados e transportados os materiais até ao ponto de entrega?',
            'As famílias indicadas são ideias para avaliar, não uma especificação nem uma recomendação institucional.',
        ],
        [
            dict(pergunta='As festas locais têm datas iguais em todos os municípios?', resposta='Não. Consulte o programa atualizado da câmara ou da entidade organizadora do local e do ano em causa.'),
            dict(pergunta='Devo preparar a mesma oferta para participantes e voluntários?', resposta='Não é obrigatório. Identifique necessidades e funções de cada grupo e decida separadamente se uma oferta ou material de apoio é pertinente.'),
        ],
        relacionados=[
            dict(titulo='Como avaliar uma maquete antes da produção', url='guias/como-avaliar-uma-maquete.html'),
            dict(titulo='Como escolher o material de um brinde', url='guias/como-escolher-o-material.html'),
            dict(titulo='Técnicas', url='tecnicas/index.html'),
        ],
        etiquetas=['municípios', 'iniciativas culturais', 'feiras locais', 'famílias', 'voluntariado'],
        ancora='municipios',
        imagens_contexto=[
            imagem_contexto('contexto-identificacao.jpg', 'Pulseiras de várias cores dispostas em grupos sobre fundo branco.', 'Em iniciativas com públicos diferentes, planeie quem recebe cada material e onde o levanta.', 300, 300),
        ],
        fotografia=imagem('camaras-municipais.jpg', 'Caixa aberta com uma medalha e um certificado sobre uma mesa.', 992, 661),
    ),
    publico(
        'escolas',
        'Escolas',
        'Ideias para alunos, docentes, famílias e equipas escolares, ajustadas à idade e à atividade concreta.',
        [
            dict(destinatário='Alunos', necessidade='A idade, a autonomia, a atividade e as instruções de utilização precisam de ser consideradas antes de escolher qualquer artigo.'),
            dict(destinatário='Docentes e equipas escolares', necessidade='Podem ter necessidades diferentes das dos alunos, como materiais de apoio, identificação ou organização.'),
            dict(destinatário='Famílias e visitantes', necessidade='Em dias abertos ou cerimónias, importa perceber se o material é informativo, participativo ou uma lembrança.'),
        ],
        [
            ocasiao(['Alunos', 'Docentes', 'Famílias'], 'Início do ano letivo', 'Escola, sala de aula ou sessão de acolhimento', 'Antes do início definido pela escola; datas e organização variam consoante o calendário e a instituição', 'Acolher ou orientar participantes sem pressupor que todos precisam do mesmo material.'),
            ocasiao(['Alunos', 'Famílias', 'Equipas escolares'], 'Dia aberto ou atividade escolar', 'Entrada, salas, pátio ou espaço da atividade', 'Ao longo do ano, segundo o calendário publicado pela escola', 'Apoiar a participação e distribuir materiais no local adequado.'),
            ocasiao(['Alunos', 'Docentes', 'Famílias'], 'Fim do ano letivo, encerramento ou cerimónia de conclusão', 'Escola ou espaço escolhido para a cerimónia', 'No encerramento do ano letivo ou percurso; data definida pela instituição', 'Assinalar a ocasião, distinguindo participantes, famílias e equipa.'),
            ocasiao(['Comunidade educativa'], 'Dia Internacional da Educação', 'Escola ou atividade educativa', '24 de janeiro, data assinalada pelas Nações Unidas [dia-educacao]', 'Ligar uma atividade ao tema da educação; a data não implica oferecer brindes.'),
        ],
        [
            dict(destinatário='Alunos', objetivo='Atividade e participação', famílias=['Material de escrita', 'Material de desenho', 'Sacos para atividades']),
            dict(destinatário='Docentes e equipas escolares', objetivo='Organização e apoio', famílias=['Cadernos', 'Material de escrita', 'Artigos de identificação']),
            dict(destinatário='Famílias e visitantes', objetivo='Informação e acolhimento', famílias=['Sacos para documentação', 'Material informativo', 'Artigos de identificação']),
        ],
        [
            'Organize a entrega por turma, idade, atividade ou papel; evite deixar materiais acessíveis sem supervisão quando a escola considere que isso não é adequado.',
            'Antes de selecionar algo para alunos, peça à escola que avalie a faixa etária, os componentes, as instruções e o contexto de utilização.',
            'Confirme as datas diretamente com a escola e consulte o calendário escolar aplicável; início, interrupções e conclusão não são universais.',
        ],
        [
            'Que idades e grupos vão receber o artigo? Há participantes que não devem receber determinada variante?',
            'A escola reviu instruções, componentes e condições de utilização previstas para a idade?',
            'O artigo é para uso dos alunos, apoio aos docentes ou entrega às famílias?',
            'Como será distribuído em sala, no pátio ou durante uma cerimónia?',
            'A família de artigos é apenas uma possibilidade a avaliar; não demonstra adequação, segurança ou conformidade para crianças.',
        ],
        [
            dict(pergunta='Um artigo destinado a adultos pode ser distribuído a alunos?', resposta='Não assuma essa adequação. A escola deve avaliar a idade, as instruções e o uso previsto antes de decidir.'),
            dict(pergunta='O início e o fim do ano letivo têm datas iguais em todas as escolas?', resposta='Não trate as datas como universais; confirme o calendário em vigor e a informação publicada pela escola.'),
            dict(pergunta='O Dia Internacional da Educação implica uma oferta?', resposta='Não. 24 de janeiro é uma data de sensibilização; uma atividade ou oferta só deve ser considerada se servir um objetivo educativo concreto.'),
        ],
        fontes=['dia-educacao'],
        relacionados=[
            dict(titulo='Como preparar um logótipo para personalização', url='guias/como-preparar-um-logotipo.html'),
            dict(titulo='Como escolher a técnica', url='guias/como-escolher-a-tecnica.html'),
            dict(titulo='Materiais', url='materiais/index.html'),
        ],
        etiquetas=['alunos', 'docentes', 'famílias', 'ano letivo', 'atividades escolares'],
        imagens_contexto=[
            imagem_contexto('escolas-atividade.jpg', 'Duas mochilas com desenhos a traço acompanhadas por lápis de cor.', 'Uma atividade escolar pode reunir materiais diferentes; considere as idades e a utilização prevista.', 300, 301),
            imagem_contexto('escolas-materiais.jpg', 'Conjuntos de material escolar em estojos transparentes, com régua e lápis.', 'A escolha deve acompanhar a atividade definida pela escola, sem presumir que uma opção serve todos os alunos.', 300, 301),
        ],
        fotografia=imagem('escolas.jpg', 'Lápis de cor alinhados, cada um com uma mensagem impressa.', 554, 554),
    ),
    publico(
        'clubes-desportivos',
        'Clubes desportivos',
        'Ideias para atletas, voluntários, participantes e adeptos, sem confundir lembranças com equipamento técnico.',
        [
            dict(destinatário='Atletas', necessidade='Podem receber material de acolhimento ou reconhecimento; o equipamento necessário à prática deve ser tratado separadamente.'),
            dict(destinatário='Voluntários e organização', necessidade='Podem precisar de identificação ligada às tarefas e aos pontos de apoio do evento.'),
            dict(destinatário='Participantes e adeptos', necessidade='A ocasião, a duração e a forma de entrega ajudam a decidir se uma lembrança tem utilidade.'),
        ],
        [
            ocasiao(['Atletas', 'Equipas técnicas'], 'Abertura ou encerramento da época', 'Instalações do clube ou local de treino', 'Calendário definido pelo clube e pela competição', 'Acolher participantes ou assinalar um momento da época.'),
            ocasiao(['Participantes', 'Voluntários', 'Adeptos'], 'Torneio, corrida ou convívio', 'Recinto, percurso, zona de partida ou espaço de encontro', 'Data e local variam por organização e edição', 'Apoiar a participação, a identificação ou o reconhecimento.'),
            ocasiao(['Participantes', 'Voluntários', 'Adeptos'], 'Dia Internacional do Desporto para o Desenvolvimento e a Paz', 'Clube, escola ou espaço da atividade', '6 de abril, data assinalada pelas Nações Unidas [dia-desporto]', 'Dar contexto a uma atividade desportiva; a data não é uma recomendação automática para distribuir brindes.'),
        ],
        [
            dict(destinatário='Atletas', objetivo='Acolhimento ou reconhecimento', famílias=['Artigos de identificação', 'Têxteis de representação', 'Artigos de reconhecimento']),
            dict(destinatário='Voluntários e organização', objetivo='Identificação funcional', famílias=['Têxteis identificativos', 'Artigos de identificação', 'Sacos para materiais da equipa']),
            dict(destinatário='Participantes e adeptos', objetivo='Participação e memória do evento', famílias=['Artigos de reconhecimento', 'Sacos', 'Artigos de hidratação']),
        ],
        [
            'Separe atletas, voluntários, participantes e público; a identificação de uma função não equivale a uma oferta para todo o recinto.',
            'Se houver nomes ou tamanhos, prepare uma lista de distribuição e um método para gerir alterações e substituições.',
            'Uma lembrança não substitui equipamento técnico desportivo nem confirma adequação à prática. Confirme essa distinção com o clube.',
            'Defina como transportar e entregar os materiais sem bloquear zonas de circulação, partida ou assistência.',
        ],
        [
            'A oferta é para atletas, voluntários, participantes ou adeptos?',
            'Está claramente separada do equipamento técnico necessário à modalidade?',
            'Como serão identificados nomes, equipas, tamanhos e quantidades?',
            'O ponto de entrega é compatível com o percurso e a organização da atividade?',
            'Os artigos de hidratação e os têxteis são apenas famílias possíveis; não se afirma qualquer característica ou adequação técnica.',
        ],
        [
            dict(pergunta='Uma lembrança do clube substitui equipamento de treino?', resposta='Não. Este guia trata de artigos promocionais ou de reconhecimento; o equipamento necessário à modalidade é uma decisão distinta.'),
            dict(pergunta='O Dia Internacional do Desporto é uma data de oferta?', resposta='Não. 6 de abril pode contextualizar uma atividade; uma oferta só deve ser considerada se corresponder a uma necessidade e a uma decisão do clube.'),
        ],
        fontes=['dia-desporto'],
        relacionados=[
            dict(titulo='Bordado', url='tecnicas/bordado.html'),
            dict(titulo='Serigrafia', url='tecnicas/serigrafia.html'),
            dict(titulo='Como escolher a técnica', url='guias/como-escolher-a-tecnica.html'),
            dict(titulo='Materiais', url='materiais/index.html'),
        ],
        etiquetas=['atletas', 'voluntários', 'torneios', 'corridas', 'adeptos'],
        ancora='clubes',
        imagens_contexto=[
            imagem_contexto('contexto-identificacao.jpg', 'Pulseiras de várias cores dispostas em grupos sobre fundo branco.', 'Em torneios ou corridas, distinga o que se destina a participantes, voluntários e organização.', 300, 300),
        ],
        fotografia=imagem('clubes-desportivos.jpg', 'Porta-chaves com uma bola de futebol em miniatura sobre fundo branco.', 447, 447),
    ),
    publico(
        'revendedores',
        'Revendedores',
        'Um método para transformar o contexto do destinatário em perguntas e comparações claras, sem pressupostos comerciais.',
        [
            dict(destinatário='Pessoa que prepara a proposta', necessidade='Precisa de recolher o contexto de utilização, os destinatários e as condições que ainda não estão confirmadas.'),
            dict(destinatário='Pessoa que avalia a proposta', necessidade='Precisa de distinguir possibilidades editoriais, dados confirmados e questões por esclarecer.'),
            dict(destinatário='Destinatários finais', necessidade='As necessidades variam com a ocasião, o local e a forma de distribuição da proposta.'),
        ],
        [
            ocasiao(['Pessoa que prepara a proposta', 'Cliente'], 'Recolha inicial do pedido', 'Reunião, chamada ou documento de requisitos', 'Antes de iniciar a comparação', 'Perceber quem recebe, quando, onde e com que objetivo.'),
            ocasiao(['Pessoa que avalia a proposta', 'Destinatários finais'], 'Comparação de famílias genéricas', 'Proposta ou sessão de avaliação', 'Conforme o calendário do projeto; não existe um prazo universal', 'Comparar utilidade, distribuição, personalização e pontos que ainda exigem confirmação.'),
            ocasiao(['Equipa responsável'], 'Preparação de uma repetição ou nova edição', 'Arquivo de versões e material de referência da própria organização', 'Antes de cada nova decisão; não presumir que as condições anteriores se mantêm', 'Identificar o que mudou e o que tem de ser reconfirmado.'),
        ],
        [
            dict(destinatário='Preparação da proposta', objetivo='Explorar opções sem fechar prematuramente uma escolha', famílias=['Material de escrita', 'Sacos', 'Têxteis', 'Artigos de hidratação']),
            dict(destinatário='Comparação', objetivo='Explicar diferenças relevantes para o contexto', famílias=['Cadernos e material de organização', 'Artigos para eventos', 'Artigos de identificação']),
        ],
        [
            'Use uma grelha curta: destinatário, ocasião, local, época, objetivo, família possível, personalização e questão por confirmar.',
            'Separe numa proposta aquilo que é uma possibilidade editorial do que foi confirmado por uma fonte atual.',
            'Não deduza preço, prazo, stock, quantidade mínima, margem, exclusividade ou compatibilidade a partir de uma família genérica.',
            'Ao reutilizar uma proposta, confirme novamente arte, quantidades, destinatários, local e condições aplicáveis.',
        ],
        [
            'Que informação sobre os destinatários está confirmada e o que continua por apurar?',
            'As opções estão descritas por família e finalidade, sem converter uma possibilidade numa promessa?',
            'A comparação separa factos documentados, sugestões editoriais e decisões comerciais?',
            'Que perguntas faltam sobre distribuição, variantes, personalização, data e local?',
        ],
        [
            dict(pergunta='Como comparar duas famílias de artigos?', resposta='Relacione cada opção com os destinatários, a ocasião, o uso esperado e o modo de distribuição; registe também as questões por confirmar.'),
            dict(pergunta='Uma proposta anterior pode ser reutilizada sem revisão?', resposta='Não assuma que as condições se mantêm. Reveja contexto, arte, variantes, quantidades, calendário e requisitos antes de a adaptar.'),
        ],
        relacionados=[
            dict(titulo='Como escolher o material de um brinde', url='guias/como-escolher-o-material.html'),
            dict(titulo='Como escolher a técnica', url='guias/como-escolher-a-tecnica.html'),
            dict(titulo='Como avaliar uma maquete antes da produção', url='guias/como-avaliar-uma-maquete.html'),
        ],
        etiquetas=['preparação de propostas', 'comparação', 'destinatários', 'requisitos', 'reconfirmação'],
        imagens_contexto=[
            imagem_contexto('empresas-distribuicao.jpg', 'Saco de tecido claro apresentado isoladamente sobre fundo branco.', 'A comparação começa por definir se o material será levado consigo ou entregue no local.', 300, 301),
            imagem_contexto('escolas-materiais.jpg', 'Conjuntos de material escolar em estojos transparentes, com régua e lápis.', 'Compare as possibilidades com o destinatário e a ocasião, não apenas pela aparência.', 300, 301),
        ],
        fotografia=imagem('revendedores.jpg', 'Chapéu de palha com fita colorida e dois acessórios dobráveis sobre fundo branco.', 700, 700),
    ),
    publico(
        'eventos',
        'Eventos',
        'Ideias para congressos, conferências, feiras, festivais e eventos desportivos, pensadas ao longo do percurso de participação.',
        [
            dict(destinatário='Participantes', necessidade='Podem precisar de informação, materiais de sessão ou de uma forma de identificar o evento.'),
            dict(destinatário='Oradores e expositores', necessidade='Podem ter necessidades diferentes das do público geral e da organização.'),
            dict(destinatário='Equipa organizadora e voluntários', necessidade='Podem precisar de identificação e de materiais ligados às tarefas que desempenham.'),
        ],
        [
            ocasiao(['Participantes', 'Oradores', 'Expositores'], 'Inscrição e receção', 'Balcão de inscrição, entrada ou ponto de acreditação', 'Antes da abertura e durante a chegada, segundo o programa do evento', 'Entregar informação e materiais adequados ao grupo identificado.'),
            ocasiao(['Participantes', 'Oradores'], 'Sessões e conferências', 'Salas, auditórios ou espaços de formação', 'Durante as sessões previstas no programa', 'Apoiar a atividade sem interferir com o conteúdo ou o equipamento de apresentação.'),
            ocasiao(['Expositores', 'Público'], 'Feira ou exposição', 'Bancadas, pavilhões e zonas de circulação', 'Horário e datas definidos para cada edição', 'Facilitar a participação ou a recolha de informação, ponderando o transporte.'),
            ocasiao(['Participantes', 'Voluntários', 'Público'], 'Festival, atividade ao ar livre ou evento desportivo', 'Recinto, percurso e pontos de apoio', 'Condições e datas variam por evento e edição', 'Planear onde ocorre a entrega e a quem se destina cada material.'),
            ocasiao(['Participantes', 'Organização'], 'Saída e encerramento', 'Saída, balcão de informação ou ponto de recolha', 'No fim do programa, se essa etapa estiver prevista', 'Evitar concentrar entregas num ponto que dificulte a circulação.'),
        ],
        [
            dict(destinatário='Participantes', objetivo='Inscrição e acompanhamento', famílias=['Sacos para documentação', 'Material de escrita', 'Artigos de identificação']),
            dict(destinatário='Oradores e expositores', objetivo='Apoio à participação', famílias=['Cadernos', 'Material de escrita', 'Artigos de identificação']),
            dict(destinatário='Organização e voluntários', objetivo='Identificação e coordenação', famílias=['Têxteis identificativos', 'Sacos para materiais da equipa', 'Artigos de identificação']),
            dict(destinatário='Público', objetivo='Participação e recordação', famílias=['Artigos para eventos', 'Sacos', 'Artigos de hidratação']),
        ],
        [
            'Desenhe a entrega ao longo do percurso: inscrição, receção, sessões, exposição ou atividades, e saída.',
            'Distinga materiais de participação, artigos para oradores, expositores e equipa; não pressuponha que o mesmo conteúdo serve todos.',
            'Para atividades ao ar livre, confirme local, acesso, transporte e plano de distribuição com a organização; não presuma condições meteorológicas nem requisitos de segurança.',
            'Faça uma simulação de montagem e fluxo com o espaço e as quantidades previstos.',
        ],
        [
            'Quem recebe cada material e em que etapa do evento?',
            'O que a pessoa terá de transportar durante e depois da participação?',
            'Onde será feita a entrega e como se evita criar filas ou bloquear acessos?',
            'Que variantes, línguas, mensagens ou nomes precisam de aprovação?',
            'As famílias sugeridas são possibilidades a avaliar, não um conjunto obrigatório para qualquer evento.',
        ],
        [
            dict(pergunta='É melhor entregar tudo na inscrição?', resposta='Depende do percurso, do volume e dos destinatários. Compare receção, sessões e saída e defina o ponto que melhor serve cada material.'),
            dict(pergunta='Participantes, oradores e expositores devem receber o mesmo?', resposta='Não existe uma regra universal. Identifique as necessidades de cada grupo e decida se há materiais diferentes ou se algum não é necessário.'),
        ],
        relacionados=[
            dict(titulo='Como escolher brindes para um evento', url='guias/como-escolher-brindes-para-um-evento.html'),
            dict(titulo='Como preparar um logótipo para personalização', url='guias/como-preparar-um-logotipo.html'),
            dict(titulo='Materiais', url='materiais/index.html'),
        ],
        etiquetas=['congressos', 'conferências', 'feiras', 'festivais', 'eventos desportivos'],
        imagens_contexto=[
            imagem_contexto('empresas-organizacao.jpg', 'Dois instrumentos de escrita dentro de uma caixa aberta de cartão.', 'A preparação de uma sessão começa por identificar o que é necessário e para quem.', 300, 301),
            imagem_contexto('eventos-acolhimento.jpg', 'Bolsa clara aberta com vários artigos de higiene pessoal dispostos à frente.', 'O acolhimento pode variar conforme o programa; a imagem é ilustrativa e não define uma oferta.', 1000, 1000),
        ],
        fotografia=imagem('eventos.png', 'Conjunto de artigos dispostos sobre uma mesa, incluindo recipientes, cadernos e acessórios.', 800, 600),
    ),
    publico(
        'turismo-alojamento',
        'Turismo e alojamento',
        'Ideias para acolhimento de hóspedes, visitas guiadas, programas culturais e eventos em alojamentos.',
        [
            dict(destinatário='Hóspedes', necessidade='Considere o que pode ser útil no contexto da estadia e se a pessoa terá de transportar o artigo durante a visita ou viagem.'),
            dict(destinatário='Visitantes e participantes', necessidade='Uma visita guiada ou programa cultural pode exigir informação legível e adequada ao percurso e à duração.'),
            dict(destinatário='Equipas de alojamento e organização', necessidade='Podem precisar de materiais para acolhimento, identificação ou coordenação de atividades.'),
        ],
        [
            ocasiao(['Hóspedes'], 'Receção ou início de uma estadia', 'Balcão de receção, quarto ou ponto de acolhimento', 'Ao longo do ano; épocas de maior procura variam por destino e alojamento', 'Transmitir informação útil ou acolher, se uma oferta for apropriada.'),
            ocasiao(['Visitantes', 'Guias'], 'Visita guiada ou programa cultural', 'Ponto de encontro, percurso ou equipamento cultural', 'Calendário e época definidos localmente', 'Apoiar a orientação ou a participação sem presumir necessidades de transporte.'),
            ocasiao(['Hóspedes', 'Participantes', 'Organização'], 'Evento num alojamento', 'Sala, espaço de receção ou área definida pelo alojamento', 'Datas específicas do programa e da reserva', 'Distinguir materiais de acolhimento, participação e apoio à equipa.'),
            ocasiao(['Visitantes', 'Comunidade local'], 'Dia Mundial do Turismo', 'Alojamento, destino ou atividade local', '27 de setembro; a página oficial da ONU Turismo consultada é relativa à edição de 2026 [dia-turismo]', 'Dar contexto a uma atividade local; a data não implica uma oferta nem uma iniciativa universal.'),
        ],
        [
            dict(destinatário='Hóspedes', objetivo='Acolhimento e informação', famílias=['Material informativo', 'Sacos', 'Artigos de hidratação']),
            dict(destinatário='Visitantes e participantes', objetivo='Visita e programa cultural', famílias=['Material de orientação', 'Sacos leves para materiais', 'Artigos de identificação']),
            dict(destinatário='Equipas de alojamento', objetivo='Coordenação e acolhimento', famílias=['Têxteis identificativos', 'Material de escrita', 'Artigos para eventos']),
        ],
        [
            'Considere se o artigo será entregue antes da visita, durante a estadia ou no final e quem o transportará.',
            'Se houver visitantes com línguas diferentes, confirme traduções e revisão da informação; não assuma que um idioma serve todas as pessoas.',
            'A sazonalidade e os programas dependem do destino e do alojamento: verifique a agenda local em vigor antes de referir épocas ou datas.',
            'Defina como a equipa guardará, reporá e distribuirá os materiais no ponto de receção.',
        ],
        [
            'O artigo continua útil fora do alojamento ou durante o transporte?',
            'A mensagem de acolhimento é local, clara e atualizada?',
            'Há necessidades linguísticas ou de orientação que a equipa já identificou?',
            'A oferta destina-se a hóspedes, visitantes, participantes ou à equipa?',
            'As famílias indicadas são possibilidades editoriais; não afirmam requisitos de viagem, compatibilidade ou características dos artigos.',
        ],
        [
            dict(pergunta='Há uma época turística igual em todos os destinos?', resposta='Não. Confirme a programação e os períodos relevantes com fontes atuais do destino e do alojamento.'),
            dict(pergunta='O Dia Mundial do Turismo é uma recomendação para oferecer artigos?', resposta='Não. 27 de setembro pode servir de referência a uma atividade; só considere uma oferta se corresponder ao objetivo e ao contexto locais.'),
        ],
        fontes=['dia-turismo'],
        relacionados=[
            dict(titulo='Como escolher brindes para um evento', url='guias/como-escolher-brindes-para-um-evento.html'),
            dict(titulo='Como escolher o material de um brinde', url='guias/como-escolher-o-material.html'),
            dict(titulo='Materiais', url='materiais/index.html'),
        ],
        etiquetas=['alojamento', 'hóspedes', 'visitas guiadas', 'programas culturais', 'visitantes'],
        imagens_contexto=[
            imagem_contexto('turismo-transporte.jpg', 'Recipiente escuro com tampa transparente, isolado sobre fundo claro.', 'Em visitas e estadias, considere o que as pessoas poderão transportar durante o percurso.', 500, 500),
        ],
        fotografia=imagem('turismo-alojamento.jpg', 'Almofada de viagem e acessórios dispostos sobre fundo branco.', 447, 447),
    ),
    publico(
        'associacoes-organizacoes-comunitarias',
        'Associações e organizações comunitárias',
        'Ideias para integrar e reconhecer voluntários e apoiar campanhas, iniciativas culturais e atividades comunitárias.',
        [
            dict(destinatário='Voluntários', necessidade='Podem precisar de acolhimento, informação sobre a atividade ou identificação relacionada com a função.'),
            dict(destinatário='Participantes e comunidade', necessidade='A utilidade do material depende do objetivo, da acessibilidade da mensagem e do local de distribuição.'),
            dict(destinatário='Equipas organizadoras', necessidade='Podem precisar de materiais separados para preparação, coordenação e entrega ao público.'),
        ],
        [
            ocasiao(['Voluntários'], 'Integração ou reconhecimento de voluntários', 'Sessão de acolhimento, ponto de encontro ou encerramento de atividade', 'Ao longo do ano; datas definidas pela organização', 'Agradecer ou apoiar a participação sem transformar o reconhecimento numa obrigação material.'),
            ocasiao(['Participantes', 'Comunidade'], 'Campanha de sensibilização', 'Rua, espaço comunitário, escola ou local da atividade', 'Calendário definido pela organização e pela campanha', 'Acompanhar uma mensagem clara e orientar a participação.'),
            ocasiao(['Comunidade', 'Voluntários', 'Equipas'], 'Iniciativa cultural ou atividade comunitária', 'Associação, recinto local, espaço público ou equipamento cultural', 'Datas e locais variam por organização e localidade', 'Facilitar acolhimento, identificação ou participação conforme a necessidade.'),
            ocasiao(['Voluntários', 'Comunidade'], 'Dia Internacional dos Voluntários', 'Atividade comunitária ou sessão da organização', '5 de dezembro, data anual assinalada pelas Nações Unidas [dia-voluntariado]', 'Dar visibilidade ao contributo voluntário; a data não implica oferecer brindes.'),
        ],
        [
            dict(destinatário='Voluntários', objetivo='Acolhimento e reconhecimento', famílias=['Artigos de identificação', 'Material de escrita', 'Têxteis identificativos']),
            dict(destinatário='Participantes e comunidade', objetivo='Informação e participação', famílias=['Material informativo', 'Sacos', 'Artigos para eventos']),
            dict(destinatário='Equipas organizadoras', objetivo='Coordenação local', famílias=['Cadernos', 'Material de escrita', 'Sacos para materiais da equipa']),
        ],
        [
            'Diferencie materiais de campanha, identificação de voluntários e ofertas aos participantes.',
            'Confirme que a mensagem é compreensível para o público e para o local onde será distribuída.',
            'Planeie o armazenamento, a entrega e o destino das sobras com a equipa organizadora.',
            'Se a iniciativa envolver outras entidades, confirme quem aprovou a mensagem e quem gere os materiais.',
        ],
        [
            'O que pretende alcançar: informar, acolher, identificar ou reconhecer?',
            'Quem deve receber o material e quem não precisa dele?',
            'A mensagem explica a ação sem exagerar o seu alcance ou prometer resultados?',
            'Há uma forma de participar sem receber um artigo?',
            'As famílias indicadas são possibilidades a avaliar e não substituem a decisão da organização.',
        ],
        [
            dict(pergunta='É necessário oferecer algo para reconhecer voluntários?', resposta='Não. O reconhecimento pode assumir formas diferentes; escolha uma oferta apenas se for adequada ao objetivo e à decisão da organização.'),
            dict(pergunta='O Dia Internacional dos Voluntários exige uma campanha ou oferta?', resposta='Não. 5 de dezembro é uma data de reconhecimento; qualquer atividade ou material é opcional e deve fazer sentido no contexto local.'),
        ],
        fontes=['dia-voluntariado'],
        relacionados=[
            dict(titulo='Como preparar um logótipo para personalização', url='guias/como-preparar-um-logotipo.html'),
            dict(titulo='Como escolher a técnica', url='guias/como-escolher-a-tecnica.html'),
            dict(titulo='Materiais', url='materiais/index.html'),
        ],
        etiquetas=['associações', 'organizações comunitárias', 'voluntários', 'sensibilização', 'iniciativas culturais'],
        ancora='associacoes',
        imagens_contexto=[
            imagem_contexto('associacoes-distribuicao.jpg', 'Saco de tecido bege apresentado isoladamente sobre fundo branco.', 'Em campanhas e atividades comunitárias, relacione a mensagem com o local e a forma de distribuição.', 300, 301),
        ],
        fotografia=imagem('associacoes-organizacoes-comunitarias.jpg', 'Caderno e caneta colocados sobre fundo branco.', 367, 367),
    ),
]

from conteudos.publicos_novos import criar, FONTES as FONTES_PUBLICOS_NOVOS
FONTES_PUBLICOS.update(FONTES_PUBLICOS_NOVOS)
PUBLICOS.extend(criar(publico, ocasiao, imagem, imagem_contexto))
