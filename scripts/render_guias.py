"""HTML, pesquisa e JSON público derivados da fonte revista dos Guias."""
from html import escape
from datetime import date
import copy
import json
import re
from conteudos.guias import GUIAS, GRUPOS_GUIAS, FONTES_GUIAS_META, DATA_REVISAO_GUIAS, INTRO_GUIAS, RESUMO_GUIAS
from conteudos.guias_imagens import fotos_publicas_guias

GUIAS_POR_ID={g['id']:g for g in GUIAS}

def data_pt(valor):
    parsed=date.fromisoformat(valor)
    months=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    return f'{parsed.day} de {months[parsed.month-1]} de {parsed.year}'


def referencias(texto):
    return re.sub(r'\[([a-z]+)\]',lambda m:'<a class="source-ref" href="#fonte-'+m[1]+
        '" aria-label="Fonte: '+escape(FONTES_GUIAS_META[m[1]]['entidade'])+'">↗</a>',escape(texto))


def diagrama_vetor():
    quadrados=''.join(f'<rect x="{x*10}" y="{y*10}" width="10" height="10" fill="#1686db"/>'
        for x,y in [(2,0),(3,0),(1,1),(4,1),(0,2),(5,2),(0,3),(5,3),(1,4),(4,4),(2,5),(3,5)])
    return ('<figure class="guide-concept"><div class="guide-vector-compare">'
        '<div><svg viewBox="0 0 60 60" role="img" aria-label="Contorno circular formado por quadrados visíveis">'+quadrados+'</svg><strong>Raster</strong><p>Imagem composta por píxeis.</p></div>'
        '<div><svg viewBox="0 0 60 60" role="img" aria-label="Contorno circular desenhado por uma curva contínua"><circle cx="30" cy="30" r="24" fill="none" stroke="#1686db" stroke-width="6"/></svg><strong>Vetor</strong><p>Formas descritas por linhas e curvas.</p></div></div>'
        '<figcaption>Esquema original de estruturas diferentes, ampliadas para leitura. O formato do ficheiro não basta para identificar o seu conteúdo.</figcaption></figure>')


def esquema(g):
    if g['id']=='como-preparar-um-logotipo': return diagrama_vetor()
    if g['id']=='pantone-cmyk-e-cor-final':
        return '<figure class="guide-color"><div aria-hidden="true"><span>C</span><span>M</span><span>Y</span><span>K</span></div><figcaption>Ciano, magenta, amarelo e preto: componentes CMYK. As cores deste esquema de ecrã não são uma prova física nem uma conversão de uma referência Pantone.</figcaption></figure>'
    if g['id']=='como-escolher-o-material':
        return '<figure class="guide-concept"><div class="guide-layers"><strong>Superfície da aplicação</strong><span>Pintura, verniz ou outro revestimento, se existir</span><span>Material de base e componentes</span></div><figcaption>Esquema de camadas possíveis. Identifique o que existe no artigo concreto e em que camada ficará a marca.</figcaption></figure>'
    steps=''.join('<li><strong>'+escape(t)+'</strong><span>'+escape(p)+'</span></li>' for t,p in g['esquema_guia'])
    return '<figure class="guide-diagram"><ol>'+steps+'</ol><figcaption>Mapa de leitura: '+escape(g['titulo'])+'.</figcaption></figure>'


def imagem(f, cartao=False):
    image='<img src="../'+escape(f['url'],quote=True)+'" alt="'+escape(f['alt'],quote=True)+'" width="'+str(f['width'])+'" height="'+str(f['height'])+'" loading="lazy" decoding="async">'
    if cartao: return '<div class="guide-cover guide-cover-photo">'+image+'</div>'
    return '<figure class="guide-photo"><div>'+image+'</div><figcaption>'+escape(f['legenda'])+' <a href="../creditos-imagens.html#guias-ilustrativos">Créditos da imagem</a></figcaption></figure>'


def capa_conceito(g):
    if g['id']=='como-preparar-um-logotipo':
        return '<div class="guide-cover guide-cover-original" aria-label="Esquema original: ficheiro, dimensão final e versão"><span>Ficheiro</span><b aria-hidden="true">→</b><span>Dimensão final</span><b aria-hidden="true">→</b><span>Versão</span></div>'
    return '<div class="guide-cover guide-cover-original" aria-label="Esquema original: sinal, verificação e evidência"><span>Sinal</span><b aria-hidden="true">→</b><span>Verificação</span><b aria-hidden="true">→</b><span>Evidência</span></div>'


