"""Estampagem a quente com folha: conteúdo e fontes, sem fotografias não autorizadas."""

FONTES_TERMOGRAVURA = {
    'termintro': ('Foilco — Foil Academy: processo, cunhos e marca de pressão', 'https://www.foilco.com/foil-academy/'),
    'termestrutura': ('Foilco — Structure of Foil: suporte, camada de libertação e adesivo', 'https://www.foilco.com/structure-of-foil/'),
    'termguia': ('Foilco — D4 Foil Grade Guide, edição 1: acabamentos (pp. 5–6), aplicações e parâmetros orientativos (pp. 18 e 24)', 'https://www.foilco.com/app/uploads/2019/05/Grade-Guide-Booklet_E_Doc.pdf'),
    'termholo': ('KURZ — Holograms: efeitos holográficos e estampagem a quente', 'https://www.kurz-world.com/en/solutions/holograms/'),
    'termpapel': ('Iggesund Paperboard — Hot foil stamping in practice, pp. 62–63: superfície e transferência', 'https://www.iggesund.com/globalassets/iggesund/services/knowledge/iam/graphics-handbook/gh-pdf----en/hot_foil_stamping_in_practice.pdf'),
    'termdetalhe': ('Foilco — Fine Detail Foiling: espaços, letras e áreas cheias', 'https://www.foilco.com/fine-detail-foiling/'),
    'termcunho': ('Foilco — Brass: produção e custo relativo do cunho', 'https://www.foilco.com/brass/'),
    'termtempo': ('Howard Imprinting — Foil Application Guide, p. 2: relação entre temperatura e tempo de contacto', 'https://www.howardimprinting.com/myfiles/FOIL-APPLICATION-GUIDE.pdf'),
    'termfalhas': ('Milford Astor / Ever Bright — Manual H-200B, H-250 e H-400, p. 23: falhas de transferência', 'https://astor.com.au/content/products/H-200B%20H250%20H-400%20Operating%20Instructions.pdf'),
}

