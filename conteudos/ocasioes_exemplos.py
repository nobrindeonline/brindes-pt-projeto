"""Exemplos ilustrados, por utilização; nomes comerciais ficam apenas nas origens."""
ORIGINAIS = {
 'natal-ornamentos': 'Natal/ig_0_nb199206_SET-DE-6-ORNAMENTOS-DE-NATAL.jpg',
 'natal-adereco': 'Natal/ig_0_nb214743_ADERECO-PAIS-NATAL.jpg',
 'natal-gorro': 'Natal/z_nb233034_GORRO-DE-NATAL_IP_5.jpg',
 'inverno-manta': 'Inverno/ig_0_nb221597_MANTA-VIAGEM-BASICA.jpg',
 'inverno-meias': 'Inverno/ig_0_nb293088_MEIAS-DE-INVERNO-UNISSEXO.jpg',
 'carnaval-mascara': 'Carnaval/ig_0_nb177444_MASCARA-EM-EVA-C-ELASTICO-PERSONALIZAVEL.jpg',
 'carnaval-pintura': 'Carnaval/ig_0_nb203770_STICK-PINTURA-CORPORAL.jpg',
 'carnaval-capa': 'Carnaval/ig_0_nb302148_CAPA-SUPER-HEROI-PARA-CRIANCA-PERSONALIZAVEL.jpg',
 'verao-chinelos': 'Verao/ig_0_nb168468_CHINELOS-BRASILEIRA.jpg',
 'verao-almofada': 'Verao/ig_0_nb190089_ALMOFADA-INSUFLAVEL.jpg',
 'verao-disco': 'Verao/ig_0_nb204550_DISCO-VOADOR-DE-21-CM-DE-DIAMETRO..jpg',
 'verao-praia': 'Verao/ig_0_nb204705_SET-DE-PRAIA-INFANTIL-EM-4-CORES-DIFERENTES.-DOIS-SETS-DE-PR.jpg',
}

def exemplo(id, titulo, alt, width, height, contexto, motivo, confirmar, relacionado):
    return dict(id=id, titulo=titulo, imagem=dict(url='assets/ocasioes/visuais/'+id+'.jpg',
        alt=alt, width=width, height=height,
        legenda='Exemplo ilustrativo. A fotografia não comprova composição, desempenho ou adequação a uma idade.'),
        contexto=contexto, motivo=motivo, confirmar=confirmar, relacionado=relacionado)

