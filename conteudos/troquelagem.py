"""Troquelagem: fontes técnicas e imagens locais observadas em 7 de outubro de 2026."""

FONTES_TROQUELAGEM = {
    'troqessencial': ('BOBST — The essentials of carton converting', 'https://www.bobst.com/na/en/news/1768493402-the-essentials-of-carton-converting'),
    'troqplaca': ('BOBST — The importance of the cutting plate in the folding carton die-cutting process', 'https://www.bobst.com/eu/en/news/1689880801-the-importance-of-the-cutting-plate-in-the-folding-carton-die-cutting-process'),
    'troqoperacoes': ('Esko — Processing Steps: Groups and Types', 'https://docs.esko.com/docs/en-us/automationengine/24.07/userguide/en-us/common/ae/concept/co_ae_PDFplus_ProcessingSteps.html'),
    'troqmaquinas': ('HEIDELBERG — Die-cutting & embossing', 'https://www.heidelberg.com/global/en/print_and_packaging/finishing/die_cutting/die_cutting___overview.jsp'),
    'troqferramenta': ('Rollem — Insignia: ferramentas, corte parcial e separação de peças', 'https://www.rollemusa.com/wp-content/uploads/2022/06/Insignia-Brochure-2021-email.pdf'),
    'troqpvc': ('Rollem — Success Stories: aplicação Insignia em papel e PVC', 'https://www.rollemusa.com/success-stories/'),
    'troqpele': ('ATOM — Leather Cutting Machines', 'https://atom.it/en/industrial-sector/leather-cutting-machines/'),
    'troqmanual': ('Sizzix — New to Die Cutting: equipamento manual de bancada', 'https://www.sizzix.com/pages/new-to-die-cutting'),
    'troqauto': ('BOBST — Engineering the future: 85 years of Autoplaten innovation', 'https://www.bobst.com/ru/en/news/1762165202-engineering-the-future-bobst-celebrates-85-years-of-autoplaten-innovation'),
    'troqdigital': ('Zünd — Packaging: corte digital sem troquel', 'https://www.zund.com/en/applications/packaging'),
    'troqperfurar': ('Duplo — Print finishing: perfuração e outras operações', 'https://www.duplointernational.com/uk/article/how-duplo-print-finishing-can-boost-your-holiday-business'),
}

# Nomes e capitalização preservados; as dimensões são as dos ficheiros originais.
# unnamed (31).jpg foi observada mas não usada: outra máquina manual e acessórios,
# sem acrescentar uma operação distinta às duas imagens selecionadas.
IMAGENS_TROQUELAGEM = {
    'o-que-e': ('unnamed (32).jpg', 474, 474,
        'Máquina de bancada azul-clara com manivela, placas de passagem, formas metálicas e recortes decorativos sobre a mesa.',
        'Exemplo de equipamento manual de bancada, com ferramentas e recortes decorativos. A fotografia não identifica materiais ou capacidades de produção.'),
    'como-funciona': ('unnamed (33).jpg', 474, 206,
        'Esquema em duas etapas: ferramenta de corte acima de uma folha verde apoiada numa placa e contornos resultantes na folha.',
        'Esquema do contacto entre ferramenta e folha apoiada numa placa. Não representa todas as configurações de troquelagem.'),
}

OPERACOES = [
    ('Corte total', 'Atravessa o suporte nas linhas definidas para obter o contorno ou uma abertura. A retirada da peça e das sobras pode ocorrer numa etapa própria. [troqoperacoes] [troqferramenta]'),
    ('Corte parcial e kiss-cut', 'O corte parcial não atravessa toda a espessura. Nas etiquetas autocolantes, o kiss-cut pode recortar a camada superior preservando a base de suporte, para permitir destacar a etiqueta. Indique quais as camadas a cortar e a conservar. [troqoperacoes] [troqferramenta]'),
    ('Vincagem', 'Prepara uma linha que orienta uma dobra posterior, por exemplo numa caixa. Não equivale a separar o material por corte. [troqoperacoes]'),
    ('Perfuração', 'Cria uma sequência de pequenas aberturas, que pode facilitar destacar uma parte, como num cupão. Distingue-se de um corte contínuo e de um vinco. [troqperfurar]'),
]

