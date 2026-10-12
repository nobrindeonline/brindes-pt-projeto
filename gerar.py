"""Gera HTML e pesquisa; formata as páginas com o Prettier local (npm ci)."""
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
from html import escape, unescape
import json
import re
import shutil
import subprocess
import argparse
import importlib.util
import sys
from neutralidade import pagina_publica, texto_publico, corrigir_ligacoes
from conteudos.produtos import PRODUTOS, textos_publicos
from render_produtos import POR_ID as FAMILIAS_PRODUTOS, render_guia, render_entrada, dados_publicos
from conteudos.produtos_imagens import CREDITOS as CREDITOS_PRODUTOS
from conteudos.catalogo import ARTIGOS, SECCOES, FONTES, DATA_REVISAO
from conteudos.recursos import FOTOS_TECNICAS, ARTIGO_PRODUTOS, GRUPO_PRODUTOS, POR_ID
from conteudos.apresentacao_recursos import tecnica, exemplos, creditos
from conteudos.ideias import IDEIAS
from conteudos.novidades import NOVIDADES
from conteudos.sublimacao import IMAGENS_SUBLIMACAO
from conteudos.publicos import PUBLICOS, PAGINAS_PRODUTOS
from conteudos.industria import INDUSTRIA, ETAPAS
from conteudos.tampografia import PASSOS as PASSOS_TAMPOGRAFIA, IMAGENS as IMAGENS_TAMPOGRAFIA
from conteudos.serigrafia import PASSOS as PASSOS_SERIGRAFIA
from conteudos.impressao_uv import PASSOS as PASSOS_UV, IMAGENS as IMAGENS_UV
from conteudos.guias import GRUPOS_GUIAS
from render_guias import GUIAS_POR_ID, entrada_guias, artigo_guia, texto_guia, dados_guias
from conteudos.guias_imagens import CREDITOS_GUIAS
from conteudos.materiais import MATERIAIS
from conteudos.bordado import IMAGENS_BORDADO
from conteudos.troquelagem import IMAGENS_TROQUELAGEM, OPERACOES as OPERACOES_TROQUELAGEM, PASSOS as PASSOS_TROQUELAGEM, FAQ as FAQ_TROQUELAGEM
from conteudos.crachas import IMAGEM_CRACHAS, COMPONENTES as COMPONENTES_CRACHAS, PASSOS as PASSOS_CRACHAS, FAQ as FAQ_CRACHAS
from conteudos.montagem import MONTAGEM, HUB_ID, BASE_IMAGENS, IMAGENS_MONTAGEM
from conteudos.transfers import IDS as TRANSFER_IDS, IMAGENS_TRANSFERS

ROOT = Path(__file__).resolve().parent
BY_ID = {a['id']: a for a in ARTIGOS}
SECS = {s['id']: s for s in SECCOES}
GROUP_LINKS = {
 ('materiais','plasticos'):['tampografia','impressao-uv'],
 ('materiais','metais'):['gravacao-a-laser','tampografia'],
 ('materiais','naturais'):['gravacao-a-laser'],
 ('materiais','texteis'):['bordado','serigrafia'],
 ('materiais','pele'):['como-escolher-a-tecnica'],
 ('materiais','vidro-ceramica'):['impressao-uv','como-escolher-a-tecnica'],
 ('produtos','canetas'):['canetas-e-escrita'],
 ('produtos','bebidas'):['garrafas-copos-e-canecas'],
 ('produtos','texteis'):['texteis'],
 ('produtos','sacos'):['sacos-e-mochilas'],
 ('produtos','tecnologia'):['tecnologia'],
 ('produtos','escritorio'):['artigos-de-escritorio'],
 ('produtos','premium'):['brindes-premium'],
 ('publicos','empresas'):['canetas-e-escrita'],
 ('publicos','municipios'):['canetas-e-escrita','como-escolher-a-tecnica'],
 ('publicos','escolas'):['canetas-e-escrita'],
 ('publicos','clubes'):['bordado','serigrafia'],
 ('publicos','revendedores'):['como-escolher-a-tecnica'],
 ('publicos','eventos'):['serigrafia','canetas-e-escrita'],
}
def url(a): return f"{a['sec']}/{a['id']}.html"

def corrigir_imagens_removidas(documento, path):
    """Retira só referências a imagens locais removidas, sem alterar os textos."""
    parent = (ROOT/path).parent
    def ausente(src):
        parsed = urlsplit(unescape(src))
        if parsed.scheme or parsed.netloc: return False
        target = (parent/unquote(parsed.path)).resolve()
        return (target.is_relative_to(ROOT/'assets/produtos') and
                target.suffix.lower() in ('.jpg','.jpeg','.png','.webp','.gif','.avif','.svg') and
                not target.is_file())
    def limpar_figura(m):
        sources = re.findall(r'<img\b[^>]*src="([^"]+)"', m.group(0), re.S)
        return '' if sources and all(ausente(src) for src in sources) else m.group(0)
    documento = re.sub(r'<figure\b[^>]*>.*?</figure>', limpar_figura, documento, flags=re.S)
    documento = re.sub(r'<img\b[^>]*src="([^"]+)"[^>]*>',
        lambda m: '' if ausente(m.group(1)) else m.group(0), documento, flags=re.S)
    documento = re.sub(r'<a\b[^>]*href="([^"]+)"[^>]*>.*?</a>',
        lambda m: '' if ausente(m.group(1)) else m.group(0), documento, flags=re.S)
    return documento

def write(path, text):
    if str(path).endswith('.html'):
        text = pagina_publica(corrigir_imagens_removidas(text, path))
    elif str(path) == 'assets/pesquisa-dados.js':
        entries = json.loads(text.split('=', 1)[1].strip().removesuffix(';'))
        for entry in entries:
            guide_id = entry['url'].removeprefix('guias/').removesuffix('.html')
            if entry['url'].startswith('guias/') and guide_id in GUIAS_POR_ID:
                entry['text'] = texto_guia(GUIAS_POR_ID[guide_id])
                continue
            product_id = entry['url'].removeprefix('produtos/').removesuffix('.html')
            if entry['url'].startswith('produtos/') and product_id in FAMILIAS_PRODUTOS:
                entry['text'] = ' '.join(textos_publicos(FAMILIAS_PRODUTOS[product_id]))
                continue
            page = ROOT/entry['url']
            if page.is_file():
                main = re.search(r'<main\b[^>]*>(.*?)</main>', page.read_text(encoding='utf-8'), re.S)
                if main:
                    entry['text'] = re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', ' ', main[1]))).strip()
            for key, value in entry.items():
                if isinstance(value, str): entry[key] = texto_publico(value)
        text = 'window.BRINDES_SEARCH = ' + json.dumps(entries, ensure_ascii=False).replace('<', '\\u003c') + ';\n'
    target=ROOT/path
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(text,encoding='utf-8')
def link(href,title): return f'<a href="{escape(href,quote=True)}">{escape(title)}</a>'
def prose(text):
    return re.sub(r'\[([a-z]+)\]',lambda m:f'<a class="source-ref" href="#fonte-{m[1]}" aria-label="Fonte: {escape(FONTES[m[1]][0])}">↗</a>',escape(text))
def header(prefix,active=''):
    nav=''
    for s in SECCOES:
        current=' aria-current="page"' if active==s['id'] else ''
        nav+=f'<a href="{prefix}{s["id"]}/index.html"{current}>{s["curto"]}</a>'
    return f'''<a class="skip" href="#conteudo">Saltar para o conteúdo</a><div class="top"></div><header class="header"><div class="wrap header-inner"><a href="{prefix}index.html" class="brand" aria-label="brindes.pt — início">brindes<span>.pt</span></a><nav id="nav" class="nav" aria-label="Navegação principal">{nav}<a href="{prefix}pesquisa.html" class="nav-search">Pesquisar</a></nav><button class="hamb" aria-label="Abrir menu" id="menu-toggle" aria-expanded="false" aria-controls="nav">☰</button></div></header>'''
