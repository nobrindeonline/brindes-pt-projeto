"""Guia da técnica; distinto do artigo de equipamentos em industria/sublimacao.html."""
FONTES_SUBLIMACAO = {
    'subepson': ('Epson — Sublimation Printers for Makers: suportes e ausência de tinta branca', 'https://epson.com/sublimation-printers-for-makers'),
    'subsawgrass': ('Sawgrass — SubliJet: processo e artigos preparados para sublimação', 'https://www.sawgrassink.com/sublijet/'),
    'subparametros': ('Sawgrass Care — Sublimation Heat Press Settings: parâmetros de partida e validação', 'https://care.sawgrassink.com/hc/en-us/articles/10587333978011-Sublimation-Heat-Press-Settings'),
    'subroland': ('Roland DG — Sublimation Printing: transferência e aplicações', 'https://www.rolanddg.com/applications/sublimated-graphics'),
}
SUBLIMACAO = {
    'id': 'tecnica-sublimacao', 'sec': 'tecnicas', 'tipo': 'tecnica',
    'titulo': 'Sublimação',
    'resumo': 'Personalização a cores por transferência de corantes com calor, em tecidos com poliéster e artigos com revestimento próprio. Conheça o processo e o que confirmar em cada referência.',
    'data_revisao': '2026-09-28', 'data_revisao_texto': '28 de setembro de 2026',
    'passos': ['Confirmar o artigo e o revestimento', 'Preparar a arte e imprimir a transferência', 'Posicionar e transferir com parâmetros validados', 'Retirar e arrefecer conforme a ficha', 'Conferir uma amostra'],
    'seccoes': [
        ('O que é a sublimação', 'Na sublimação convencional, o calor permite transferir corantes para um material recetor compatível. A imagem integra-se na fibra de poliéster ou no revestimento preparado para a receber, em vez de formar uma camada opaca de tinta branca sobre o artigo. Este guia aborda a transferência por papel, uma aplicação comum na personalização de brindes. [subsawgrass]'),
        ('Como funciona', 'O desenho é impresso com tinta de sublimação num papel de transferência adequado ao sistema. Posiciona-se o papel sobre a zona a personalizar e aplica-se calor com contacto e pressão controlados. O corante transfere-se para o suporte compatível. A remoção do papel e o arrefecimento seguem as instruções do artigo e do sistema utilizado. O esquema acima resume a sequência; não substitui uma ficha de produção. [subroland] [subparametros]'),
        ('Equipamento e consumíveis', 'O conjunto inclui impressora, tinta e papel compatíveis entre si, gestão de cor e equipamento de transferência ajustado à forma do artigo. Uma prensa plana e um equipamento para peças curvas exigem configurações próprias. Não basta possuir uma prensa: confirme dimensões, contacto com a zona imprimível e capacidade para controlar os parâmetros da referência escolhida. [subsawgrass] [subroland]'),
        ('Materiais compatíveis', 'A sublimação convencional funciona em tecidos com poliéster e em artigos com revestimento polimérico próprio para sublimação. Num tecido misto, a proporção e a distribuição do poliéster influenciam o resultado; algodão sem preparação não é um suporte equivalente. Em objetos rígidos, cerâmica, metal ou madeira de base não demonstram compatibilidade: é preciso identificar o revestimento recetor e confirmar que o artigo foi preparado para este processo. [subepson] [subsawgrass]'),
        ('Cores e influência do suporte', 'A tinta de sublimação convencional não imprime branco. As zonas brancas do desenho deixam aparecer a cor do suporte, que também influencia as restantes cores. Um fundo branco ou claro favorece a leitura e a reprodução, mas o suporte não tem obrigatoriamente de ser branco. Fundos escuros podem impedir o contraste pretendido; aprove uma prova na cor real do artigo, sem prometer uma correspondência exata com o ecrã. [subepson]'),
        ('Temperatura, tempo e pressão', 'Não existe uma receita universal de 180–200 °C. Temperatura, tempo e pressão dependem da tinta, do equipamento e do artigo, incluindo o revestimento e a geometria. As tabelas gerais são pontos de partida, não instruções válidas para todas as peças. Siga as recomendações dos fabricantes, confirme a calibração da prensa e valide uma amostra antes da série. Não copie os parâmetros de uma caneca para um tecido ou uma placa. [subparametros]'),
        ('Canecas, bases de rato e placas', 'Uma caneca só deve ser considerada após confirmação do revestimento próprio, da área autorizada e da compatibilidade com o equipamento. Numa base de rato, identifique a camada superior recetora e a tolerância do conjunto ao calor: o nome do produto ou uma base de borracha não bastam. Numa placa, confirme a face imprimível, o revestimento e as instruções específicas. Estas são perguntas de avaliação por referência, não uma declaração de compatibilidade de toda a categoria. [subepson] [subsawgrass]'),
        ('Quando escolher e preparar a arte', 'Pode ser uma opção para fotografias, gradientes e desenhos multicolores quando o artigo é adequado. [subroland] Entregue o original à dimensão pretendida, indique posição e margens e peça confirmação da resolução, do perfil de cor e do espelhamento exigido pelo fluxo de transferência. Verifique textos e logótipos na prova; não confunda a aprovação da composição numa maquete com a validação da cor e do acabamento numa amostra física.'),
        ('Limitações e cuidados', 'A técnica não torna qualquer superfície sublimável. Relevos, curvas ou zonas sem contacto uniforme precisam de avaliação. Um resultado satisfatório numa peça não garante o mesmo resultado noutra composição ou revestimento. Não prometa resistência universal à lavagem, máquina de lavar loiça, micro-ondas, abrasão ou exposição exterior: peça instruções e evidência para o artigo e a utilização pretendida. Evite extrapolar a durabilidade a partir do aspeto da primeira amostra.'),
        ('O que confirmar para cada artigo', 'Registe fornecedor, referência, composição, cor e revestimento; confirme a indicação expressa para sublimação e a área imprimível. Reúna as instruções da tinta, papel e equipamento, os parâmetros aprovados e os cuidados de utilização. Peça uma amostra na referência final, incluindo a avaliação de cor, posição, legibilidade, deformação e resistência necessária. Guarde a prova e as condições aprovadas para comparação com a produção. Esta lista é orientação editorial para preparar a encomenda.'),
        ('Comparar alternativas', 'Quando a composição, a cor ou o acabamento não servem a sublimação, compare serigrafia, impressão digital UV, bordado ou outros processos de transferência. Cada alternativa precisa da sua própria avaliação de compatibilidade. Sublimação e DTF não são sinónimos: a existência de uma etapa de prensagem não identifica o processo nem permite trocar consumíveis ou parâmetros.'),
    ],
    'problemas': [
        ('Cor diferente ou pouco visível', 'Confirmar a cor e a composição do suporte, o perfil usado e a amostra aprovada. A ausência de tinta branca deve ser considerada logo na escolha do artigo. [subepson]'),
        ('Resultado irregular ou contornos duplicados', 'Pedir à produção que reveja o posicionamento, o contacto e a estabilidade da transferência. Um defeito visual não permite concluir uma causa única; comparar a amostra e o registo do processo.'),
        ('Deformação ou alteração do acabamento', 'Suspender a repetição dos mesmos parâmetros e confirmar com o fornecedor as condições admissíveis do artigo. Rever a combinação de tempo, temperatura e pressão, sem aumentar o calor por tentativa. [subparametros]'),
    ],
    'fontes': list(FONTES_SUBLIMACAO),
    'relacionados': ['sublimacao', 'como-escolher-a-tecnica', 'serigrafia', 'impressao-uv', 'materiais-texteis', 'vidro-e-ceramica'],
    'ancoras': ['tecnicas/index.html#textil', 'produtos/index.html#bebidas', 'materiais/index.html#texteis'],
    'tags': 'sublimação sublimacao poliéster poliester revestimento polimérico canecas bases de rato placas calor prensa transferência cores sem branco',
}