PASSOS = [
    ('Preparar o desenho e o troquel', 'Definir contornos e operações. A ferramenta pode usar lâminas montadas numa base ou uma matriz flexível, conforme o sistema. [troqferramenta]'),
    ('Posicionar o material', 'Colocar o suporte e alinhar o corte com o grafismo, quando existe impressão. Confirmar formato e orientação antes da série. [troqauto]'),
    ('Aplicar pressão e executar o corte', 'A ferramenta atua sobre o material contra uma superfície de apoio. A placa de corte e o seu estado influenciam a qualidade; os ajustes pertencem ao equipamento e ao trabalho concreto. [troqplaca]'),
    ('Separar e conferir', 'Retirar peças e sobras conforme a configuração, ou manter as etiquetas na base quando isso foi previsto. Verificar o contorno e, numa embalagem, a montagem. [troqferramenta]'),
]

FAQ = [
    ('Posso pedir uma amostra antes de existir o troquel?', 'Pergunte se é possível validar primeiro a forma com corte digital. Essa amostra ajuda a avaliar dimensões e montagem, mas não confirma automaticamente o acabamento da futura produção com troquel. [troqdigital]'),
    ('O mesmo troquel serve depois de mudar o material?', 'Não o dê por garantido. Mesmo mantendo o desenho, peça avaliação da espessura, das camadas, dos vincos e do sistema de corte antes de reutilizar a ferramenta.'),
    ('Como evitar que as linhas técnicas apareçam impressas?', 'Entregue grafismo e operações identificados separadamente e peça confirmação da interpretação do ficheiro. Reveja uma prova que distinga o que será impresso do que será cortado ou vincado. [troqoperacoes]'),
]