def footer(prefix):
    return f'<footer class="footer"><div class="wrap foot-inner"><div class="footer-library"><p>brindes.pt — Biblioteca informativa independente. Informação para compreender, comparar e escolher.</p></div><nav class="footer-links" aria-label="Informação do site"><a href="{prefix}creditos-imagens.html">Créditos de imagens</a></nav></div></footer>'
def search_form(prefix):
    return f'<form class="search" action="{prefix}pesquisa.html" method="get" role="search"><label class="sr-only" for="q">Pesquisar na biblioteca</label><input id="q" name="q" type="search" maxlength="160" placeholder="Técnica, produto ou dúvida…"><button type="submit">Pesquisar</button></form>'
def shell(title,description,content,prefix='',active='',extra=''):
    return f'''<!doctype html><html lang="pt-PT"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{escape(description,quote=True)}"><meta name="robots" content="noindex, nofollow"><title>{escape(title)} — brindes.pt</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet"><link rel="stylesheet" href="{prefix}styles.css"></head><body>{header(prefix,active)}<main id="conteudo" class="wrap" tabindex="-1">{content}</main>{footer(prefix)}{extra}<script src="{prefix}script.js" defer></script></body></html>'''
def card(a,prefix=''):
    return f'<a class="topic content-card" href="{prefix}{url(a)}"><span class="eyebrow">{SECS[a["sec"]]["curto"]}</span><h3>{a["titulo"]}</h3><p>{a["resumo"]}</p><span class="arrow" aria-hidden="true">↗</span></a>'
def idea_media(a,caption=True):
    if not (ROOT/'assets/produtos/manifesto.json').is_file():
        return ''
    sizes={p['id']:p for p in json.loads((ROOT/'assets/produtos/manifesto.json').read_text(encoding='utf-8'))}
    images=''
    for id in a['imagens']:
        p=POR_ID[id];s=sizes[id]
        images+=f'<img src="../assets/produtos/{p["ficheiro"]}" alt="{escape(p["alt"])}" width="{s["width"]}" height="{s["height"]}" loading="lazy" decoding="async">'
    figcaption=''
    if caption:
        source=' · '.join(f'{POR_ID[id]["nome"]} {POR_ID[id]["ref"]}: PDF p. {POR_ID[id]["pdf"]}' for id in a['imagens'])
        note=' Sugestão de combinação de artigos individuais; não é um kit comercial documentado.' if len(a['imagens'])>1 else ''
        figcaption=f'<figcaption>Fotografias do catálogo. {source}.{note} <a href="../creditos-imagens.html#catalogo">Créditos das imagens</a></figcaption>'
    return f'<figure class="idea-media"><div class="idea-images idea-images-{len(a["imagens"])}">{images}</div>{figcaption}</figure>'

def editorial_text(text):
    """Parágrafos, listas e destaque dos textos recebidos; HTML é escapado."""
    def inline(value):
        return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escape(value))
    blocks = []
    for block in text.split('\n\n'):
        lines = block.splitlines()
        if all(line.startswith('- ') for line in lines):
            blocks.append('<ul>' + ''.join('<li>' + inline(line[2:]) + '</li>' for line in lines) + '</ul>')
        else:
            blocks.append('<p>' + inline(' '.join(lines)) + '</p>')
    return ''.join(blocks)


def novelty_visual(a):
    return f'<div class="novelty-visual"><span>{escape(a["fornecedor"])}</span><strong>{escape(a["referencia"])}</strong><span>Design e utilidade quotidiana</span></div>'


def novelty_article(a):
    body = ''.join(f'<section id="parte-{n}"><h2>{escape(title)}</h2>{editorial_text(text)}</section>' for n, (title, text) in enumerate(a['seccoes']))
    sources = ''.join('<li>' + link(source['url'], source['titulo']) + ' — Consulta registada no dossier: <time datetime="' + source['consulta'] + '">28 de setembro de 2026</time>.</li>' for source in a['fontes_editoriais'])
    body += '<section id="fontes"><h2>Fontes e âmbito</h2><ul class="sources">' + sources + '</ul><p>As características são atribuídas aos fornecedores. Os contextos de utilização são sugestões editoriais; não comprovam procura ou disponibilidade comercial.</p></section>'
    body += '<section id="confirmar"><h2>Antes de uma proposta comercial</h2><ul>' + ''.join('<li>' + escape(item) + '</li>' for item in a['pendentes']) + '</ul></section>'
    toc = ''.join(link('#parte-' + str(n), title) for n, (title, _) in enumerate(a['seccoes'])) + link('#fontes', 'Fontes e âmbito') + link('#confirmar', 'Antes de uma proposta comercial')
    intro = f'<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / <a href="index.html">Tendências e novidades</a></nav><div class="page-intro"><span class="eyebrow">{escape(a["categoria"])} · {escape(a["fornecedor"])}</span><h1>{escape(a["titulo"])}</h1><p>{escape(a["resumo"])}</p><div class="review">Data editorial: <time datetime="{a["data"]}">28 de setembro de 2026</time></div></div>'
    note = '<aside class="note"><p>' + escape(a['nota_editorial']) + '</p></aside>'
    content = intro + '<div class="reading-layout"><aside class="contents"><strong>Neste artigo</strong><nav aria-label="Índice do artigo">' + toc + '</nav></aside><article class="reading novelty-reading">' + novelty_visual(a) + note + body + '<a class="back-to-ideas" href="index.html">← Voltar a Tendências e novidades</a></article></div><section><h2>Guias para aprofundar</h2><div class="article-grid">' + ''.join(card(BY_ID[k], '../') for k in a['relacionados']) + '</div></section>'
    write(url(a), shell(a['titulo'], a['resumo'], content, '../', 'tendencias'))


def idea_listing(s):
    cards = ''.join(f'<article class="idea-card">{novelty_visual(a)}<div class="idea-card-copy"><span class="eyebrow">{escape(a["categoria"])}</span><h2>{escape(a["titulo"])}</h2><p>{escape(a["resumo"])}</p><a class="link idea-read-more" href="{a["id"]}.html" aria-label="Ler mais: {escape(a["titulo"], quote=True)}">Ler mais <span aria-hidden="true">→</span></a></div></article>' for a in NOVIDADES)
    for a in IDEIAS:
        cards+=f'<article class="idea-card">{idea_media(a,False)}<div class="idea-card-copy"><span class="eyebrow">{a["categoria"]}</span><h2>{a["titulo"]}</h2><p>{a["resumo"]}</p><a class="link idea-read-more" href="{a["id"]}.html" aria-label="Ler mais: {escape(a["titulo"],quote=True)}">Ler mais <span aria-hidden="true">→</span></a></div></article>'
    intro='<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / Tendências e novidades</nav><div class="page-intro"><span class="eyebrow">Inspiração para escolher</span><h1>Tendências e novidades</h1><p>Novidades identificadas pelos fornecedores, produtos em destaque e ideias para pensar a sua próxima oferta.</p></div>'
    content=intro+'<div class="ideas-grid">'+cards+'</div><aside class="note"><strong>Ideias para adaptar ao seu contexto</strong><p>Os cartões distinguem novidades confirmadas nas fontes, destaques editoriais e ideias de utilização. Uma novidade de fornecedor não comprova uma tendência de mercado nem disponibilidade na Nobrinde.</p></aside>'
    # Conserva os destinos de âncoras da versão anterior.
    content+='<section id="sustentabilidade"><h2>Reutilização com contexto</h2><p class="catalogue-intro">Ao escolher um artigo, pense no uso que terá. Uma composição ou um material, por si só, não demonstra uma vantagem ambiental.</p></section><section id="novidades"><h2>Continue a explorar</h2><div class="context-links"><a href="../produtos/index.html">Conhecer os produtos</a><a href="../guias/como-escolher-a-tecnica.html">Como escolher a técnica</a></div></section>'
    write('tendencias/index.html',shell('Tendências e novidades',s['resumo'],content,'../','tendencias'))

