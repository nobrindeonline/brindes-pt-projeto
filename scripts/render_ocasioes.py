"""Apresentação de Ocasiões, com os componentes partilhados da biblioteca."""
from html import escape
import json
import re
from conteudos.ocasioes import OCASIOES, FONTES_OCASIOES, SECCAO_OCASIOES, DATA

def texto(valor):
    def referencia(match):
        f = FONTES_OCASIOES[match[1]]
        return '<a class="source-ref" href="' + escape(f['url'], quote=True) + '" aria-label="Fonte: ' + escape(f['entidade'], quote=True) + '">Fonte</a>'
    return re.sub(r'\[([a-z]+)\]', referencia, escape(valor))

def media(a, legenda=False):
    f = a['imagem'] if legenda else a.get('imagem_cartao', a['imagem'])
    imagem = '<img src="../' + escape(f['url'], quote=True) + '" alt="' + escape(f['alt'], quote=True) + '" width="' + str(f['width']) + '" height="' + str(f['height']) + '" loading="lazy" decoding="async">'
    if legenda:
        return '<figure class="product-illustration"><div class="product-illustration-frame">' + imagem + '</div></figure>'
    return '<figure class="idea-media product-media"><div class="idea-images">' + imagem + '</div></figure>'

def entrada(shell, link):
    cards = ''.join('<article class="idea-card occasion-card" id="' + a['id'] + '">' + media(a) + '<div class="idea-card-copy"><span class="eyebrow">Época e contexto</span><h2>' + escape(a['titulo']) + '</h2><p>' + escape(a['resumo']) + '</p><a class="link idea-read-more" href="' + a['id'] + '.html">Explorar ' + escape(a['titulo']) + ' <span aria-hidden="true">→</span></a></div></article>' for a in OCASIOES)
    intro = '<nav class="crumb" aria-label="Percurso">' + link('../index.html','Início') + ' / Ocasiões e Sazonalidade</nav><div class="page-intro"><span class="eyebrow">Escolher pelo momento</span><h1>Ocasiões e Sazonalidade</h1><p>Uma época ajuda a formular perguntas: quem participa, onde será usado o artigo e como chega à pessoa certa? Explore contextos, tradições documentadas e critérios de escolha, sem tratar uma oferta como regra da celebração.</p></div>'
    ajuda = '<section class="note"><h2>Relacionar ocasião e destinatário</h2><p>Esta secção trata épocas e celebrações. Os públicos e setores continuam em Para quem; as características dos artigos encontram-se em Produtos.</p><div class="context-links">' + link('../publicos/index.html','Para quem') + link('../produtos/index.html','Produtos') + '</div></section>'
    return shell(SECCAO_OCASIOES['titulo'], SECCAO_OCASIOES['resumo'], intro + '<div class="ideas-grid occasion-grid">' + cards + '</div>' + ajuda, '../', 'ocasioes')

def pagina(a, artigos, shell, link, card):
    sections = [(s['id'], s['titulo'], ''.join('<p>' + texto(p) + '</p>' for p in s['paragrafos'])) for s in a['conteudo']]
    if a.get('exemplos'):
        exemplos = '<p>Estes exemplos relacionam objetos com uma utilização concreta. A escolha depende de quem participa e das condições da atividade; as imagens não comprovam materiais, desempenho ou adequação.</p>'
        for e in a['exemplos']:
            relacionado = artigos[e['relacionado']]
            exemplos += '<article class="audience-family occasion-example" id="' + e['id'] + '"><h3>' + escape(e['titulo']) + '</h3>' + media({'imagem':e['imagem']}, True)
            for chave, label in [('contexto','Contexto'), ('motivo','Razão da escolha'), ('confirmar','Aspetos a confirmar')]:
                exemplos += '<p><strong>' + label + '</strong><br>' + texto(e[chave]) + '</p>'
            exemplos += '<p>' + link('../' + relacionado['sec'] + '/' + relacionado['id'] + '.html', 'Aprofundar: ' + relacionado['titulo']) + '</p></article>'
        posicao = next((i for i,s in enumerate(sections) if s[0]=='escolha'), len(sections))
        sections.insert(posicao, ('exemplos','Exemplos em contexto',exemplos))
    faq = ''.join('<details class="guide-faq"><summary>' + escape(p) + '</summary><p>' + texto(r) + '</p></details>' for p, r in a['perguntas_frequentes'])
    sections.append(('faq','Perguntas frequentes',faq))
    toc = ''.join(link('#' + id, title) for id, title, _ in sections)
    intro = '<nav class="crumb" aria-label="Percurso">' + link('../index.html','Início') + ' / ' + link('index.html','Ocasiões e Sazonalidade') + ' / <span>' + escape(a['titulo']) + '</span></nav><div class="page-intro"><span class="eyebrow">Ocasiões e Sazonalidade</span><h1>' + escape(a['titulo']) + '</h1><p>' + escape(a['resumo']) + '</p></div>'
    body = ''.join('<section id="' + id + '"><h2>' + title + '</h2>' + content + '</section>' for id, title, content in sections)
    relacionados = '<section id="relacionados"><h2>Conteúdos relacionados</h2><div class="article-grid">' + ''.join(card(artigos[id], '../') for id in a['relacionados']) + '</div></section>'
    outras = '<section><h2>Outras ocasiões</h2><div class="context-links">' + ''.join(link(b['id'] + '.html', b['titulo']) for b in OCASIOES if b['id'] != a['id']) + '</div></section>'
    return shell(a['titulo'], a['resumo'], intro + '<div class="reading-layout"><aside class="contents"><strong>Neste guia</strong><nav aria-label="Índice do artigo">' + toc + '</nav></aside><article class="reading">' + media(a, True) + body + '</article></div>' + relacionados + outras + link('index.html','← Voltar a Ocasiões e Sazonalidade'), '../', 'ocasioes')

def dados():
    return json.dumps(dict(schema_version='1.0', idioma='pt-PT', data_revisao=DATA,
        secao=SECCAO_OCASIOES['titulo'], fontes=FONTES_OCASIOES,
        artigos=[dict({k:v for k,v in a.items() if k not in ('seccoes','problemas','ancoras')},
                      url='ocasioes/' + a['id'] + '.html') for a in OCASIOES]), ensure_ascii=False, indent=2) + '\n'
