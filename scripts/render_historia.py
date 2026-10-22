"""Cronologia e galeria da página existente de História, com âncoras preservadas."""
from html import escape
from conteudos.historia_brindes import CRONOLOGIA, GALERIA, BASE


def corpo_historia(a, prose, link):
    def paragrafos(text):
        return ''.join('<p>'+prose(p)+'</p>' for p in text.split('\n\n'))

    sections=[]
    for n,(title,text) in enumerate(a['seccoes']):
        content=paragrafos(text)
        if n==2:
            items=''
            for p in CRONOLOGIA:
                items+=('<li id="'+p['id']+'"><div class="history-era"><h3>'+escape(p['titulo'])+'</h3></div>'
                    '<div class="history-era-copy">'
                    '<dl><dt>Meio e mensagem:</dt><dd>'+prose(p['meio'])+'</dd>'
                    '<dt>Objetos e relação com o público:</dt><dd>'+prose(p['objeto'])+'</dd></dl></div></li>')
            content='<p>Marcos selecionados de contextos diferentes. As datas indicam o âmbito de cada exemplo; os meios continuaram a coexistir.</p><ol class="history-timeline">'+items+'</ol>'
        elif n==3:
            items=''
            for p in GALERIA:
                sources=' · '.join(link('#fonte-'+key, 'Fonte histórica '+str(i+1)) for i,key in enumerate(p['fontes']))
                items+=('<article id="'+p['id']+'" class="history-object"><div class="history-object-heading">'
                    '<p class="eyebrow">'+escape(p['periodo'])+'</p><h3>'+escape(p['titulo'])+'</h3></div>'
                    '<figure><div class="history-object-image"><img src="../'+BASE+p['ficheiro']+'" width="'+str(p['width'])+'" height="'+str(p['height'])+'" alt="'+escape(p['alt'],quote=True)+'" loading="lazy" decoding="async"></div>'
                    '<figcaption>'+escape(p['legenda'])+' '+sources+' · <a href="../creditos-imagens.html#historia-objetos">Créditos da imagem</a></figcaption></figure>'
                    '<div class="history-object-copy">'+paragrafos(p['texto'])+'</div></article>')
            content='<p>Do apoio comemorativo aos objetos úteis com publicidade. A ordem começa pelos contextos documentados; as réguas sem data confirmada fecham o conjunto sem lhes atribuir uma posição cronológica exata.</p><div class="history-gallery">'+items+'</div>'
        elif n==5:
            content+='<div class="context-links">'+link('../materiais/index.html','Conhecer os materiais')+link('../guias/produto-standard-ou-a-medida.html','Produto standard ou à medida?')+'</div>'
        elif n==7:
            content+='<div class="context-links">'+link('da-ideia-a-entrega.html','Da ideia à entrega')+link('maquinas-e-processos.html','Máquinas e processos')+'</div>'
        sections.append('<section id="parte-'+str(n)+'"><h2>'+escape(title)+'</h2>'+content+'</section>')
    return ''.join(sections)