def idea_article(a):
    body=''.join(f'<section id="parte-{n}"><h2>{escape(t)}</h2><p>{escape(p)}</p></section>' for n,(t,p) in enumerate(a['seccoes']))
    sources=''.join(f'<li><a href="../creditos-imagens.html#catalogo-{id}">{POR_ID[id]["nome"]} {POR_ID[id]["ref"]}</a> — PDF p. {POR_ID[id]["pdf"]}; página impressa {POR_ID[id]["impressa"]}.</li>' for id in a.get('produtos',a['imagens']))
    content=f'<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / <a href="index.html">Artigos e ideias</a></nav><div class="page-intro"><span class="eyebrow">{a["categoria"]} · Artigo e ideias</span><h1>{a["titulo"]}</h1><p>{a["resumo"]}</p></div><article class="idea-reading">{idea_media(a)}{body}<section id="fontes"><h2>Fontes e âmbito</h2><p>Características e imagens do General Catalogue 2026, fornecido pela equipa. As sugestões de utilização e combinação são propostas editoriais. Os dados da edição do catálogo não garantem disponibilidade atual nem compatibilidade de personalização.</p><ul class="sources">{sources}</ul></section><a class="back-to-ideas" href="index.html">← Voltar aos artigos e ideias</a></article><section><h2>Guias para aprofundar</h2><div class="article-grid">'+''.join(card(BY_ID[k],'../') for k in a['relacionados'])+'</div></section>'
    write(url(a),shell(a['titulo'],a['resumo'],content,'../','tendencias'))

def public_listing(s):
    cards=''
    for a in PUBLICOS:
        photo=idea_media({'imagens':[a['selecoes'][0][0]]},False)
        cards+=f'<article class="audience-card" id="{a["ancora"]}">{photo}<div class="idea-card-copy"><span class="eyebrow">Guia de escolha</span><h2>{a["titulo"]}</h2><p>{a["resumo"]}</p><a class="link idea-read-more" href="{a["id"]}.html">Explorar: {a["titulo"]} <span aria-hidden="true">→</span></a></div></article>'
    body='<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / Para quem</nav><div class="page-intro"><span class="eyebrow">Escolher pelo contexto</span><h1>Para quem</h1><p>Encontre ideias para os seus destinatários. Seis guias com produtos reais do catálogo e perguntas úteis para preparar a escolha.</p></div><div class="audience-grid">'+cards+'</div><aside class="note"><strong>Da referência à escolha</strong><p>As seleções são propostas editoriais. As fotografias e características provêm do catálogo; a utilização pretendida e a personalização precisam de avaliação para o artigo concreto.</p></aside>'
    write('publicos/index.html',shell('Para quem',s['resumo'],body,'../','publicos'))

def public_article(a):
    manifest = ROOT/'assets/produtos/manifesto.json'
    sizes={p['id']:p for p in json.loads(manifest.read_text(encoding='utf-8'))} if manifest.is_file() else {}
    choices=''
    for id,why in a['selecoes']:
        if id not in sizes: continue
        p=POR_ID[id];size=sizes[id];category=PAGINAS_PRODUTOS[p['categoria']]
        choices+=f'''<article class="product-example audience-choice" id="produto-{id}"><figure><div class="product-photo-frame"><img src="../assets/produtos/{p['ficheiro']}" alt="{escape(p['alt'])}" width="{size['width']}" height="{size['height']}" loading="lazy" decoding="async"></div><figcaption>Fotografia do catálogo · Ref. {p['ref']}</figcaption></figure><div class="product-example-copy"><h3>{p['nome']} <span>Referência {p['ref']}</span></h3><p class="choice-reason">{escape(why)}</p><details><summary>Características indicadas no catálogo</summary><ul>{''.join('<li>'+escape(f)+'</li>' for f in p['factos'])}</ul></details><p class="catalogue-source"><a href="../creditos-imagens.html#catalogo-{id}">Fonte: PDF p. {p['pdf']} · página impressa {p['impressa']}</a></p><a class="choice-category" href="../produtos/{category}.html">Consultar o guia: {BY_ID[category]['titulo']} →</a></div></article>'''
    methods=''.join(link('../'+url(BY_ID[id]),BY_ID[id]['titulo']) for id in a['metodos'])
    sources=''.join(f'<li>{POR_ID[id]["nome"]} {POR_ID[id]["ref"]}: PDF p. {POR_ID[id]["pdf"]}; página impressa {POR_ID[id]["impressa"]}.</li>' for id,_ in a['selecoes'])
    body=f'''<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / <a href="index.html">Para quem</a> / {a['titulo']}</nav><div class="page-intro"><span class="eyebrow">Guia de escolha · Para quem</span><h1>{a['titulo']}</h1><p>{a['resumo']}</p></div><section class="audience-intro"><h2>Necessidades e critérios</h2><p>{escape(a['seccoes'][0][1])}</p></section><section class="audience-selection"><h2>Produtos a considerar</h2><p class="catalogue-intro">Sugestões de utilização para este público, apoiadas em características do catálogo. As fotografias não representam trabalhos da Nobrinde.</p><div class="audience-products">{choices}</div></section><section class="note"><h2>Antes de escolher</h2><p>{escape(a['seccoes'][1][1])}</p></section><section><h2>Compreender a personalização</h2><p class="catalogue-intro">Estes guias explicam métodos a discutir com a produção. A ligação a uma técnica não confirma a sua compatibilidade com todos os produtos desta seleção. Confirme a referência, a superfície, a arte e as condições de aplicação.</p><div class="context-links">{methods}{link('../guias/como-escolher-a-tecnica.html','Como escolher a técnica')}</div></section><section id="fontes"><h2>Fontes deste guia</h2><p class="catalogue-intro">General Catalogue 2026, fornecido pela equipa. Os dados referem-se à edição consultada; não constituem confirmação de disponibilidade. As justificações de utilização são sugestões editoriais.</p><ul class="sources">{sources}</ul></section><a class="back-to-ideas" href="index.html">← Voltar a Para quem</a>'''
    write(url(a),shell(a['titulo'],a['resumo'],body,'../','publicos'))

def guide_listing(s):
    write('guias/index.html', entrada_guias(shell, link))

def guide_article(a):
    write(url(a), artigo_guia(GUIAS_POR_ID[a['id']], BY_ID, shell, link))

def material_media(a, caption=True):
    if not caption and a.get('imagem_cartao'):
        file, width, height, description = a['imagem_cartao']
        return f'<figure class="idea-media material-media"><div class="idea-images"><img src="../{quote(file)}" alt="{escape(description, quote=True)}" width="{width}" height="{height}" loading="lazy" decoding="async"></div></figure>'
    if not a.get('imagem'):
        return ''
    if not (ROOT/'assets/produtos/manifesto.json').is_file():
        return ''
    product_id, description = a['imagem']
    p = POR_ID[product_id]
    size = next(p for p in json.loads((ROOT/'assets/produtos/manifesto.json').read_text(encoding='utf-8')) if p['id'] == product_id)
    legend = f'<figcaption>{escape(description)}</figcaption>' if caption else ''
    return f'<figure class="idea-media material-media"><div class="idea-images"><img src="../assets/produtos/{p["ficheiro"]}" alt="{escape(description, quote=True)}" width="{size["width"]}" height="{size["height"]}" loading="lazy" decoding="async"></div>{legend}</figure>'