def entrada_guias(shell,link):
    images=fotos_publicas_guias()
    content='<div class="guides-index"><nav class="crumb" aria-label="Percurso">'+link('../index.html','Início')+' / Guias</nav><div class="page-intro"><span class="eyebrow">Da dúvida à decisão</span><h1>Guias práticos</h1><p>'+escape(INTRO_GUIAS)+'</p></div>'
    content+='<nav class="context-links" aria-label="Percursos dos guias">'+''.join(link('#'+id,title) for id,title,_,_ in GRUPOS_GUIAS)+'</nav>'
    for id,title,description,theme in GRUPOS_GUIAS:
        cards=''
        for g in GUIAS:
            if g['tema']!=theme: continue
            cover=imagem(images[g['id']]['cartao'],True) if g['id'] in images else capa_conceito(g)
            cards+='<article class="idea-card guide-card">'+cover+'<div class="idea-card-copy"><span class="eyebrow">Guia prático</span><h3>'+escape(g['titulo'])+'</h3><p>'+escape(g['resumo'])+'</p><a class="link idea-read-more" href="'+g['id']+'.html" aria-label="Ler guia: '+escape(g['titulo'],quote=True)+'">Ler guia <span aria-hidden="true">→</span></a></div></article>'
        content+='<section id="'+id+'" class="guide-group"><div class="section-head"><div><h2>'+escape(title)+'</h2><p>'+escape(description)+'</p></div></div><div class="guide-index-grid">'+cards+'</div></section>'
    content+='</div>'
    return shell('Guias práticos',RESUMO_GUIAS,content,'../','guias')


def artigo_guia(g, artigos, shell, link):
    photos=fotos_publicas_guias().get(g['id'],{}).get('artigo',[])
    section_ids=g.get('ids_seccoes',[f'parte-{n}' for n in range(len(g['seccoes']))])
    sections=[]
    for id,(title,text) in zip(section_ids,g['seccoes']):
        parts=''.join('<p>'+referencias(p)+'</p>' for p in text.split('\n\n'))
        parts+=''.join(imagem(f) for f in photos if f['secao']==id)
        sections.append((id,title,parts))
    if g['casos']:
        casos=[]
        for c in g['casos']:
            text='<dl class="guide-case"><dt>Sinal observado</dt><dd>'+referencias(c['sinal'])+'</dd><dt>Pontos a verificar</dt><dd>'+referencias(c['verificar'])+'</dd><dt>Evidência a reunir</dt><dd>'+referencias(c['evidencia'])+'</dd></dl>'
            casos.append((c['id'],c['titulo'],text))
        sections=[sections[0],*casos,*sections[1:]]
    errors='<div class="troubleshooting">'+''.join('<div><h3>'+escape(t)+'</h3><p>'+referencias(p)+'</p></div>' for t,p in g['problemas'])+'</div>'
    sections.append(('problemas','Erros frequentes e prevenção',errors))
    checklist='<ul class="guide-checklist">'+''.join('<li>'+escape(p)+'</li>' for p in g['confirmar'])+'</ul>'
    if g['id']=='como-escolher-a-tecnica': checklist='<span id="parte-6" class="anchor-alias"></span>'+checklist
    sections.append(('confirmar','Lista de verificação antes de avançar',checklist))
    faq=''.join('<details class="guide-faq"><summary>'+escape(f['pergunta'])+'</summary><p>'+referencias(f['resposta'])+'</p></details>' for f in g['perguntas_frequentes'])
    sections.append(('faq','Perguntas frequentes',faq))
    sources='<p>Os passos e as listas são recomendações editoriais. As fontes sustentam os princípios identificados; condições de artigo, material, arte e processo precisam de confirmação específica.</p><ul class="sources">'
    for key in g['fontes']:
        f=FONTES_GUIAS_META[key]
        sources+='<li id="fonte-'+key+'">'+link(f['url'],f['titulo'])+'<br>'+escape(f['entidade'])+' · Consulta: <time datetime="'+f['data_consulta']+'">'+data_pt(f['data_consulta'])+'</time><p>'+escape(f['ambito'])+'</p></li>'
    sections.append(('fontes','Fontes, âmbito e revisão',sources+'</ul><p class="documentary-date">Conteúdo revisto em <time datetime="'+g['data_revisao']+'">'+data_pt(g['data_revisao'])+'</time>.</p>'))
    toc=''.join(link('#'+id,title) for id,title,_ in sections)
    body='<section id="resposta" class="guide-answer"><h2>Resposta breve</h2><p>'+referencias(g['resposta_breve'])+'</p></section>'+esquema(g)
    body+=''.join('<section id="'+id+'"><h2>'+escape(title)+'</h2>'+text+'</section>' for id,title,text in sections)
    intro='<nav class="crumb" aria-label="Percurso">'+link('../index.html','Início')+' / '+link('index.html','Guias')+' / <span>'+escape(g['titulo'])+'</span></nav><div class="page-intro"><span class="eyebrow">'+escape(g['tema'])+'</span><h1>'+escape(g['titulo'])+'</h1><p>'+escape(g['resumo'])+'</p><p class="documentary-date">Revisão documental: <time datetime="'+g['data_revisao']+'">'+data_pt(g['data_revisao'])+'</time></p></div>'
    content=intro+'<div class="reading-layout"><aside class="contents"><details id="guia-indice" class="guide-toc" open><summary>Neste guia</summary><nav aria-label="Índice do artigo">'+link('#resposta','Resposta breve')+toc+'</nav></details></aside><article class="reading guide-reading">'+body+'</article></div>'
    related=list(dict.fromkeys(g['relacionados']))
    content+='<section><h2>Guias relacionados</h2><div class="guide-related">'+''.join('<a href="'+id+'.html">'+escape(GUIAS_POR_ID[id]['titulo'])+' <span aria-hidden="true">→</span></a>' for id in related)+'</div><div class="context-links">'+''.join(link('../'+p['url'],p['titulo']) for p in g['links_contexto'])+'</div></section><a class="back-to-ideas" href="index.html">← Voltar aos Guias</a>'
    return shell(g['titulo'],g['resumo'],content,'../','guias',extra='<script src="../assets/js/guias.js" defer></script>')


