"""Entrada de Mercado e páginas de modelos, centradas nas funções das empresas."""
from html import escape as e
from urllib.parse import quote
from conteudos.mercado_modelos import IMAGENS_CARTOES
from conteudos.mercado_modelos import CLASSIFICACOES, MODELOS, MODELOS_POR_ID, DESTAQUES, ETAPAS, ROTULOS, DATA_MODELOS


def fontes_empresa(c):
    return list(dict.fromkeys(k for keys in c['funcoes'].values() for k in keys))


def empresas(ids, companies, sources, logo):
    cards=''
    for id in ids:
        company=companies[id]; c=CLASSIFICACOES[id]
        tags=[ROTULOS[k] for k in c['funcoes'] if k!=c['principal']]
        if c.get('desenvolvimento'): tags.append('Desenvolvimento e desenho')
        tags=c.get('etiquetas',tags)
        secondary='<ul class="market-role-tags" aria-label="Outras atividades documentadas">'+''.join('<li>'+e(t)+'</li>' for t in tags)+'</ul>' if tags else ''
        place='<p class="market-company-location">'+e(company['local'])+'</p>' if company.get('local') else ''
        refs=' · '.join('<a href="'+e(sources[k][1],quote=True)+'">'+e(sources[k][0])+'</a>' for k in fontes_empresa(c))
        consulted='14 de outubro de 2026' if c.get('consulta') else '22 de outubro de 2026'
        cards+=('<article class="market-company"><header class="market-company-heading">'+logo(id)+'<h3>'+e(company['nome'])+'</h3>'+place+'</header>'
            '<div class="market-company-copy"><p class="market-company-role"><span>Atividade principal</span>'+e(ROTULOS[c['principal']])+'</p>'+secondary+
            '<p class="market-specialties"><strong>Especialidades:</strong> '+e(c['especialidades'])+'</p><p>'+e(c['texto'])+'</p>'
            '<details class="market-evidence"><summary>Âmbito e fontes da classificação</summary><p>'+e(c['limite'])+'</p><p>Fontes: '+refs+'</p>'
            '<p>Consulta: <time datetime="'+c.get('consulta',DATA_MODELOS)+'">'+consulted+'</time>.</p></details>'
            '<a class="link market-company-profile" href="'+id+'.html">Ler o perfil de '+e(company['nome'])+' →</a></div></article>')
    return '<div class="market-company-grid market-model-companies">'+cards+'</div>'


def cartoes():
    cards=''
    for n,a in enumerate(MODELOS,1):
        file,width,height,alt=IMAGENS_CARTOES[a['id']]
        visual='<img class="market-model-image" src="../assets/mercado/cartoes/'+a['id']+'/'+quote(file)+'" width="'+str(width)+'" height="'+str(height)+'" alt="'+e(alt,quote=True)+'" loading="lazy" decoding="async">'
        cards+=('<article class="market-model-card market-model-'+a['funcao']+'"><div class="market-model-top"><span class="market-model-number">0'+str(n)+'</span>'
            '<span>'+str(len(a['empresas']))+' exemplos documentados</span></div>'+visual+'<div class="market-model-copy"><h3>'+e(a['titulo'])+'</h3><p>'+e(a['resumo'])+'</p>'
            '<a href="'+a['id']+'.html" class="link">Explorar '+e(a['titulo'].lower())+' →</a></div></article>')
    return '<div class="market-model-grid">'+cards+'</div>'


def relacionados():
    return '<section class="market-related"><h2>Aprofundar os artigos, materiais e processos</h2><div class="context-links"><a href="../produtos/index.html">Produtos</a><a href="../materiais/index.html">Materiais</a><a href="../tecnicas/index.html">Técnicas</a><a href="../industria/da-ideia-a-entrega.html">Da ideia à entrega</a></div></section>'