TERMOGRAVURA = {
    'id': 'termogravura', 'sec': 'tecnicas', 'tipo': 'tecnica',
    'titulo': 'Termogravura',
    'resumo': 'Estampagem a quente com folha: como o cunho transfere o acabamento, que materiais avaliar e o que confirmar na arte e na amostra.',
    'data_revisao': '2026-09-29', 'data_revisao_texto': '29 de setembro de 2026',
    'ids_seccoes': ['o-que-e', 'como-funciona', 'folhas-acabamentos', 'materiais-artigos', 'preparacao-arte', 'resultado-limitacoes', 'confirmar', 'comparar'],
    'seccoes': [
        ('O que é a termogravura',
         'Neste guia, termogravura significa estampagem a quente com folha, também conhecida como hot foil stamping, hot stamping ou foil blocking. Um cunho ou molde metálico aquecido pressiona a folha contra o artigo e transfere o desenho. [termintro]\n\n'
         'Confirme sempre o significado do termo com o fornecedor: este artigo trata da transferência decorativa com folha. Uma marca feita apenas por pressão, sem folha, é um acabamento diferente. A conformação de peças metálicas a quente, que também pode aparecer sob o nome hot stamping, não é o processo aqui descrito.'),
        ('Como funciona: do desenho à transferência',
         'A arte define as zonas que recebem o acabamento. A partir dela prepara-se o cunho, que tem de corresponder à dimensão e ao desenho aprovados. Na máquina, posicionam-se a peça e a folha entre o cunho e a superfície a marcar. [termintro]\n\n'
         'A folha inclui um filme de transporte e camadas que permitem libertar e fixar a decoração. Calor e pressão fazem transferir as zonas em contacto; o filme de transporte é separado e não fica a cobrir o artigo como uma película inteira. A formulação adesiva faz parte da escolha para o suporte. [termestrutura]\n\n'
         'Pressão, temperatura e tempo de contacto interagem e devem ser ajustados ao material, à folha e à máquina. O guia Howard relaciona temperatura e duração do contacto; o guia Foilco avisa que as temperaturas tabeladas são apenas orientativas e dependem da velocidade da máquina. Não existe uma tabela universal a aplicar a qualquer capa ou agenda. A preparação deve incluir ensaios, seguindo as instruções do equipamento e dos consumíveis. [termtempo] [termguia]'),
        ('Folhas e acabamentos',
         'Há folhas com aspeto metálico, incluindo dourado e prateado, e variantes acetinadas, pigmentadas brilhantes ou mate. São famílias de acabamento; a referência disponível e a formulação adequada ao suporte precisam de confirmação. A designação dourado não significa que se esteja a aplicar ouro maciço. [termguia]\n\n'
         'Existem também efeitos holográficos, que podem alterar a leitura visual com a luz e o ângulo de observação. A KURZ documenta a sua aplicação por estampagem a quente. [termholo] A imagem estampada recebe o efeito da folha escolhida: a técnica, por si só, não reconstrói as cores de uma fotografia nem os degradés do ficheiro original. Um padrão ou efeito multicolor já presente na folha não equivale a imprimir essa fotografia. Compare uma amostra física, não apenas a simulação no ecrã.'),
        ('Materiais e artigos: avaliar a superfície real',
         'Papel e cartão são exemplos documentados. A lisura, a limpeza, o revestimento e a estabilidade da superfície influenciam a definição e a ligação da folha; as irregularidades podem ficar mais evidentes no acabamento. A orientação da Iggesund refere-se a cartão, não confirma todas as superfícies. [termpapel]\n\n'
         'Capas, agendas, pele e imitação de pele podem entrar na avaliação. O guia Foilco identifica aplicações de determinadas formulações em encadernação, pele revestida e imitação de pele; isso não torna qualquer folha compatível com qualquer uma dessas peças. [termguia] Identifique vernizes, laminações e outras camadas, a textura e a sensibilidade ao calor. Numa agenda montada, confirme também se lombada, elástico, costuras ou acolchoamento permitem apoiar e alcançar a posição pretendida. Peça ensaio na referência concreta.'),
        ('Preparação da arte',
         'Forneça o desenho à escala final, com as zonas a estampar bem identificadas, e confirme o formato pedido por quem fabrica o cunho. Uma linha positiva é uma linha que recebe folha; uma linha negativa é um espaço deixado livre dentro de uma área estampada. Reveja ambas, incluindo os espaços interiores das letras e a distância entre caracteres.\n\n'
         'Pormenores finos e espaços estreitos podem perder separação. Combinar grandes áreas cheias com traços muito delicados no mesmo desenho merece avaliação específica. A Foilco recomenda atenção a essa combinação e aos espaços das letras. [termdetalhe] Peça ao fornecedor os limites aplicáveis ao cunho, à folha e ao suporte escolhidos, sem adotar uma espessura mínima universal. Simplificar, abrir espaços ou separar elementos pode ajudar, mas qualquer alteração ao logótipo deve ser aprovada antes de produzir o cunho.'),
        ('Resultado e limitações',
         'O resultado combina o acabamento da folha com a superfície do artigo. Pode ficar uma ligeira marca de pressão; um relevo ou baixo-relevo pronunciado exige uma preparação própria e não deve ser prometido como consequência automática da folha. [termintro] Aderência e definição devem ser verificadas numa amostra. Não confunda brilho inicial com resistência ao manuseamento.\n\n'
         'A escolha de cores está ligada às folhas e às operações previstas. Confirme a viabilidade de combinar acabamentos e de manter o alinhamento pretendido. Textura, acesso à superfície e posição podem limitar a aplicação, mesmo quando o material de base parece adequado.\n\n'
         'A produção do cunho e a preparação da máquina fazem parte do trabalho. A Foilco distingue materiais de cunho com custos de fabrico diferentes. [termcunho] Pergunte se há cobrança de cunho ou preparação, o que acontece se a arte mudar e em que condições o cunho poderá ser reutilizado. Não se deduz daqui um preço, prazo ou quantidade mínima.'),
        ('O que confirmar antes de avançar',
         'Reúna as decisões abaixo antes da aprovação. Uma maquete permite conferir posição e desenho; uma amostra estampada permite avaliar o efeito no suporte. Combine os critérios de aceitação com o fornecedor e registe qual foi a prova aprovada.'),
        ('Comparar com alternativas',
         'Consulte gravação a laser quando o objetivo for uma marca resultante da alteração da superfície, em material devidamente identificado e compatível. Para imagens multicolores, a impressão digital UV pode ser uma alternativa a avaliar; para aplicação de tinta através de tela, compare serigrafia. Os guias relacionados explicam as condições próprias de cada processo.\n\n'
         'A decisão deve partir do artigo, da imagem e do acabamento desejado. Uma impressão a cores, uma gravação e uma folha metálica produzem resultados diferentes; nenhuma técnica é universalmente superior. Confirme as alternativas numa amostra quando a cor, o toque ou o detalhe forem decisivos.'),
    ],
    'passos': [
        'Arte: aprovar desenho, dimensão e posição.',
        'Cunho: produzir a ferramenta correspondente ao desenho.',
        'Montagem: apoiar a peça e posicionar a folha sob o cunho.',
        'Transferência: aplicar calor e pressão durante o contacto definido.',
        'Prova: separar o filme e avaliar cobertura, contornos e suporte.',
    ],
    'checklist': [
        ('Suporte', 'Artigo, material, revestimentos, textura e sensibilidade ao calor; confirmar numa peça real.'),
        ('Área e posição', 'Dimensão final, orientação, acesso e apoio da zona a estampar.'),
        ('Folha', 'Referência, cor e efeito; confirmar disponibilidade e adequação ao suporte.'),
        ('Arte e cunho', 'Detalhe mínimo positivo e negativo, letras e espaços; aprovar adaptações e versão do ficheiro.'),
        ('Amostra e uso', 'Prova no artigo ou suporte representativo acordado; avaliar marca de pressão, aderência e resistência ao manuseamento previsto.'),
        ('Condições comerciais', 'Custo do cunho e preparação, se aplicável; reutilização, prazos e restantes condições a acordar com o fornecedor.'),
    ],
    'problemas': [
        ('Transferência incompleta', 'Zonas sem folha podem justificar a revisão do contacto e da planicidade do cunho, da formulação da folha e dos parâmetros. O manual Astor apresenta várias causas possíveis; não basta concluir que falta temperatura. Peça análise do conjunto cunho, folha, material e máquina. [termfalhas]'),
        ('Contornos pouco definidos ou espaços fechados', 'Compare com a arte aprovada à escala final. Pormenores demasiado próximos, folha inadequada ao detalhe ou condições de transferência podem interferir com os contornos. O guia Howard relaciona impressão esbatida com temperatura e tempo de contacto; isso é uma hipótese a verificar, não um diagnóstico à distância. [termdetalhe] [termtempo]'),
        ('Marcas excessivas ou dano no suporte', 'Uma impressão demasiado marcada, deformação ou aspeto queimado exige interromper a aprovação e avaliar a amostra. Pressão e calor excessivos são possibilidades indicadas no manual Astor. Confirme também a adequação do suporte e da folha, sem prescrever uma correção antes de examinar a peça. [termfalhas]'),
        ('Aderência ou aspeto irregulares', 'Reveja limpeza, revestimento, textura e apoio da superfície com o fornecedor. Em cartão, a Iggesund destaca a influência da superfície e das suas irregularidades. A aparência, por si só, não permite prometer resistência: acorde um ensaio representativo do manuseamento. [termpapel]'),
    ],
    'fontes': list(FONTES_TERMOGRAVURA),
    'relacionados': ['gravacao-a-laser', 'impressao-uv', 'serigrafia', 'papel-e-cartao', 'pele-e-imitacao-de-pele', 'como-preparar-um-logotipo', 'como-avaliar-uma-maquete'],
    'ancoras': ['tecnicas/index.html#gravacao', 'produtos/index.html#escritorio'],
    'tags': 'termogravura estampagem a quente hot foil stamping foil blocking cunho molde folha dourado prateado holografico agenda capa pele imitacao papel cartao calor pressao tempo contacto',
}