def material_listing(s):
    cards = ''
    for a in MATERIAIS:
        cards += f'<article class="idea-card material-card" id="{a["ancora"]}">{material_media(a, False)}<div class="idea-card-copy"><span class="eyebrow">Família de materiais</span><h2>{escape(a["titulo"])}</h2><p>{escape(a["resumo"])}</p><a class="link idea-read-more" href="{a["id"]}.html" aria-label="Explorar materiais: {escape(a["titulo"], quote=True)}">Explorar materiais <span aria-hidden="true">→</span></a></div></article>'
    intro = '<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / Materiais</nav><div class="page-intro"><span class="eyebrow">Escolher pelo uso</span><h1>Materiais para brindes</h1><p>Conheça sete famílias de materiais e compare o que importa para o seu brinde: utilização, aspeto, peso, resistência e manutenção. O acabamento e a construção do artigo também contam.</p></div>'
    criteria = '<section class="material-criteria"><h2>Como comparar duas opções</h2><div class="guide-grid"><div class="topic guide-card"><h3>Comece pelo dia a dia</h3><p>Vai transportar o artigo, usá-lo numa secretária ou lavá-lo frequentemente? Compare a capacidade, o peso completo, a pega e as instruções de manutenção.</p></div><div class="topic guide-card"><h3>Observe uma amostra</h3><p>Compare textura, brilho, espessura e construção. Defina a posição do logótipo e peça uma prova na referência e no acabamento escolhidos.</p></div></div><div class="context-links"><a href="metais.html#parte-4">Alumínio ou aço inoxidável?</a><a href="materiais-texteis.html#parte-4">Algodão ou poliéster?</a><a href="../guias/como-escolher-o-material.html">Guia de escolha do material</a></div></section>'
    note = '<aside class="note"><h2>O material é um ponto de partida</h2><p>Não há uma família universalmente superior. As propriedades gerais não comprovam o desempenho de um artigo, a compatibilidade de personalização ou uma vantagem ambiental. Confirme os dados da referência escolhida.</p></aside>'
    write('materiais/index.html', shell('Materiais para brindes', s['resumo'], intro + '<div class="ideas-grid materials-grid">' + cards + '</div>' + criteria + note, '../', 'materiais'))

def material_article(a):
    toc = ''.join(link('#parte-' + str(n), title) for n, (title, _) in enumerate(a['seccoes']))
    body = material_media(a) + ''.join(f'<section id="parte-{n}"><h2>{escape(title)}</h2><p>{prose(p)}</p></section>' for n, (title, p) in enumerate(a['seccoes']))
    sources = ''.join(f'<li id="fonte-{key}">{link(FONTES[key][1], FONTES[key][0])}</li>' for key in a['fontes'])
    methods = [BY_ID[id] for id in a['relacionados'] if BY_ID[id]['sec'] in ('tecnicas', 'industria')]
    sources += ''.join('<li>' + link('../' + url(method), method['titulo'] + ' — processo e fontes técnicas') + '</li>' for method in methods)
    body += '<section id="fontes"><h2>Fontes e âmbito</h2><p>As fontes sustentam propriedades gerais ou exemplos específicos dos respetivos autores. Não certificam os artigos apresentados nem as capacidades da Nobrinde. As propostas de comparação e as perguntas de escolha são orientação editorial; confirme composição, acabamento, cuidados e personalização para a referência concreta.</p><ul class="sources">' + sources + '</ul></section><a class="back-to-ideas" href="index.html">← Voltar aos materiais</a>'
    related = ''.join(card(BY_ID[id], '../') for id in a['relacionados'])
    content = f'<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / <a href="index.html">Materiais</a> / <span>{escape(a["titulo"])}</span></nav><div class="page-intro"><span class="eyebrow">Materiais · Guia de escolha</span><h1>{escape(a["titulo"])}</h1><p>{escape(a["resumo"])}</p><div class="review">Revisão documental: <time datetime="2026-09-28">28 de setembro de 2026</time> · Guia permanente</div></div><div class="reading-layout"><aside class="contents"><strong>Neste guia</strong><nav aria-label="Índice do artigo">{toc}{link("#fontes", "Fontes e âmbito")}</nav></aside><article class="reading">{body}</article></div><section><h2>Produtos e técnicas para aprofundar</h2><div class="article-grid">{related}</div></section>'
    write(url(a), shell(a['titulo'], a['resumo'], content, '../', 'materiais'))

def montagem_media(a, caption=True):
    file, width, height, alt, description = IMAGENS_MONTAGEM[a['id']]
    legend = '<figcaption>'+escape(description)+' Não representa produção da Nobrinde. <a href="../creditos-imagens.html#montagem-fornecidas">Origem das imagens</a></figcaption>' if caption else ''
    return f'<figure class="pad-reference montagem-media"><img src="../{quote(BASE_IMAGENS + file)}" width="{width}" height="{height}" alt="{escape(alt, quote=True)}" loading="lazy" decoding="async">{legend}</figure>'

def montagem_hub(a):
    intro=f'<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / <a href="index.html">Técnicas</a> / {escape(a["titulo"])}</nav><div class="page-intro"><span class="eyebrow">Montagem e acabamento</span><h1>{escape(a["titulo"])}</h1><p>{escape(a["resumo"])}</p></div>'
    def section(n):
        title, text = a['seccoes'][n]
        return '<section><h2>'+escape(title)+'</h2>'+''.join('<p>'+prose(p)+'</p>' for p in text.split('\n\n'))+'</section>'
    cards=''
    for child in MONTAGEM[1:]:
        cards+='<article class="idea-card">'+montagem_media(child, False)+'<div class="idea-card-copy"><h2>'+escape(child['titulo'])+'</h2><p>'+escape(child['resumo'])+'</p><a class="link idea-read-more" href="'+child['id']+'.html" aria-label="Explorar técnica: '+escape(child['titulo'])+'">Explorar técnica <span aria-hidden="true">→</span></a></div></article>'
    sources=''.join(f'<li id="fonte-{k}">{link(FONTES[k][1],FONTES[k][0])}</li>' for k in a['fontes'])
    body=intro+'<div class="montagem-intro">'+section(0)+'</div><div class="ideas-grid montagem-grid">'+cards+'</div><p class="montagem-credits">Imagens ilustrativas fornecidas para o projeto; não representam produção da Nobrinde. <a href="../creditos-imagens.html#montagem-fornecidas">Créditos das imagens</a></p><div class="montagem-intro">'+section(1)+'</div><section id="fontes"><h2>Fontes e âmbito</h2><p>Princípios gerais e configurações dos autores, sem confirmação de serviços ou equipamentos da Nobrinde.</p><ul class="sources">'+sources+'</ul></section><section><h2>Continue a explorar</h2><div class="article-grid">'+''.join(card(BY_ID[id],'../') for id in a['relacionados'])+'</div></section>'
    write(url(a),shell(a['titulo'],a['resumo'],body,'../','tecnicas'))