EXEMPLOS = {
 'natal': [
    exemplo('natal-ornamentos','Ornamentos para uma decoração partilhada',
        'Seis pequenos ornamentos com motivos natalícios e cordões para pendurar.',300,301,
        'Uma atividade de associação, escola ou equipa em que os participantes decoram um espaço comum, se essa celebração fizer sentido para o grupo.',
        'O objeto fica ligado a uma ação concreta: escolher onde o colocar e compor a decoração. Pode também acompanhar um cartão para levar para casa, sem exigir um conjunto volumoso.',
        'Observe dimensões, forma de suspensão, armazenamento e eventuais peças destacáveis. Um ornamento decorativo não deve ser tratado automaticamente como brinquedo. Confirme se o desenho e o espaço de personalização permitem uma mensagem legível.',
        'casa-decoracao-e-cuidados-pessoais'),
    exemplo('natal-adereco','Adereços para uma participação breve',
        'Bandolete vermelha com duas pequenas figuras natalícias presas a molas.',300,300,
        'Um momento de animação ou fotografia num encontro, com utilização voluntária e possibilidade de participar sem adereço.',
        'Pode marcar visualmente o momento festivo sem acrescentar uma peça de vestuário completa. Faz mais sentido quando há uma atividade preparada do que numa entrega sem contexto.',
        'Verifique ajuste, fixações, conforto e instruções para o utilizador previsto. Combine como será distribuído e guardado; não deduza adequação infantil ou resistência das molas pela imagem.',
        'eventos-identificacao-e-premios'),
    exemplo('natal-gorro','Gorros numa atividade de grupo',
        'Gorro vermelho com faixa e pompom brancos.',500,500,
        'Uma equipa de acolhimento ou um grupo que escolheu uma apresentação festiva para um encontro.',
        'Uma peça visual comum pode ajudar a reconhecer o grupo durante a atividade. Se o objetivo for apenas acompanhar um agradecimento pessoal, um cartão ou outro artigo pode ter mais utilidade.',
        'Confirme medidas, composição e cuidados da peça, bem como a visibilidade da mensagem quando está colocada. A forma de gorro natalício não demonstra proteção contra frio nem torna a utilização obrigatória.',
        'texteis'),
 ],
 'inverno': [
    exemplo('inverno-manta','Mantas para pausas e deslocações',
        'Manta preta com padrão de linhas claras, dobrada e presa com uma fita branca.',300,300,
        'Uma entrega individual para uso doméstico, pausas ou viagens, quando a pessoa dispõe de espaço para levar e guardar a peça.',
        'Pode continuar a ter uma função depois do encontro. A escolha é mais pertinente quando corresponde a uma rotina conhecida do que quando apenas se associa a palavra Inverno a uma oferta.',
        'Meça a manta aberta e dobrada, observe como se guarda e consulte composição e cuidados. Espessura aparente e padrão não quantificam isolamento térmico. Planeie a personalização tendo em conta a face visível nas duas posições.',
        'casa-decoracao-e-cuidados-pessoais'),
    exemplo('inverno-meias','Meias para uma oferta pessoal',
        'Dois pés com meias de padrões claros, uma vermelha e outra azul-escura.',300,301,
        'Um conjunto pessoal ou doméstico, se houver informação suficiente sobre tamanhos e preferências de quem recebe.',
        'O volume reduzido pode simplificar a apresentação e o transporte. O interesse está no uso real da peça, não numa promessa genérica de conforto para todas as pessoas.',
        'Confirme gama de tamanhos, composição, costuras e lavagem. A imagem não demonstra propriedades térmicas ou antiderrapantes. Se não conhecer o tamanho, considere uma alternativa que não dependa dessa informação.',
        'texteis'),
 ],
 'carnaval': [
    exemplo('carnaval-mascara','Máscaras para compor uma personagem',
        'Máscara de olhos amarela e verde com padrão geométrico.',300,300,
        'Uma oficina ou atividade de caracterização em que a organização selecionou o artigo para os participantes concretos.',
        'Pode servir de ponto de partida para uma personagem e relacionar a preparação com a participação na atividade. Não representa automaticamente uma tradição portuguesa nem substitui a revisão dos símbolos locais.',
        'Avalie ajuste, aberturas, sistema de fixação e instruções. Não se trata de proteção respiratória. Para utilização por crianças, respeite idades, capacidades e avisos do artigo; a orientação europeia de brinquedos não certifica esta máscara. [brinquedos]',
        'criancas'),
    exemplo('carnaval-pintura','Pintura para uma atividade de caracterização',
        'Aplicador de várias cores com tampa transparente, acompanhado por outras combinações de cores.',300,301,
        'Um momento organizado de caracterização, apenas depois de confirmar o uso previsto, os destinatários e o modo de aplicação.',
        'Pode acompanhar uma escolha de cores ou personagem sem acrescentar uma peça de roupa. O seu interesse depende da atividade e da vontade de participar; uma alternativa sem aplicação na pele deve continuar disponível.',
        'Consulte rótulo, ingredientes, avisos, zonas de aplicação e remoção. A FDA recomenda seguir as instruções, não partilhar maquilhagem e não a usar junto dos olhos se não for destinada a essa zona. É orientação geral norte-americana, não aprovação deste artigo para Portugal. [cosmeticos]',
        'como-avaliar-uma-maquete'),
    exemplo('carnaval-capa','Capas para atividades de representação',
        'Capa vermelha com desenho amarelo, estrelas e uma mensagem de super-heroína.',300,300,
        'Uma dinâmica de representação ou desfile de um grupo que definiu personagens, movimento e acompanhamento.',
        'Uma capa permite construir uma apresentação visual sem exigir um conjunto completo de fantasia. A imagem ou mensagem pode ligar-se à atividade, desde que respeite as escolhas e os participantes.',
        'Confirme tamanho, comprimento, fecho e liberdade de movimentos no percurso previsto. Não deduza comportamento perante chama, proteção ou adequação etária pela fotografia; o adulto responsável deve conservar os avisos e instruções aplicáveis. [brinquedos]',
        'texteis'),
 ],
 'verao': [
    exemplo('verao-chinelos','Chinelos quando o uso é conhecido',
        'Pares de chinelos de enfiar o pé, apresentados em várias cores.',300,306,
        'Uma oferta ligada a estadia ou lazer em que se conhecem o tamanho e as condições em que a pessoa pretende usar o calçado.',
        'Podem corresponder a uma necessidade concreta de uso pessoal e ocupar pouco espaço numa apresentação. Perdem pertinência se o tamanho ou o contexto forem desconhecidos.',
        'Verifique medidas, ajuste, sola e instruções para as superfícies previstas. A associação a praia ou piscina não demonstra aderência em piso molhado. A personalização deve ser avaliada sem comprometer a utilização.',
        'texteis'),
    exemplo('verao-almofada','Almofadas insufláveis para pausas e viagens',
        'Almofadas retangulares coloridas com válvula lateral.',300,301,
        'Uma deslocação ou pausa em que o destinatário valoriza poder guardar o objeto com pouco volume, se essa for uma característica confirmada do artigo.',
        'A forma de encher, esvaziar e guardar faz parte da escolha. Pode ser mais útil para quem o transporta consigo do que um objeto volumoso que fica sem utilização no percurso.',
        'Confirme dimensões em uso, válvula, método de enchimento, limpeza e armazenamento. Não apresente uma almofada como equipamento de flutuação ou proteção aquática; a aparência insuflável não demonstra essa finalidade.',
        'sacos-e-mochilas'),
    exemplo('verao-disco','Discos para uma atividade recreativa',
        'Cinco discos redondos nas cores verde, laranja, vermelho, preto e azul.',300,301,
        'Uma atividade de grupo num espaço onde a organização tenha previsto área e regras de jogo.',
        'O artigo pode ser usado durante a própria iniciativa, em vez de ficar apenas como recordação. Antes de preparar uma entrega individual, avalie se materiais partilhados no local cumprem o mesmo objetivo.',
        'Considere o espaço de utilização, outros participantes, instruções e arrumação depois do jogo. Não atribua idade indicada ou resistência pelo aspeto. Para brinquedos, a orientação europeia recomenda respeitar idade, capacidades e supervisão. [brinquedos]',
        'desporto-lazer-e-exterior'),
    exemplo('verao-praia','Conjuntos para brincar na areia',
        'Baldes de várias cores com pequenas pás e formas de brincar na areia.',300,301,
        'Uma atividade de praia ou de areia preparada para crianças acompanhadas, com escolha do conjunto pelo adulto responsável.',
        'Pode dar suporte a uma tarefa concreta, como construir e moldar em grupo. A utilidade depende do local e de como as peças são reunidas e guardadas; não é uma oferta necessária em todas as visitas.',
        'Confirme idade indicada, peças incluídas, avisos e forma de limpeza. A orientação europeia recomenda respeitar as indicações e acompanhar a utilização dos brinquedos. Não deduza aptidão para contacto com alimentos nem função de proteção na água. [brinquedos]',
        'criancas'),
 ],
}

def integrar(artigos, fontes, fonte):
    fontes['cosmeticos'] = fonte('Utilização de cosméticos', 'Food and Drug Administration',
        'https://www.fda.gov/cosmetics/resources-consumers-cosmetics/using-cosmetics-safely',
        'Orientação de utilização norte-americana; não certifica a pintura ilustrada nem substitui requisitos aplicáveis em Portugal.')
    fontes['brinquedos'] = fonte('Escolha e utilização de brinquedos', 'Comissão Europeia',
        'https://ec.europa.eu/docsroom/documents/6791/attachments/1/translations',
        'Idade, capacidades, avisos e supervisão; não valida os artigos fotografados.')
    for a in artigos:
        a['exemplos'] = EXEMPLOS[a['id']]
        # O índice semântico usa o texto editorial, sem nomes dos ficheiros de origem.
        a['seccoes'].append(('Exemplos em contexto', ' '.join(
            e['titulo']+' '+e['contexto']+' '+e['motivo']+' '+e['confirmar'] for e in a['exemplos'])))
        if a['id']=='carnaval': a['fontes'].extend(['brinquedos','cosmeticos'])
        if a['id']=='verao': a['fontes'].append('brinquedos')