TROQUELAGEM = {
    'id': 'tecnica-troquelagem', 'sec': 'tecnicas', 'tipo': 'tecnica',
    'titulo': 'Troquelagem',
    'resumo': 'Um troquel define e corta uma forma no suporte. Conheça o processo, as operações relacionadas e os pontos a validar em etiquetas, caixas e outras peças.',
    'data_revisao': '2026-10-07', 'data_revisao_texto': '7 de outubro de 2026',
    'ids_seccoes': ['o-que-e', 'como-funciona', 'operacoes', 'equipamento', 'materiais', 'vantagens', 'limitacoes', 'preparar', 'comparar', 'perguntas'],
    'seccoes': [
        ('O que é a troquelagem?', 'A troquelagem utiliza uma ferramenta de corte, o troquel, para dar uma forma definida ao material. Pode preparar peças recortadas ou suportes que depois serão dobrados e montados. [troqferramenta]\n\nÉ uma operação de forma ou acabamento: por si só, não imprime cores nem grafismos. Pode integrar um trabalho que também inclui impressão, estampagem e montagem, com etapas distintas. [troqessencial]'),
        ('Como funciona', 'O percurso abaixo explica a lógica do trabalho. A alimentação, o corte e a retirada das sobras variam com a máquina; não se trata de uma instrução de operação.'),
        ('Tipos de corte e operações relacionadas', 'Corte, corte parcial, vincagem e perfuração têm funções diferentes. Podem ser combinados quando a ferramenta e a configuração o permitem, mas não estão todos presentes em cada encomenda. [troqoperacoes]'),
        ('Equipamentos e configurações', 'No corte plano, o troquel atua sobre uma superfície plana; no rotativo, a ferramenta trabalha num sistema de cilindros. A HEIDELBERG apresenta ambas as configurações, e a Rollem documenta matrizes flexíveis em cilindros magnéticos. [troqmaquinas] [troqferramenta]\n\nO grau de automação é outra distinção. Há equipamentos manuais de bancada, como os apresentados pela Sizzix. A BOBST documenta processos manuais e semiautomáticos e a automação da alimentação e do alinhamento das folhas. Confirme quais as fases manuais ou automáticas da solução proposta; estas referências não identificam máquinas da Nobrinde. [troqmanual] [troqauto]'),
        ('Materiais e aplicações', 'Papel e cartão podem dar origem a etiquetas, peças de apresentação e caixas. A BOBST descreve a transformação de cartão em embalagens; a Rollem inclui etiquetas e peças autocolantes entre as aplicações dos seus sistemas. [troqessencial] [troqferramenta]\n\nPVC e couro/pele exigem avaliação própria: a Rollem documenta PVC em aplicações Insignia, enquanto a ATOM apresenta prensas de troquelagem para couro. São exemplos específicos, não uma lista de materiais universalmente aceites. [troqpvc] [troqpele]\n\nIndique material, espessura, camadas, acabamento, formato e finalidade. Para uma etiqueta, esclareça se deve permanecer numa base; para uma caixa, entregue as dimensões e necessidades de montagem. Peça ensaio no material escolhido antes de aprovar a produção.'),
        ('Vantagens e critérios de escolha', 'Uma ferramenta permite repetir a mesma forma e, em configurações adequadas, reunir diferentes operações. A BOBST distingue soluções conforme a série e o suporte; não há uma configuração superior para todos os trabalhos. [troqessencial]\n\nPara decidir, compare o resultado pretendido, a frequência de repetição, o número de formatos e a necessidade de alterar o desenho. Avalie a amostra pelo contorno, pelo destaque da peça e pela montagem, quando aplicável.'),
        ('Limitações e aspetos a confirmar', 'A ferramenta e a preparação representam custos a considerar no conjunto da produção. Séries pequenas não excluem automaticamente a troquelagem: a BOBST descreve matrizes rotativas flexíveis orientadas para trabalhos curtos. Peça comparação de soluções para o seu desenho e material, sem assumir uma quantidade mínima universal. [troqessencial]\n\nO estado e a escolha da placa de corte também importam. A BOBST associa desgaste ou seleção inadequada a problemas como rebarbas, poeiras e folhas presas à ferramenta. A causa e a correção devem ser avaliadas na produção; não se pode garantir um acabamento apenas pelo nome da técnica. [troqplaca]'),
        ('Preparar o ficheiro e validar o trabalho', 'Defina o contorno final e identifique corte, corte parcial, vincagem e perfuração separadamente do grafismo. A documentação Esko distingue estes dados estruturais e também as indicações de sangria. Combine com o fornecedor a organização de camadas, nomes e formato do ficheiro; não existe aqui uma convenção de cor ou margem imposta ao trabalho. [troqoperacoes]\n\nIndique se o corte atravessa o conjunto ou preserva uma base. Junte dimensões finais, material e uma visualização do resultado montado quando necessário. Antes de produzir, valide desenho, material e prova: contorno, alinhamento com a impressão, facilidade de destaque e comportamento nas dobras.'),
        ('Comparar com corte digital', 'O corte digital pode seguir o desenho sem fabricar um troquel para cada forma. A Zünd apresenta esta abordagem para protótipos e pequenas séries de embalagens. Compare preparação, variedade de desenhos, material e resultado final; a ausência de troquel não demonstra, por si só, menor custo total em qualquer quantidade. [troqdigital]\n\nTroquelagem e termogravura também não são equivalentes: uma define cortes e formas; a outra é uma técnica de estampagem. Se quiser combinar contorno, impressão e acabamento, especifique cada operação e valide a sequência com a produção.'),
        ('Perguntas frequentes', 'Três dúvidas úteis antes de fechar o desenho e pedir avaliação à produção.'),
    ],
    'fontes': list(FONTES_TROQUELAGEM), 'problemas': [],
    'relacionados': ['termogravura', 'serigrafia', 'impressao-uv', 'transfers', 'troquelagem', 'papel-e-cartao', 'pele-e-imitacao-de-pele', 'como-preparar-um-logotipo', 'como-avaliar-uma-maquete'],
    'ancoras': ['tecnicas/index.html#acabamentos', 'materiais/index.html#plasticos'],
    'tags': 'troquelagem troquel molde corte total parcial kiss-cut vincagem perfuração plano rotativo etiquetas caixas papel cartao PVC couro pele faca corte digital',
}