def page_article(a):
    if a['sec']=='produtos':
        write(url(a), render_guia(FAMILIAS_PRODUTOS[a['id']], BY_ID, shell, link, card))
        return
    if a['id']==HUB_ID:
        montagem_hub(a)
        return
    if a['tipo']=='novidade':
        novelty_article(a)
        return
    if a['sec']=='materiais':
        material_article(a)
        return
    if a['sec']=='guias':
        guide_article(a)
        return
    if a['tipo']=='area-industria':
        return  # Geradas em conjunto pela entrada da secção.
    if a['tipo']=='publico':
        public_article(a)
        return
    if a['tipo']=='ideia':
        idea_article(a)
        return
    ids=a.get('ids_seccoes', [f'parte-{n}' for n in range(len(a['seccoes']))])
    toc=''.join(link('#'+i,s[0]) for i,s in zip(ids,a['seccoes']))
    body=''.join(f'<section id="{i}"><h2>{escape(t)}</h2><p>{prose(p)}</p></section>' for i,(t,p) in zip(ids,a['seccoes']))
    if a.get('montagem'):
        body='<a class="back-to-ideas" href="'+HUB_ID+'.html">← Costura, Argolagem e Encadernação</a>'
        for n,(i,(title,text)) in enumerate(zip(ids,a['seccoes'])):
            content=''.join('<p>'+prose(p)+'</p>' for p in text.split('\n\n'))
            if n==0:
                content+=montagem_media(a)
            body+='<section id="'+i+'"><h2>'+escape(title)+'</h2>'+content+'</section>'
    if a.get('transfer'):
        body=''
        if a['id']!='transfers':
            body+='<a class="back-to-ideas" href="transfers.html">← Explorar todos os transfers</a>'
        for i,(title,text) in zip(ids,a['seccoes']):
            content=''.join('<p>'+prose(paragraph)+'</p>' for paragraph in text.split('\n\n'))
            if i in IMAGENS_TRANSFERS.get(a['id'], {}):
                file,width,height,alt,caption=IMAGENS_TRANSFERS[a['id']][i]
                content+=f'<figure class="pad-reference"><img src="../assets/tecnicas/Transfers/{quote(file)}" width="{width}" height="{height}" alt="{escape(alt)}" loading="lazy" decoding="async"><figcaption>{escape(caption)} Não representa produção da Nobrinde. <a href="../creditos-imagens.html#transfers-fornecidas">Origem e autorização de utilização</a></figcaption></figure>'
            if i=='modalidades':
                content+='<div class="transfer-cards">'+''.join(card(BY_ID[k],'../') for k in TRANSFER_IDS)+'</div>'
            if i=='confirmar':
                content+='<ul class="guide-checklist">'+''.join('<li><strong>'+escape(label)+':</strong> '+prose(detail)+'</li>' for label,detail in a['checklist'])+'</ul>'
            if i=='comparar':
                content+='<div class="context-links">'+''.join(link(k+'.html',BY_ID[k]['titulo']) for k in TRANSFER_IDS if k!=a['id'])+'</div>'
            body+=f'<section id="{i}"><h2>{escape(title)}</h2>{content}</section>'
    if a['id']=='crachas-automaticos':
        body=''
        for i,(title,text) in zip(ids,a['seccoes']):
            content=''.join('<p>'+prose(p)+'</p>' for p in text.split('\n\n'))
            if i=='como-funciona':
                content+='<ol class="pad-steps">'+''.join('<li><strong>'+escape(t)+'</strong><p>'+prose(p)+'</p></li>' for t,p in PASSOS_CRACHAS)+'</ol>'
            if i in ('componentes','perguntas'):
                items=COMPONENTES_CRACHAS if i=='componentes' else FAQ_CRACHAS
                content+='<div class="troubleshooting">'+''.join('<div><h3>'+escape(t)+'</h3><p>'+prose(p)+'</p></div>' for t,p in items)+'</div>'
            if i=='equipamento':
                file,width,height,alt,caption=IMAGEM_CRACHAS
                content+=f'<figure class="pad-reference"><img src="../assets/tecnicas/Crachas/{quote(file)}" width="{width}" height="{height}" alt="{escape(alt)}" loading="lazy" decoding="async"><figcaption>{escape(caption)} <a href="../creditos-imagens.html#crachas-fornecida">Origem da imagem</a></figcaption></figure>'
            body+=f'<section id="{i}"><h2>{escape(title)}</h2>{content}</section>'
    if a['id']=='tecnica-troquelagem':
        body=''
        for i,(title,text) in zip(ids,a['seccoes']):
            content=''.join('<p>'+prose(p)+'</p>' for p in text.split('\n\n'))
            if i=='como-funciona':
                content+='<ol class="pad-steps">'+''.join('<li><strong>'+escape(t)+'</strong><p>'+prose(p)+'</p></li>' for t,p in PASSOS_TROQUELAGEM)+'</ol>'
            if i in ('operacoes','perguntas'):
                items=OPERACOES_TROQUELAGEM if i=='operacoes' else FAQ_TROQUELAGEM
                content+='<div class="troubleshooting">'+''.join('<div><h3>'+escape(t)+'</h3><p>'+prose(p)+'</p></div>' for t,p in items)+'</div>'
            if i in IMAGENS_TROQUELAGEM:
                file,width,height,alt,caption=IMAGENS_TROQUELAGEM[i]
                content+=f'<figure class="pad-reference"><img src="../assets/tecnicas/Troquelagem/{quote(file)}" width="{width}" height="{height}" alt="{escape(alt)}" loading="lazy" decoding="async"><figcaption>{escape(caption)} <a href="../creditos-imagens.html#troquelagem-fornecidas">Origem das imagens</a></figcaption></figure>'
            body+=f'<section id="{i}"><h2>{escape(title)}</h2>{content}</section>'
    if a['id']=='termogravura':
        body=''
        for i,(title,text) in zip(ids,a['seccoes']):
            content=''.join('<p>'+prose(paragraph)+'</p>' for paragraph in text.split('\n\n'))
            if i=='confirmar':
                content+='<ul class="guide-checklist">'+''.join('<li><strong>'+escape(label)+':</strong> '+prose(detail)+'</li>' for label,detail in a['checklist'])+'</ul>'
            if i=='comparar':
                content+='<div class="context-links">'+''.join(link(id+'.html',BY_ID[id]['titulo']) for id in ['gravacao-a-laser','impressao-uv','serigrafia'])+'</div>'
            body+=f'<section id="{i}"><h2>{escape(title)}</h2>{content}</section>'
    if a['id']=='bordado':
        body=''
        for i,(title,text) in zip(ids,a['seccoes']):
            content=''.join('<p>'+prose(paragraph)+'</p>' for paragraph in text.split('\n\n'))
            if i in IMAGENS_BORDADO:
                file,width,height,alt,caption=IMAGENS_BORDADO[i]
                content+=f'<figure class="pad-reference"><img src="../assets/tecnicas/Bordado/{file}" width="{width}" height="{height}" alt="{escape(alt)}" loading="lazy" decoding="async"><figcaption>{escape(caption)} Não representa produção da Nobrinde. <a href="../creditos-imagens.html#bordado-fornecidas">Origem e autorização de utilização</a></figcaption></figure>'
            if i=='parte-5':
                content+='<ul class="guide-checklist">'+''.join('<li><strong>'+escape(label)+':</strong> '+prose(detail)+'</li>' for label,detail in a['confirmar_bordado'])+'</ul>'
            if i=='parte-7':
                content+='<div class="context-links">'+link('serigrafia.html','Comparar com serigrafia')+link('tecnica-sublimacao.html','Condições da sublimação')+'</div>'
            body+=f'<section id="{i}"><h2>{escape(title)}</h2>{content}</section>'
    if a['id']=='tecnica-sublimacao':
        body = ''
        for i, (title, text) in zip(ids, a['seccoes']):
            media = ''
            for file, height, alt, caption in IMAGENS_SUBLIMACAO.get(title, []):
                src = '../assets/tecnicas/Sublimacao/' + quote(file)
                media += f'<figure class="pad-reference sublimacao-reference"><img src="{src}" width="474" height="{height}" alt="{escape(alt)}" loading="lazy" decoding="async"><figcaption>{escape(caption)} Não representa instalações da Nobrinde. <a href="../creditos-imagens.html#sublimacao-fornecidas">Origem e autorização de utilização</a></figcaption></figure>'
            body += f'<section id="{i}"><h2>{escape(title)}</h2><p>{prose(text)}</p>{media}</section>'
    if a['id']=='tampografia':
        body='<section id="o-que-e"><h2>O que é a tampografia?</h2><p>'+prose(a['introducao'])+'</p></section>'
        toc=link('#o-que-e','O que é a tampografia?')+toc
        for i,(t,p) in zip(ids,a['seccoes']):
            extra=''
            if t=='Como funciona':
                extra='<ol class="pad-steps">'+''.join('<li><strong>'+escape(title)+'</strong><p>'+escape(text)+'</p></li>' for title,text in PASSOS_TAMPOGRAFIA)+'</ol><p>'+prose('Descrição do ciclo de copo fechado: [inkcups]. Secagem e cura dependem da tinta e dos auxiliares utilizados: [marabu].')+'</p>'
            if t in IMAGENS_TAMPOGRAFIA:
                file,height,alt,caption=IMAGENS_TAMPOGRAFIA[t]
                extra+=f'<figure class="pad-reference"><img src="../assets/tecnicas/Tampografia/{file}" width="474" height="{height}" alt="{escape(alt)}" loading="lazy" decoding="async"><figcaption>{escape(caption)} <strong>Imagem provisória: origem e autorização de publicação por confirmar.</strong> <a href="../creditos-imagens.html#tampografia-provisoria">Estado dos créditos</a></figcaption></figure>'
            if t=='Equipamentos':
                extra+='<p><a href="../creditos-imagens.html#tampografia">Consultar também a fotografia de equipamento anteriormente documentada e os seus créditos.</a></p>'
            body+=f'<section id="{i}"><h2>{escape(t)}</h2><p>{prose(p)}</p>{extra}</section>'
    if a['id']=='serigrafia':
        body='<section id="o-que-e"><h2>O que é a serigrafia?</h2><p>'+prose(a['introducao'])+'</p></section>'
        toc=link('#o-que-e','O que é a serigrafia?')+toc
        for i,(t,p) in zip(ids,a['seccoes']):
            extra=''
            if t=='Como funciona':
                extra='<figure class="screen-process"><ol>'+''.join('<li><strong>'+escape(title)+'</strong><p>'+escape(text)+'</p></li>' for title,text in PASSOS_SERIGRAFIA)+'</ol><figcaption>Da arte ao artigo impresso: leia as sete etapas de cima para baixo. A sequência é simplificada e deve ser adaptada à tinta e ao produto.</figcaption></figure>'
            if t=='Equipamento':
                extra='<figure class="pad-reference"><img src="../assets/tecnicas/Serigrafia/maquina-carrossel-serigrafia-verde.jpg" width="474" height="474" alt="Carrossel de serigrafia com várias telas verdes levantadas e suportes planos para peças têxteis." loading="lazy" decoding="async"><figcaption>Exemplo ilustrativo de máquina de serigrafia para têxteis<strong>Imagem provisória de terceiros: origem e autorização de publicação por confirmar.</strong><a href="../creditos-imagens.html#serigrafia-provisoria">Estado dos créditos</a></figcaption></figure>'
            body+=f'<section id="{i}"><h2>{escape(t)}</h2><p>{prose(p)}</p>{extra}</section>'
    if a['id']=='impressao-uv':
        body='<section id="o-que-e"><h2>O que é a impressão digital UV?</h2><p>'+prose(a['introducao'])+'</p></section>'
        toc=link('#o-que-e','O que é a impressão digital UV?')+toc
        for i,(t,p) in zip(ids,a['seccoes']):
            extra=''
            if t=='Como funciona':
                extra='<figure class="screen-process"><ol>'+''.join('<li><strong>'+escape(title)+'</strong><p>'+escape(text)+'</p></li>' for title,text in PASSOS_UV)+'</ol><figcaption>Cinco etapas de leitura; impressão e cura são coordenadas no equipamento.</figcaption></figure>'
            if t in IMAGENS_UV:
                file,height,alt,caption=IMAGENS_UV[t]
                extra+=f'<figure class="pad-reference"><img src="../assets/tecnicas/ImpressaoUV/{file}" width="474" height="{height}" alt="{escape(alt)}" loading="lazy" decoding="async"><figcaption>{escape(caption)} Não representa instalações da Nobrinde. <strong>Imagem provisória: origem e autorização de publicação por confirmar.</strong> <a href="../creditos-imagens.html#uv-provisoria">Estado dos créditos</a></figcaption></figure>'
            if t=='Equipamento':
                extra+='<p>Os equipamentos de grande formato representam outra escala de trabalho, distinta da personalização de pequenos artigos numa mesa. Consulte o <a href="../industria/impressoras-uv.html">guia de impressoras UV</a> para comparar configurações.</p>'
            body+=f'<section id="{i}"><h2>{escape(t)}</h2><p>{prose(p)}</p>{extra}</section>'
    if a.get('passos'):
        caption='Marcos selecionados; fontes e contexto no texto.' if a['tipo']=='historia' else 'Esquema simplificado de leitura; não é uma instrução de operação.'
        body='<figure class="process-diagram"><ol>'+''.join('<li>'+escape(p)+'</li>' for p in a['passos'])+'</ol><figcaption>'+caption+'</figcaption></figure>'+body
    if a.get('foto_tecnica'):
        body=tecnica(a['foto_tecnica'])+body
    if a['sec']=='industria':
        body+='<a class="back-to-ideas" href="index.html">← Voltar ao percurso e aos guias da indústria</a>'
    if a['id'] in FOTOS_TECNICAS and a['id']!='tampografia':
        body=tecnica(a['id'])+body
    if a['id'] in ARTIGO_PRODUTOS:
        toc+=link('#exemplos-catalogo','Exemplos do catálogo')
        body+=exemplos(ARTIGO_PRODUTOS[a['id']])
    if a['problemas']:
        toc+=link('#problemas','Problemas e verificações')
        body+='<section id="problemas"><h2>Problemas frequentes e verificações</h2><p>Um sinal pode ter várias causas. Estas verificações orientam a conversa com a produção.</p><div class="troubleshooting">'+''.join(f'<div><h3>{escape(t)}</h3><p>{prose(p)}</p></div>' for t,p in a['problemas'])+'</div></section>'
    if a['tipo']=='tecnica':
        body+='<aside class="note"><strong>Antes de produzir</strong><p>A compatibilidade deve ser confirmada para o artigo, a arte e a utilização pretendida. Estes guias não constituem uma declaração de equipamentos ou capacidades da Nobrinde.</p></aside>'
    if a['fontes']:
        scope='Os registos históricos sustentam apenas os marcos identificados. As interpretações são editoriais; o catálogo não é usado como prova histórica.' if a['tipo']=='historia' else 'As referências de fabricantes e fornecedores descrevem os seus próprios processos ou equipamentos. Não são especificações da operação da Nobrinde.'
        body+='<section id="fontes"><h2>Fontes e âmbito</h2><p>'+scope+'</p><ul class="sources">'+''.join(f'<li id="fonte-{k}">{link(FONTES[k][1],FONTES[k][0])}</li>' for k in a['fontes'])+'</ul></section>'
    else:
        body+='<section id="fontes"><h2>Base deste guia</h2><p>Perguntas editoriais para preparar o trabalho, acompanhadas por exemplos do General Catalogue 2026. Cada exemplo identifica a página do PDF e a página impressa que suportam a fotografia e as características. As explicações técnicas e respetivas fontes encontram-se nos guias relacionados.</p></section>'
    def context_title(p):
        sec=SECS[p.split('/')[0]]
        return next((g[1] for g in sec['grupos'] if '#' in p and g[0]==p.split('#')[1]),sec['titulo'])
    context=''.join(link('../'+p,context_title(p)) for p in a['ancoras'])
    related=''.join(card(BY_ID[k],'../') for k in a['relacionados'])
    content=f'''<nav class="crumb" aria-label="Percurso">{link('../index.html','Início')} / {link('index.html',SECS[a['sec']]['titulo'])} / <span>{a['titulo']}</span></nav><div class="page-intro"><span class="eyebrow">{SECS[a['sec']]['titulo']}</span><h1>{a['titulo']}</h1><p>{a['resumo']}</p><div class="review">Revisão documental: <time datetime="{a.get('data_revisao', DATA_REVISAO)}">{a.get('data_revisao_texto', '24 de setembro de 2026')}</time> · Guia permanente</div></div><div class="reading-layout"><aside class="contents"><strong>Neste guia</strong><nav aria-label="Índice do artigo">{toc}{link('#fontes','Fontes e âmbito')}</nav></aside><article class="reading">{body}</article></div><section><div class="section-head"><div><span class="eyebrow">Continue a explorar</span><h2>Assuntos relacionados</h2></div></div><div class="context-links">{context}</div><div class="article-grid">{related}</div></section>'''
    write(url(a),shell(a['titulo'],a['resumo'],content,'../',a['sec']))