# Utilização autorizada expressamente pelo utilizador em 28/09/2026.
# Origem/autoria não documentadas; não inferir tecnologia ou licença pelo nome.
IMAGENS_SUBLIMACAO = {
    'Equipamento e consumíveis': [
        ('Imagem ChatGPT 28_09_2026, 16_21_36.jpg', 404,
         'Composição com impressora, quatro frascos de tinta, prensa plana, papel e rolo de fita.',
         'Conjunto ilustrativo de equipamento e consumíveis. A imagem não confirma a compatibilidade entre os elementos apresentados.'),
        ('Imagem ChatGPT 28_09_2026, 16_21_32.jpg', 474,
         'Prensa térmica plana com acessórios de diferentes formas apresentados em redor.',
         'Exemplo visual de prensa com acessórios. A forma do acessório não confirma os parâmetros nem a compatibilidade de um artigo concreto.'),
    ],
    'Temperatura, tempo e pressão': [
        ('Imagem ChatGPT 28_09_2026, 16_21_23.jpg', 490,
         'Prensa térmica plana aberta, com imagens de almofadas, camisola escura e saco ao lado.',
         'Uma prensa pode servir vários processos de transferência. As peças escuras desta montagem não demonstram aplicação de sublimação convencional nem impressão de branco.'),
    ],
    'Comparar alternativas': [
        ('Imagem ChatGPT 28_09_2026, 16_21_39.jpg', 355,
         'Equipamentos de impressão com tecido estampado com motivos florais.',
         'Imagem ilustrativa de impressão têxtil: não permite identificar a tecnologia, a tinta ou a composição do tecido e não comprova um processo de sublimação.'),
    ],
}
