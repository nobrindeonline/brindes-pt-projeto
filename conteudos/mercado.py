"""Mercado: síntese editorial e perfis sustentados em fontes públicas."""
DATA = '2026-10-14'
FONTES_MERCADO = {
 'stricker': ('Stricker — Who we are', 'https://www.strickergroup.com/en/about-us'),
 'tejo': ('TejoBrinde — Missão', 'https://www.tejobrinde.pt/pt-pt/missao'),
 'th': ('TH Clothes — A marca', 'https://thclothes.com/pt/content/40-sobre-nos'),
 'roly': ('Roly — Perguntas frequentes', 'https://www.roly.eu/es/faq'),
 'roly_identidade': ('Roly — Identificação da sociedade', 'https://www.roly.eu/es/disclaimer'),
 'dimatur': ('Dimatur — Quem somos', 'https://www.dimatur.pt/Home/Index/178'),
 'dimatur_historia': ('Dimatur — História', 'https://www.dimatur.pt/Home/Index/174'),
 'eurovinil': ('Eurovinil — Sobre nós', 'https://www.eurovinil-sa.com/sobre-n%C3%B3s'),
 'solo': ('Solo midocean — About us', 'https://www.midocean.com/export/us/eur/content/about-us'),
 'solo_locais': ('Solo midocean — Locations', 'https://www.midocean.com/export/us/eur/content/locations'),
 'solo_preparacao': ('Solo midocean — Special handling', 'https://www.midocean.com/export/us/eur/content/special-handling'),
}

def artigo(id, titulo, resumo, seccoes, fontes, relacionados=(), **extra):
    return dict(id=id, sec='mercado', tipo='mercado', titulo=titulo, resumo=resumo,
                seccoes=seccoes, fontes=fontes, relacionados=list(relacionados),
                problemas=[], ancoras=[], tags=titulo, **extra)

PERFIS = [
 artigo('stricker', 'Stricker: desenvolvimento e distribuição a profissionais', 'Uma empresa sediada em Coimbra que documenta criação, desenvolvimento e distribuição de brindes para profissionais do setor.', [], [], ['desenvolvimento-e-marcas', 'distribuicao-e-importacao'], site='https://www.strickergroup.com/', categoria='Desenvolvimento e distribuição'),
 artigo('tejobrinde', 'TejoBrinde: fornecimento e alcance internacional', 'Um exemplo português de fornecimento de brindes com presença comercial identificada em Portugal e Espanha.', [], [], ['distribuicao-e-importacao'], site='https://www.tejobrinde.pt/', categoria='Fornecimento de brindes'),
 artigo('th-clothes', 'TH Clothes e Organizações Biscana: marca de vestuário', 'A distinção entre uma marca de vestuário promocional e a empresa que a detém, sediada na Batalha.', [], [], ['vestuario-promocional-profissional', 'desenvolvimento-e-marcas'], site='https://thclothes.com/', categoria='Marca e vestuário promocional'),
 artigo('roly', 'Roly e Gor Factory: vestuário e gestão de encomendas', 'Um exemplo ibérico de oferta têxtil com informação pública sobre stock, encomendas e expedição.', [], [], ['vestuario-promocional-profissional', 'logistica-e-encomendas'], site='https://www.roly.eu/', categoria='Vestuário e distribuição'),
 artigo('dimatur', 'Dimatur: materiais, consumíveis e equipamentos', 'Um fornecedor para comunicação visual e transformação, com sede logística e administrativa em Turquel, Portugal.', [], [], ['materias-primas-consumiveis-equipamentos'], site='https://dimatur.pt/', categoria='Materiais, consumíveis e equipamentos'),
 artigo('eurovinil', 'Eurovinil: fornecimento para comunicação visual', 'Venda e distribuição de consumíveis e equipamentos, acompanhadas de suporte técnico e formação.', [], [], ['materias-primas-consumiveis-equipamentos'], site='https://www.eurovinil-sa.com/', categoria='Consumíveis e equipamentos'),
 artigo('solo-midocean', 'Solo midocean: stock, impressão e preparação', 'Uma operação europeia que documenta instalações próprias de logística e impressão e serviços de preparação de pedidos.', [], [], ['personalizacao-impressao-acabamento', 'logistica-e-encomendas'], site='https://www.midocean.com/', categoria='Fornecimento, impressão e logística'),
]