def industry_listing(s):
    intro='<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / Indústria</nav><div class="page-intro"><span class="eyebrow">Da escolha à receção</span><h1>O percurso de uma encomenda</h1><p>Conheça as decisões que transformam um pedido num artigo personalizado, pronto a chegar ao destinatário.</p></div><aside class="note"><strong>Um percurso para compreender e adaptar</strong><p>A sequência pode variar com o produto e o tipo de encomenda, incluir regressos à aprovação e combinar etapas. É um guia editorial, não um procedimento interno ou uma promessa de serviços da Nobrinde.</p></aside>'
    stages=''
    for n,(title,what,confirm) in enumerate(ETAPAS,1):
        more=''
        if n==1: more='<a href="../produtos/index.html">Explorar os produtos →</a>'
        if n==2: more='<a href="../guias/como-escolher-a-tecnica.html">Comparar técnicas →</a>'
        if n==6: more=tecnica('tampografia')+'<a href="#maquinas">Conhecer os processos →</a>'
        if n==8: more=idea_media({'imagens':['gratox-22075']})+'<a href="montagem-e-acabamentos.html">Conhecer as operações de montagem →</a>'
        stages+=f'<li id="etapa-{n}"><span class="stage-number" aria-hidden="true">{n:02}</span><div><h3>{title}</h3><p>{what}</p><p class="stage-confirm"><strong>A confirmar pelo cliente</strong> {confirm}</p>{more}</div></li>'
    timeline='<section id="fluxo"><h2>Do pedido à entrega, em 11 etapas</h2><ol class="order-timeline">'+stages+'</ol></section>'
    machines='<section id="maquinas"><div class="section-head"><div><span class="eyebrow">Compreender a produção</span><h2>Processos e tipos de máquinas</h2><p>Função, aplicações e limites. Estes guias não identificam o parque de máquinas da Nobrinde.</p></div></div><div class="article-grid">'+''.join(card(a,'../') for a in INDUSTRIA if a['id'] not in ['montagem-e-acabamentos','historia-dos-brindes'])+'</div></section>'
    back='<a class="back-to-ideas" href="index.html">← Voltar a Indústria</a>'
    journey=intro.replace('<h1>O percurso de uma encomenda</h1>','<h1>Da ideia à entrega</h1>').replace('href="#maquinas"','href="maquinas-e-processos.html"')
    journey=journey.replace(' / Indústria</nav>',' / <a href="index.html">Indústria</a> / Da ideia à entrega</nav>')
    journey+=timeline.replace('href="#maquinas"','href="maquinas-e-processos.html"')
    journey+='<aside class="note"><h2>Base e limites deste percurso</h2><p>Organização editorial das perguntas de uma encomenda. Os guias de processos identificam as fontes técnicas. Equipamentos, amostras, critérios de qualidade, montagem, embalagem e condições de entrega precisam de confirmação pela produção.</p></aside>'+back
    write('industria/da-ideia-a-entrega.html',shell('Da ideia à entrega',BY_ID['da-ideia-a-entrega']['resumo'],journey,'../','industria'))
    machine_intro='<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / <a href="index.html">Indústria</a> / Máquinas e processos</nav><div class="page-intro"><span class="eyebrow">Compreender a produção</span><h1>Máquinas e processos</h1><p>Explore como os artigos podem ser produzidos e personalizados, as aplicações e os limites de cada processo.</p></div>'
    write('industria/maquinas-e-processos.html',shell('Máquinas e processos',BY_ID['maquinas-e-processos']['resumo'],machine_intro+machines+back,'../','industria'))
    areas=[
        ('historia','historia-dos-brindes','História dos Brindes','Evolução dos objetos promocionais, com marcos documentados e um exemplo português.'),
        ('fluxo','da-ideia-a-entrega','Da ideia à entrega','O percurso de uma encomenda, desde a escolha do artigo até à receção.'),
        ('maquinas','maquinas-e-processos','Máquinas e processos','Como trabalham os equipamentos, para que servem e quais são os seus limites.'),
        ('montagem','montagem-e-acabamentos','Montagem e acabamentos','Componentes, acessórios, revisão, embalagem e preparação para expedição.')]
    cards=''
    for anchor,id,title,description in areas:
        if anchor=='historia':
            visual='<div class="industry-card-visual history-milestones"><span>1881 · Portugal</span><span>c. 1896 · Emblemas</span><span>1903 · Setor profissional</span></div>'
        elif anchor=='fluxo':
            visual='<div class="industry-card-visual journey-milestones"><span>Ideia</span><span>Personalização</span><span>Entrega</span></div>'
        elif anchor=='maquinas':
            visual=tecnica('tampografia')
        else:
            visual=idea_media({'imagens':['gratox-22075']})
        cards+=f'<article class="industry-area" id="{anchor}">{visual}<div class="idea-card-copy"><h2><a href="{id}.html">{title}</a></h2><p>{description}</p><a class="link idea-read-more" href="{id}.html">Explorar: {title} →</a></div></article>'
    intro='<nav class="crumb" aria-label="Percurso"><a href="../index.html">Início</a> / Indústria</nav><div class="page-intro"><span class="eyebrow">História, produção e entrega</span><h1>Indústria</h1><p>Quatro caminhos para compreender os brindes: a sua história, o percurso de uma encomenda, os processos e as operações finais.</p></div>'
    write('industria/index.html',shell('Indústria',s['resumo'],intro+'<div class="industry-areas">'+cards+'</div>','../','industria'))

