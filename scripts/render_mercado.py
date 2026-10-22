"""Reutiliza cartões, tipografia e índice de leitura da biblioteca."""
from html import escape
from urllib.parse import quote
from conteudos.mercado import TEMAS, AREAS, DATA, FONTES_MERCADO
from conteudos.mercado_areas import ASSOCIACOES, NOTAS_FONTES
from conteudos.mercado_imagens import IMAGENS, LEGENDAS, destino
from conteudos.mercado_empresas import EMPRESAS, EXEMPLOS, LOGOS
from conteudos.mercado_modelos import MODELOS_POR_ID
from scripts.render_mercado_modelos import entrada_modelos, pagina_modelo

def logo_empresa(id):
    if id not in LOGOS:
        return ''
    file, width, height, alt = LOGOS[id]
    return '<div class="market-company-logo"><img src="../assets/mercado/Empresas/'+quote(file, safe='/')+'" width="'+str(width)+'" height="'+str(height)+'" alt="'+escape(alt, quote=True)+'" loading="lazy" decoding="async"></div>'

def ficha_empresa(a):
    if not a.get('ficha'):
        return ''
    items = ''.join('<div><dt>'+escape(label)+'</dt><dd>'+escape(value)+'</dd></div>' for label,value in a['ficha'])
    return '<aside class="market-profile-summary" aria-label="Ficha-resumo da empresa">'+logo_empresa(a['id'])+'<dl>'+items+'</dl></aside>'

def exemplos_empresas(a, link):
    ids = EXEMPLOS.get(a['id'], [])
    if not ids:
        return ''
    cards = ''
    for id in ids:
        company = EMPRESAS[id]
        activity, refs = ASSOCIACOES.get(a['id'], {}).get(id, (company['atividade'], company['fontes']))
        logo = ''
        if id in LOGOS:
            file, width, height, alt = LOGOS[id]
            logo = '<div class="market-company-logo"><img src="../assets/mercado/Empresas/'+quote(file, safe='/')+'" width="'+str(width)+'" height="'+str(height)+'" alt="'+escape(alt, quote=True)+'" loading="lazy" decoding="async"></div>'
        local = '<p class="market-company-location">'+escape(company['local'])+'</p>' if company['local'] else ''
        sources = ' · '.join(link('#fonte-'+key, FONTES_MERCADO[key][0]) for key in refs)
        cards += '<article class="market-company"><header class="market-company-heading">'+logo+'<span class="eyebrow">Exemplo documentado</span><h3>'+escape(company['nome'])+'</h3>'+local+'</header><div class="market-company-copy"><p class="market-company-role">'+escape(company['papel'])+'</p><p>'+escape(activity)+'</p><a class="link market-company-profile" href="'+id+'.html">Ler o perfil de '+escape(company['nome'])+' →</a><p class="market-company-sources">Fontes: '+sources+'</p></div></article>'
    return '<section id="empresas" class="market-examples"><h2>Empresas com atividade documentada nesta área</h2><p class="market-examples-intro">Exemplos para compreender funções e modelos de trabalho. As atividades são atribuídas às fontes oficiais consultadas; não constituem uma recomendação comercial.</p><div class="market-company-grid">'+cards+'</div></section>'

def cartao(a, card, prefix='../'):
    if a['id'] not in IMAGENS:
        return card(a, prefix)
    _, width, height, alt = IMAGENS[a['id']]['cartao']
    image_class = 'market-card-image market-area-image' if a['tipo']=='area-mercado' else 'market-card-image'
    image = '<img class="'+image_class+'" src="'+prefix+destino(a['id'], 'cartao')+'" width="'+str(width)+'" height="'+str(height)+'" alt="'+escape(alt, quote=True)+'" loading="lazy" decoding="async">'
    return '<a class="topic content-card market-card" href="'+prefix+'mercado/'+a['id']+'.html">'+image+'<span class="eyebrow">Mercado</span><h3>'+escape(a['titulo'])+'</h3><p>'+escape(a['resumo'])+'</p><span class="arrow" aria-hidden="true">↗</span></a>'

def imagem_corpo(a):
    if a['id'] not in IMAGENS or 'corpo' not in IMAGENS[a['id']]:
        return ''
    _, width, height, alt = IMAGENS[a['id']]['corpo']
    return '<figure class="market-body-image"><img src="../'+destino(a['id'], 'corpo')+'" width="'+str(width)+'" height="'+str(height)+'" alt="'+escape(alt, quote=True)+'" loading="lazy" decoding="async"><figcaption>'+escape(LEGENDAS[a['id']])+'</figcaption></figure>'

def entrada(shell, card):
    return entrada_modelos(shell,EMPRESAS,FONTES_MERCADO,logo_empresa,AREAS,TEMAS)