TEMAS = [
 artigo('distribuicao-e-importacao', 'Distribuição e importação de brindes',
 'Como distinguir aquisição internacional, stock, distribuição profissional e revenda ao cliente final.', [
 ('Funções diferentes na mesma cadeia', 'Um distribuidor fornece produtos a outros profissionais ou empresas. Um importador introduz produtos adquiridos noutro mercado; essa função não implica fabrico próprio. Um revendedor acompanha o pedido do cliente final e pode articular produto, personalização e entrega. A mesma organização pode acumular funções, mas o nome comercial não confirma quais executa.'),
 ('Stock e fornecimento a profissionais', 'Stock é a quantidade armazenada para fornecimento. A existência de stock não assegura reserva para um pedido, nem disponibilidade de todas as variantes. A distribuição e a exportação documentadas nos exemplos não bastam para atribuir importação a todas as empresas do setor.'),
 ('Portugal, Ibéria e Europa', 'Uma empresa portuguesa pode fornecer outros países e recorrer a produção internacional. Uma operação ibérica pode combinar apoio comercial em português ou espanhol com armazéns noutro local. Uma rede europeia pode centralizar preparação e expedição. Para compreender o percurso concreto, identifique a entidade fornecedora, o local de stock, onde ocorre a personalização e de onde parte a encomenda. A localização, por si só, não demonstra qualidade ou superioridade.')],
 ['stricker', 'tejo', 'solo_locais'], ['stricker', 'tejobrinde', 'solo-midocean']),
 artigo('desenvolvimento-e-marcas', 'Desenvolvimento de produto e marcas próprias',
 'A diferença entre definir um produto, deter uma marca e fabricar o artigo.', [
 ('Marca, desenho e produção', 'Uma marca identifica uma oferta; o seu titular pode definir desenho, materiais, cores ou apresentação. Desenvolver um produto é estabelecer características e preparar a sua realização. Um produtor transforma materiais ou componentes no artigo físico. Estas funções podem estar reunidas ou repartidas entre organizações.'),
 ('O que os exemplos documentam', 'Intervir na definição do produto não demonstra que o titular da marca fabrica todos os artigos nas suas próprias instalações. Para distinguir desenvolvimento e produção, importa identificar quem define as características, quem transforma os materiais e que operações estão efetivamente documentadas.'),
 ('Como ler uma afirmação de origem', 'País da sede, país de desenho, origem dos materiais e país de fabrico não são equivalentes. Uma afirmação sobre um deles não prova os restantes. Quando não existe informação pública suficiente, a origem de produção deve ficar por esclarecer. A marca também não garante, por si só, exclusividade do desenho ou capacidade de personalização.')],
 ['stricker', 'th'], ['stricker', 'th-clothes']),
 artigo('vestuario-promocional-profissional', 'Vestuário promocional e profissional',
 'O papel das marcas e fornecedores têxteis na escolha, disponibilidade e preparação de peças.', [
 ('O fornecedor têxtil na cadeia', 'O vestuário promocional pode servir ações de comunicação e identificação. O vestuário profissional responde a um contexto de trabalho. O fornecedor pode definir modelos e disponibilizar variantes de cor e tamanho, enquanto outra entidade aplica impressão ou bordado. O uso profissional, por si só, não comprova uma função de proteção.'),
 ('Marcas e disponibilidade', 'Numa encomenda têxtil, a quantidade global deve ser desdobrada por modelo, cor e tamanho; a disponibilidade de uma variante não prova a das restantes. Uma entrada prevista no armazém também deve ser distinguida de uma quantidade já disponível para preparar o pedido.'),
 ('Da peça à personalização', 'A composição e a construção da peça condicionam a técnica e a área de aplicação. Uma costura, fecho ou bolso pode limitar o acesso. Antes da produção, importa definir a arte, validar uma maquete e confirmar a compatibilidade do processo. Estes são critérios gerais; os perfis não atribuem serviços de impressão que as fontes consultadas não esclarecem.')],
 ['th', 'roly', 'roly_identidade'], ['th-clothes', 'roly', 'materiais-texteis', 'bordado', 'transfers']),
 artigo('personalizacao-impressao-acabamento', 'Personalização, impressão e acabamento',
 'Quem aplica a identidade visual ao artigo e como essa operação se articula com o fornecimento.', [
 ('Transformar o artigo', 'Personalização é aplicar uma mensagem ou identidade ao produto. Pode envolver impressão, gravação ou bordado. Acabamento inclui operações que completam a apresentação ou a montagem. Uma oficina especializada pode receber artigos de terceiros; um fornecedor integrado pode disponibilizar produto e personalização no mesmo pedido.'),
 ('Operação própria ou externa', 'A integração de fornecimento e impressão não é universal: noutros pedidos, a personalização pode ser contratada a uma entidade distinta. Sem uma fonte explícita, não se atribui execução própria a um fornecedor. Mesmo quando existem instalações próprias, importa confirmar onde e por quem será executado o pedido concreto.'),
 ('Informação que acompanha o pedido', 'O artigo, a quantidade, a arte e a zona de aplicação precisam de estar definidos. A maquete representa a aplicação pretendida; não substitui um ensaio físico quando este é necessário. A aprovação da arte, a execução, o controlo e o acabamento devem ter responsáveis identificados. O percurso apresentado é uma síntese de operações possíveis, não a descrição de uma empresa específica.')],
 ['solo_locais'], ['solo-midocean', 'como-escolher-a-tecnica', 'como-avaliar-uma-maquete', 'montagem-e-acabamentos']),
 artigo('materias-primas-consumiveis-equipamentos', 'Matérias-primas, consumíveis e equipamentos',
 'Os fornecedores que disponibilizam materiais e meios para produzir e personalizar.', [
 ('Três tipos de fornecimento', 'Uma matéria-prima é um material que será transformado ou incorporado no artigo. Um consumível é utilizado durante a operação e precisa de reposição, como uma tinta ou película. Um equipamento executa uma operação, como imprimir, cortar ou prensar. Fornecer estes meios é uma função distinta de vender um brinde acabado.'),
 ('Exemplos a montante da produção', 'A cadeia dos brindes cruza-se com a comunicação visual e as artes gráficas no fornecimento de suportes, tintas, películas e equipamentos. Estar a montante da produção significa disponibilizar meios que outra organização pode transformar ou utilizar na personalização; não comprova a execução do artigo acabado.'),
 ('Compatibilidade e apoio técnico', 'A adequação de uma tinta, película ou suporte depende do processo e do material de destino. O apoio técnico e a formação podem ajudar a configurar a operação, mas não comprovam compatibilidade universal. Importa consultar a documentação do produto e realizar os ensaios necessários. O fornecimento de um material também não identifica automaticamente o seu fabricante.')],
 ['dimatur', 'eurovinil'], ['dimatur', 'eurovinil', 'plasticos', 'maquinas-e-processos']),
 artigo('logistica-e-encomendas', 'Logística e preparação de encomendas',
 'Do artigo disponível ao pedido preparado, identificado e entregue ao transportador.', [
 ('Um percurso possível', 'Depois de escolher o produto e confirmar a disponibilidade, o pedido pode seguir para validação da arte, personalização, controlo, montagem, embalagem e expedição. Controlo significa verificar o resultado face ao que foi definido. Algumas etapas podem ser executadas por empresas diferentes, repetidas ou dispensadas conforme o projeto.'),
 ('Preparação e expedição', 'Preparar pode incluir separar variantes, contar unidades, dobrar peças, compor conjuntos, embalar e identificar caixas. Expedir é encaminhar a encomenda para transporte; não equivale à entrega no destino. A informação sobre conteúdo, destino e identificação das caixas acompanha a passagem do armazém para o transportador.'),
 ('O que varia entre operações', 'O prazo total pode reunir espera pelo stock, aprovação da arte, produção, preparação e transporte. O país da sede não define esse percurso. Uma expedição internacional pode ter pontos de passagem diferentes de um envio local; compare a operação documentada, os destinos e os responsáveis, sem atribuir qualidade ao território.'),
 ('Serviço integrado e operador de transporte', 'Os exemplos usados documentam preparação integrada no fornecimento. Não representam perfis de transportadores ou operadores logísticos independentes. A página de serviços da Solo midocean indica que as opções variam por pedido e região; a disponibilidade precisa de confirmação para cada encomenda.')],
 ['solo_preparacao', 'roly', 'solo_locais'], ['solo-midocean', 'roly', 'da-ideia-a-entrega', 'montagem-embalagem-expedicao']),
]
from conteudos.perfis_mercado import FONTES_PERFIS, DADOS_PERFIS, aprofundar
from conteudos.mercado_areas import AREAS, ASSOCIACOES, FONTES_AREAS
from conteudos.mercado_novos_perfis import NOVOS, FONTES_EXTRA
FONTES_MERCADO.update(FONTES_PERFIS)
FONTES_MERCADO.update(FONTES_AREAS)
FONTES_MERCADO.update(FONTES_EXTRA)
DADOS_PERFIS.update(NOVOS)
for id, data in NOVOS.items():
    PERFIS.append(artigo(id, data['nome']+': atividade e modelo de fornecimento', data['resumo'], [], [],
                        site=data['site'], categoria=data['papel']))
aprofundar(PERFIS)
for profile in PERFIS:
    areas = [a['id'] for a in AREAS if profile['id'] in ASSOCIACOES[a['id']]]
    profile['relacionados'] = areas + [id for id in profile['relacionados'] if id not in areas]
MERCADO = AREAS + TEMAS + PERFIS