def page_section(s):
    if s['id']=='produtos':
        write('produtos/index.html', render_entrada(shell, link))
        return
    if s['id']=='materiais':
        material_listing(s)
        return
    if s['id']=='guias':
        guide_listing(s)
        return
    if s['id']=='industria':
        industry_listing(s)
        return
    if s['id']=='publicos':
        public_listing(s)
        return
    if s['id']=='tendencias':
        idea_listing(s)
        return
    nested_ids = set(TRANSFER_IDS) | {a['id'] for a in MONTAGEM[1:]}
    available=[a for a in ARTIGOS if a['sec']==s['id'] and a['id'] not in nested_ids]
    cards='<section class="available"><h2>Guias disponíveis</h2><div class="article-grid">'+''.join(card(a,'../') for a in available)+'</div></section>' if available else ''
    groups=''
    published={a['titulo']:a for a in available}
    for gid,title,description,topics in s['grupos']:
        pills=''.join(link('../'+url(published[t]),t) if t in published else f'<span>{escape(t)}</span>' for t in topics.split('|'))
        more='<div class="context-links">'+''.join(link('../'+url(BY_ID[k]),BY_ID[k]['titulo']) for k in GROUP_LINKS[(s['id'],gid)])+'</div>' if (s['id'],gid) in GROUP_LINKS else ''
        if s['id']=='industria' and gid=='maquinas':
            more='<div class="context-links">'+''.join(link('../'+url(BY_ID[k])+'#parte-1','Equipamentos de '+BY_ID[k]['titulo'].lower()) for k in ['tampografia','serigrafia','gravacao-a-laser','impressao-uv','bordado'])+'</div>'
        if (s['id'],gid) in GRUPO_PRODUTOS:
            more+=exemplos(GRUPO_PRODUTOS[(s['id'],gid)],heading=False)
        groups+=f'<section class="index-group" id="{gid}"><h2>{title}</h2><p>{description}</p><div class="topic-tags">{pills}</div>{more}</section>'
    intro=f'<nav class="crumb" aria-label="Percurso">{link("../index.html","Início")} / <span>{s["titulo"]}</span></nav><div class="page-intro"><span class="eyebrow">Explore a biblioteca</span><h1>{s["titulo"]}</h1><p>{s["resumo"]}</p></div>'
    jumps='<nav class="context-links jump-links" aria-label="Assuntos desta secção">'+''.join(link('#'+g[0],g[1]) for g in s['grupos'])+'</nav>'
    support='<section class="note"><h2>Comece com uma escolha informada</h2><p>Explore os processos já documentados e reúna as perguntas necessárias para o seu artigo.</p><div class="context-links">'+link('../guias/como-escolher-a-tecnica.html','Como escolher a técnica')+link('../tecnicas/index.html','Conhecer as técnicas')+'</div></section>'
    write(s['id']+'/index.html',shell(s['titulo'],s['resumo'],intro+jumps+cards+'<div class="index-groups">'+groups+'</div>'+support,'../',s['id']))