def entrada_modelos(shell, companies, sources, logo, areas, temas):
    intro='<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / Mercado</nav><div class="page-intro market-model-intro"><span class="eyebrow">Empresas, funções e cadeia de fornecimento</span><h1>Quem faz o quê no mercado dos brindes?</h1><p>Conheça os modelos de atividade das empresas do setor: quem fornece artigos, quem fabrica, quem personaliza e quem combina várias funções. O objetivo é compreender o papel de cada interveniente e as etapas que executa ou articula.</p><nav class="context-links" aria-label="Explorar Mercado"><a href="#modelos">Modelos de atividade</a><a href="#empresas">Empresas em destaque</a><a href="#diretorio">Todas as empresas</a></nav></div>'
    stages=''.join('<li><span class="market-stage-number">0'+str(n)+'</span><h3>'+e(t)+'</h3><p>'+e(p)+'</p></li>' for n,(t,p) in enumerate(ETAPAS,1))
    chain='<section id="cadeia" class="market-chain"><div class="section-head"><div><h2>Como funciona a cadeia de fornecimento</h2><p>Etapas possíveis entre uma ideia e um objeto entregue.</p></div></div><ol>'+stages+'</ol><p class="market-chain-note">Nem todas as empresas realizam todas as etapas. A ordem pode variar: um artigo pode ser personalizado antes da distribuição, e preparação e transporte podem envolver entidades diferentes. Desenho e desenvolvimento não equivalem a fabrico.</p></section>'
    models='<section id="modelos" class="market-model-section"><div class="section-head"><div><span class="eyebrow">Quatro formas de participar no setor</span><h2>Modelos de atividade</h2><p>As funções podem sobrepor-se. Cada empresa mantém um único perfil e uma atividade principal editorial, com etiquetas para as restantes funções comprovadas.</p></div></div>'+cartoes()+'</section>'
    featured='<section id="empresas" class="market-featured"><div class="section-head"><div><h2>Empresas em destaque</h2><p>Uma seleção para ilustrar papéis diferentes, sem ranking ou recomendação comercial.</p></div></div>'+empresas(DESTAQUES,companies,sources,logo)+'</section>'
    directory='<section id="diretorio" class="market-directory"><h2>Todas as empresas documentadas</h2><p>Os '+str(len(CLASSIFICACOES))+' perfis existentes continuam disponíveis. A atividade principal orienta a leitura; as restantes funções estão identificadas nos modelos.</p><ul>'+''.join('<li><a href="'+id+'.html">'+e(companies[id]['nome'])+'</a><span>'+e(ROTULOS[c['principal']])+'</span></li>' for id,c in CLASSIFICACOES.items())+'</ul></section>'
    criteria='<section id="criterios" class="market-criteria"><h2>Critérios e fontes</h2><p>Distribuição disponibiliza artigos ou meios de produção; fabrico transforma materiais ou componentes; personalização aplica uma identidade ao artigo. Atividade mista combina duas ou mais destas funções documentadas. Desenvolvimento e desenho são descritos separadamente.</p><p>As classificações apoiam-se nas fontes institucionais ligadas em cada cartão e nos perfis. São declarações públicas atribuídas às empresas, sem avaliação independente do desempenho. Uma sede, marca ou imagem de equipamento não comprova o fabrico de toda a oferta. Quando a execução interna não está esclarecida, essa limitação é indicada.</p><p>Revisão desta organização: <time datetime="2026-10-22">22 de outubro de 2026</time>. Os perfis mantêm as suas datas documentais; a informação da XD Connects conserva a consulta anterior, identificada nas páginas de modelos.</p></section>'
    # Conserva os percursos anteriores como documentação complementar, sem cartões de produtos.
    guides='<details class="market-other-guides"><summary>Áreas de oferta e outros guias de Mercado</summary><p>Consulte os percursos anteriores por área de oferta e os temas complementares.</p><div class="context-links">'+''.join('<a href="'+a['id']+'.html">'+e(a['titulo'])+'</a>' for a in [*areas,*[a for a in temas if a['id'] not in MODELOS_POR_ID]])+'</div></details>'
    return shell('Mercado: empresas e modelos de atividade','Quem distribui, fabrica e personaliza brindes: quatro modelos de atividade, cadeia de fornecimento e perfis documentados de empresas.',intro+chain+models+featured+directory+criteria+guides+relacionados(),'../','mercado',robots='index, follow')


def pagina_modelo(a,shell,companies,sources,logo):
    intro='<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / <a href="index.html">Mercado</a> / <span>'+e(a['titulo'])+'</span></nav><div class="page-intro market-model-intro"><span class="eyebrow">Modelo de atividade</span><h1>'+e(a['titulo'])+'</h1><p>'+e(a['resumo'])+'</p></div>'
    context='<section id="parte-1" class="market-criteria"><h2>O papel destas empresas</h2><p>'+e(a['distincao'])+'</p><h3 id="parte-2">O que confirmar numa operação concreta</h3><p>'+e(a['pergunta'])+'</p><span id="parte-3" class="anchor-alias"></span></section>'
    cards='<section id="empresas"><h2>Empresas com funções documentadas</h2><p>A atividade principal identifica a classificação editorial. As etiquetas mostram funções adicionais. Leia o âmbito e as fontes de cada empresa para distinguir execução própria e serviços disponibilizados.</p>'+empresas(a['empresas'],companies,sources,logo)+'</section>'
    keys=list(dict.fromkeys(k for id in a['empresas'] for k in fontes_empresa(CLASSIFICACOES[id])))
    refs='<section id="fontes"><h2>Fontes e âmbito</h2><p>Revisão em 22 de outubro de 2026, com datas de consulta indicadas em cada empresa. A presença nesta página não certifica capacidade, origem ou disponibilidade para um pedido.</p><ul class="sources">'+''.join('<li id="fonte-'+k+'"><a href="'+e(sources[k][1],quote=True)+'">'+e(sources[k][0])+'</a></li>' for k in keys)+'</ul></section>'
    nav='<section><h2>Outros modelos de atividade</h2><div class="context-links">'+''.join('<a href="'+m['id']+'.html">'+e(m['titulo'])+'</a>' for m in MODELOS if m['id']!=a['id'])+'</div></section>'
    return shell(a['titulo'],a['resumo'],intro+context+cards+refs+nav+relacionados()+'<a class="back-to-ideas" href="index.html">← Voltar a Mercado</a>','../','mercado',robots='index, follow')