def texto_guia(g):
    def textos(v):
        if isinstance(v,str): yield re.sub(r'\[[a-z]+\]','',v)
        elif isinstance(v,list):
            for x in v: yield from textos(x)
        elif isinstance(v,dict):
            for k,x in v.items():
                if k not in ('id','fontes','relacionados','ancoras','data_revisao','ids_seccoes','links_contexto'): yield from textos(x)
        elif isinstance(v,tuple):
            for x in v: yield from textos(x)
    return ' '.join(textos(g))


def dados_guias():
    photos=fotos_publicas_guias()
    result=[]
    def texto(text):
        keys=list(dict.fromkeys(re.findall(r'\[([a-z]+)\]',text)))
        return dict(texto=re.sub(r'\s*\[[a-z]+\]','',text),fontes=keys)
    for original in GUIAS:
        g=copy.deepcopy(original)
        ids=g.get('ids_seccoes',[f'parte-{n}' for n in range(len(g['seccoes']))])
        order=[ids[0],*[c['id'] for c in g['casos']],*ids[1:]] if g['casos'] else ids
        result.append(dict(id=g['id'],slug=g['id'],url='guias/'+g['id']+'.html',titulo=g['titulo'],
            categoria=g['tema'],resumo=g['resumo'],resposta_breve=texto(g['resposta_breve']),ordem_leitura=order,
            passos=[dict(id=id,titulo=t,**texto(p)) for id,(t,p) in zip(ids,g['seccoes'])],
            casos=[dict(id=c['id'],titulo=c['titulo'],sinal=texto(c['sinal']),verificar=texto(c['verificar']),evidencia=texto(c['evidencia'])) for c in g['casos']],
            erros=[dict(erro=t,prevencao=texto(p)) for t,p in g['problemas']],checklist=g['confirmar'],
            perguntas_frequentes=[dict(pergunta=f['pergunta'],resposta=texto(f['resposta'])) for f in g['perguntas_frequentes']],
            esquema=[dict(titulo=t,descricao=p) for t,p in g['esquema_guia']],
            relacionados=[dict(id=id,titulo=GUIAS_POR_ID[id]['titulo'],url='guias/'+id+'.html') for id in g['relacionados']],
            links_contexto=g['links_contexto'],fontes=[dict(id=k,**FONTES_GUIAS_META[k]) for k in g['fontes']],
            data_revisao=g['data_revisao'],imagens=photos.get(g['id'],{})))
    paths=[dict(id=id,titulo=t,resumo=d,guias=[g['id'] for g in GUIAS if g['tema']==theme]) for id,t,d,theme in GRUPOS_GUIAS]
    return json.dumps(dict(schema_version='1.0',idioma='pt-PT',site='brindes.pt',introducao=INTRO_GUIAS,
        data_revisao=DATA_REVISAO_GUIAS,percursos=paths,guias=result),ensure_ascii=False,indent=2)+'\n'