def homepage():
    main=(ROOT/'modelos/inicio.html').read_text(encoding='utf-8')
    main+=exemplos(['synex-20673','hetien-1364','sulkan-6620'],prefix='')
    write('index.html',shell('O universo dos brindes, explicado','Um projeto informativo da Nobrinde: técnicas de personalização, materiais, produtos e guias práticos.',main))
def search_page():
    entries=[dict(title=a['titulo'],category=SECS[a['sec']]['curto'],url=url(a),summary=a['resumo'],text=' '.join(p for _,p in a['seccoes'])+' '+a['tags']) for a in ARTIGOS]
    entries += [dict(title=s['titulo'],category='Secção',url=s['id']+'/index.html',summary=s['resumo'],text=' '.join(' '.join(g[1:]) for g in s['grupos'])) for s in SECCOES]
    for entry in entries:
        article_id=entry['url'].split('/')[-1].removesuffix('.html')
        if entry['url'].startswith('guias/') and article_id in GUIAS_POR_ID:
            entry['text']=texto_guia(GUIAS_POR_ID[article_id])
            continue
        if entry['url'].startswith('produtos/'):
            if article_id in FAMILIAS_PRODUTOS:
                entry['text']=' '.join(textos_publicos(FAMILIAS_PRODUTOS[article_id]))
            continue
        guide=BY_ID.get(article_id,{})
        if article_id=='crachas-automaticos':
            entry['text']+=' '+' '.join(t+' '+p for t,p in COMPONENTES_CRACHAS+PASSOS_CRACHAS+FAQ_CRACHAS)
        if article_id=='tecnica-troquelagem':
            entry['text']+=' '+' '.join(t+' '+p for t,p in OPERACOES_TROQUELAGEM+PASSOS_TROQUELAGEM+FAQ_TROQUELAGEM)
        if guide.get('checklist'):
            entry['text']+=' '+' '.join(t+' '+p for t,p in guide['checklist'])+' '+' '.join(t+' '+p for t,p in guide['problemas'])
        if guide.get('confirmar_bordado'):
            entry['text']+=' '+' '.join(t+' '+p for t,p in guide['confirmar_bordado'])+' '+' '.join(t+' '+p for t,p in guide['problemas'])
        if guide.get('esquema_guia'):
            entry['text']+=' '+' '.join(guide['confirmar'])+' '+' '.join(t+' '+p for t,p in guide['problemas'])
            entry['text']+=' '+' '.join(POR_ID[id]['nome']+' '+POR_ID[id]['ref'] for id in guide.get('produtos_guia',[]))
        audience=next((a for a in PUBLICOS if a['id']==article_id and entry['url'].startswith('publicos/')),None)
        if audience:
            entry['text']+=' '+' '.join(POR_ID[id]['nome']+' '+POR_ID[id]['ref']+' '+why+' '+' '.join(POR_ID[id]['factos']) for id,why in audience['selecoes'])
        for product_id in ARTIGO_PRODUTOS.get(article_id,[]):
            p=POR_ID[product_id]
            entry['text']+=' '+p['nome']+' '+p['ref']+' '+' '.join(p['factos'])
    write('assets/pesquisa-dados.js','window.BRINDES_SEARCH = '+json.dumps(entries,ensure_ascii=False).replace('<','\\u003c')+';\n')
    content='<nav class="crumb" aria-label="Percurso">'+link('index.html','Início')+' / Pesquisa</nav><div class="page-intro"><span class="eyebrow">Encontre a sua resposta</span><h1>Pesquisar na biblioteca</h1><p>Pesquise por técnica, produto, material ou dúvida.</p>'+search_form('')+'</div><p id="search-status" role="status" aria-live="polite"></p><div id="search-results" class="article-grid"></div><noscript><p>Ative JavaScript para pesquisar. Pode também navegar pelas secções abaixo.</p></noscript><section><h2>Explorar por assunto</h2><div class="context-links">'+''.join(link(s['id']+'/index.html',s['titulo']) for s in SECCOES)+'</div></section>'
    write('pesquisa.html',shell('Pesquisa','Pesquise os artigos e secções da biblioteca brindes.pt.',content,extra='<script src="assets/pesquisa-dados.js" defer></script><script src="pesquisa.js" defer></script>'))
if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--secao', choices=['produtos','guias'], help='Regenera a secção indicada e os índices, preservando o conteúdo das outras páginas.')
    args = parser.parse_args()
    node = shutil.which('node')
    prettier = ROOT/'node_modules/prettier/bin/prettier.cjs'
    if not node or not prettier.is_file():
        raise SystemExit('A geração requer Node.js e Prettier. Execute npm ci na pasta do projeto e volte a executar python gerar.py.')
    image_python = sys.executable if importlib.util.find_spec('PIL') else str(ROOT/'.venv/Scripts/python.exe')
    if not Path(image_python).is_file():
        raise SystemExit('A preparação das fotografias requer o ambiente Python existente com Pillow.')
    if not args.secao or args.secao=='produtos':
        subprocess.run([image_python, str(ROOT/'editorial/preparar_imagens_produtos.py')], cwd=ROOT, check=True)
    if not args.secao or args.secao=='guias':
        subprocess.run([image_python, str(ROOT/'editorial/preparar_imagens_guias.py')], cwd=ROOT, check=True)
    for section in SECCOES:
        if not args.secao or section['id']==args.secao: page_section(section)
    for article in ARTIGOS:
        if not args.secao or article['sec']==args.secao: page_article(article)
    if not args.secao: homepage()
    if args.secao:
        # A correção de identidade é partilhada; o texto alheio à secção
        # permanece como estava, incluindo alterações locais do utilizador.
        paths = ['index.html', 'pesquisa.html', 'creditos-imagens.html']
        paths += [s['id']+'/index.html' for s in SECCOES]
        paths += [url(a) for a in ARTIGOS]
        for path in paths:
            if path.startswith(args.secao+'/'): continue
            target = ROOT/path
            previous = target.read_text(encoding='utf-8')
            repaired = corrigir_imagens_removidas(previous, path)
            neutral = pagina_publica(repaired) if 'nobrinde' in repaired.lower() else corrigir_ligacoes(repaired)
            if path == 'creditos-imagens.html':
                section_id, credits = ('produtos-ilustrativos', CREDITOS_PRODUTOS) if args.secao=='produtos' else ('guias-ilustrativos', CREDITOS_GUIAS)
                neutral = re.sub(r'<section\b[^>]*id="'+section_id+r'"[^>]*>.*?</section>', '', neutral, flags=re.S)
                neutral = neutral.replace('</main>', credits + '</main>')
            if neutral != previous: target.write_text(neutral, encoding='utf-8')
    search_page()
    if not args.secao or args.secao=='produtos':
        write('assets/produtos-conteudos.json', dados_publicos(BY_ID))
    if not args.secao or args.secao=='guias':
        write('assets/guias-conteudos.json', dados_guias())
    if not args.secao:
        write('creditos-imagens.html',shell('Créditos de imagens','Autores, fontes, licenças e alterações das fotografias utilizadas no brindes.pt.',creditos() + CREDITOS_PRODUTOS + CREDITOS_GUIAS))
    outputs = ['index.html', 'pesquisa.html', 'creditos-imagens.html']
    outputs += [s['id']+'/index.html' for s in SECCOES]
    outputs += [url(a) for a in ARTIGOS]
    subprocess.run([node, str(prettier), '--write', '--log-level', 'warn', *outputs], cwd=ROOT, check=True)
    print(f'Geradas {8 if args.secao else len(SECCOES)+len(ARTIGOS)+3} páginas; pesquisa e dados públicos atualizados.')