def pagina(a, shell, card, by_id, link):
    if a['id'] in MODELOS_POR_ID:
        return pagina_modelo(MODELOS_POR_ID[a['id']],shell,EMPRESAS,FONTES_MERCADO,logo_empresa)
    data_consulta=a.get('data_consulta',DATA)
    data_texto=a.get('data_consulta_texto','14 de outubro de 2026')
    section_ids = a.get('ids_seccoes', ['parte-'+str(n) for n in range(1,len(a['seccoes'])+1)])
    sections = ''
    for n,(title,text) in enumerate(a['seccoes']):
        refs = a.get('fontes_seccoes', [[] for _ in a['seccoes']])[n]
        evidence = '<p class="market-section-sources">Fontes desta secção: '+' · '.join(link('#fonte-'+key,FONTES_MERCADO[key][0]) for key in refs)+'</p>' if refs else ''
        sections += '<section id="'+section_ids[n]+'"><h2>'+escape(title)+'</h2>'+''.join('<p>'+escape(p)+'</p>' for p in text.split('\n\n'))+evidence+'</section>'
    thematic = a['id'] in EXEMPLOS
    # Introdução breve, exemplos visuais e aprofundamento mantêm as âncoras antigas.
    examples = exemplos_empresas(a, link)
    sections = examples + sections.replace('</section>', '</section>'+imagem_corpo(a), 1)
    toc = (link('#empresas','Empresas neste segmento') if thematic else '') + ''.join(link('#'+id,title) for id,(title,_) in zip(section_ids,a['seccoes'])) + link('#fontes','Fontes e âmbito')
    source_keys = list(dict.fromkeys(a['fontes'] + [key for id in EXEMPLOS.get(a['id'], []) for key in ASSOCIACOES.get(a['id'], {}).get(id, ('',EMPRESAS[id]['fontes']))[1]]))
    sources = ''.join('<li id="fonte-'+key+'">'+link(FONTES_MERCADO[key][1],FONTES_MERCADO[key][0])+' — consulta: <time datetime="'+data_consulta+'">'+data_texto+'</time>.'+(' '+escape(NOTAS_FONTES[key]) if key in NOTAS_FONTES else '')+'</li>' for key in source_keys)
    website = '<p>'+link(a['site'], 'Visitar o site de '+a['titulo'].split(':')[0])+'</p>' if a.get('site') else ''
    source_body = '<section id="fontes"><h2>Fontes e âmbito</h2><p>Fontes oficiais consultadas para as atividades atribuídas às empresas. As explicações das funções e do percurso são sínteses editoriais; não descrevem um modelo universal nem avaliam o desempenho dos fornecedores.</p><ul class="sources">'+sources+'</ul>'+website+'</section>'
    profile_areas = [area for area in AREAS if a.get('ficha') and a['id'] in ASSOCIACOES[area['id']]]
    parent = link(profile_areas[0]['id']+'.html',profile_areas[0]['titulo'])+' / ' if profile_areas else ''
    area_links = '<nav class="context-links" aria-label="Áreas deste perfil">'+''.join(link(area['id']+'.html',area['titulo']) for area in profile_areas)+'</nav>' if profile_areas else ''
    intro = '<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / <a href="index.html">Mercado</a> / '+parent+escape(a['titulo'].split(':')[0])+'</nav><div class="page-intro"><span class="eyebrow">'+escape(a.get('categoria','Área de produto' if a['tipo']=='area-mercado' else 'Cadeia de fornecimento'))+'</span><h1>'+escape(a['titulo'])+'</h1><p>'+escape(a['resumo'])+'</p><div class="review">Consulta das fontes: <time datetime="'+data_consulta+'">'+data_texto+'</time></div></div>'+ficha_empresa(a)+area_links
    body = intro + '<div class="reading-layout"><aside class="contents"><strong>Neste artigo</strong><nav aria-label="Índice do artigo">'+toc+'</nav></aside><article class="reading">'+sections+source_body+'<a class="back-to-ideas" href="index.html">← Voltar a Mercado</a></article></div>'
    related_ids = [id for id in a['relacionados'] if id not in EXEMPLOS.get(a['id'], [])]
    if thematic:
        collection = AREAS if a['tipo']=='area-mercado' else TEMAS
        related_ids += [topic['id'] for topic in collection if topic['id']!=a['id'] and topic['id'] not in related_ids][:2]
    body += '<section><h2>Continue a explorar</h2><div class="article-grid">'+''.join(cartao(by_id[id],card) for id in related_ids)+'</div></section>'
    return shell(a['titulo'],a['resumo'],body,'../','mercado',robots='index, follow')
