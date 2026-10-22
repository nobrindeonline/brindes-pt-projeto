"""Verificações da secção Indústria e das diretivas de rastreio."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from conteudos.industria import (  # noqa: E402
    AREAS_INDUSTRIA,
    INDUSTRIA,
    PROCESSOS_INDUSTRIA,
)
from conteudos.historia_brindes import HISTORIA, FONTES as FONTES_HISTORIA, GALERIA, CRONOLOGIA


class TagsImagem(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sem_alt = []
        self.srcs = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            atributos = dict(attrs)
            if not atributos.get("alt", "").strip():
                self.sem_alt.append(atributos.get("src", "(sem src)"))
            if atributos.get("src"):
                self.srcs.append(atributos["src"])


esperadas = {f"{artigo['id']}.html" for artigo in INDUSTRIA + AREAS_INDUSTRIA}
esperadas.add("index.html")
encontradas = {ficheiro.name for ficheiro in (ROOT / "industria").glob("*.html")}
assert encontradas == esperadas, (
    f"Rotas divergentes: em falta {sorted(esperadas - encontradas)}; "
    f"não registadas {sorted(encontradas - esperadas)}"
)

proibidos = re.compile(
    r"nobrinde|general catalogue|cat[aá]logo|\bsku\b|"
    r"trombolix|gratox|hetien|farnes|larsen|mckinley|"
    r"cornell|1881|1896|c\. p\. bourg",
    re.IGNORECASE,
)

for nome in esperadas:
    pagina = (ROOT / "industria" / nome).read_text(encoding="utf-8")
    assert '<html lang="pt-PT">' in pagina, f"Idioma ausente em {nome}"
    assert re.search(r'<meta\s+name="description"\s+content="[^"]*"', pagina), (
        f"Descrição ausente em {nome}"
    )
    assert re.search(r'<meta\s+name="robots"\s+content="index,\s*follow"', pagina), (
        f"Rastreio não permitido em {nome}"
    )
    assert "<title>" in pagina and "</title>" in pagina, f"Título ausente em {nome}"
    assert re.search(r'<main\s+id="conteudo"', pagina), f"Conteúdo HTML inicial ausente em {nome}"
    assert not proibidos.search(pagina), f"Referência proibida em {nome}"
    assert "industry-review" in pagina, f"Data de revisão ausente em {nome}"
    artigo=next((a for a in INDUSTRIA+AREAS_INDUSTRIA if nome==a['id']+'.html'),None)
    data=artigo['data_revisao'] if artigo else '2026-10-14'
    data_texto=artigo['data_revisao_texto'] if artigo else '14 de outubro de 2026'
    assert f'datetime="{data}">{data_texto}</time>' in pagina, (
        f"Data de revisão incoerente em {nome}"
    )

    imagens = TagsImagem()
    imagens.feed(pagina)
    assert not imagens.sem_alt, f"Imagens sem texto alternativo em {nome}: {imagens.sem_alt}"
    for src in imagens.srcs:
        parsed = urlsplit(src)
        if not parsed.scheme and not parsed.netloc:
            alvo = ((ROOT / "industria" / nome).parent / unquote(parsed.path)).resolve()
            assert alvo.is_file(), f"Imagem inexistente em {nome}: {src}"

maquinas = (ROOT / "industria" / "maquinas-e-processos.html").read_text(encoding="utf-8")
for processo in PROCESSOS_INDUSTRIA:
    if processo["guia"]:
        assert f'href="{processo["guia"]}"' in maquinas, (
            f"Guia de equipamento não ligado: {processo['guia']}"
        )
    for _, url in processo["tecnicas"]:
        assert f'href="{url}"' in maquinas, f"Técnica não ligada: {url}"

for tecnica in {
    urlsplit(url).path.replace("../", "")
    for processo in PROCESSOS_INDUSTRIA
    for _, url in processo["tecnicas"]
}:
    assert (ROOT / tecnica).is_file(), f"Página de técnica inexistente: {tecnica}"

for guia in {
    processo["guia"]
    for processo in PROCESSOS_INDUSTRIA
    if processo["guia"]
}:
    assert (ROOT / "industria" / guia).is_file(), f"Página da Indústria inexistente: {guia}"

pagina_principal = (ROOT / "industria" / "index.html").read_text(encoding="utf-8")
for rota in {
    "historia-dos-brindes.html",
    "da-ideia-a-entrega.html",
    "maquinas-e-processos.html",
    "montagem-embalagem-expedicao.html",
}:
    assert f'href="{rota}"' in pagina_principal, f"Cartão principal sem destino: {rota}"
assert "assets/Industria/IdeiaAteEntrega/brindes-para-feiras.jpg" in pagina_principal
assert "assets/Industria/MaquinaseProcessos/images.jpg" in pagina_principal
assert "assets/Industria/Montagem/images.jpg" in pagina_principal
assert HISTORIA['imagem_cartao']['src'] in pagina_principal
cartao_historia = pagina_principal.split('id="historia"', 1)[1].split("</article>", 1)[0]
assert cartao_historia.count(HISTORIA['titulo']) == 1
assert "<span>" not in cartao_historia

historia = (ROOT / "industria" / "historia-dos-brindes.html").read_text(encoding="utf-8")
for url in (f['url'] for f in FONTES_HISTORIA.values()):
    assert url in historia, f"Fonte da cronologia não ligada: {url}"

# A cronologia, a associação imagem/objeto e os destinos antigos sobrevivem à geração.
for n in range(8):
    assert f'id="parte-{n}"' in historia
assert historia.count('class="history-object"')==4
assert historia.count('class="history-object-image"')==4
assert [historia.index('id="'+p['id']+'"') for p in GALERIA]==sorted(historia.index('id="'+p['id']+'"') for p in GALERIA)
for p in CRONOLOGIA:
    assert 'id="'+p['id']+'"' in historia
for p in GALERIA:
    bloco=historia.split('id="'+p['id']+'"',1)[1].split('</article>',1)[0]
    assert p['ficheiro'] in bloco and p['alt'] in bloco
    assert all('#fonte-'+key in bloco for key in p['fontes'])
reguas=historia.split('id="reguas-publicitarias"',1)[1].split('</article>',1)[0]
assert 'calendário' not in reguas.casefold() and 'calendários' not in reguas.casefold()
assert 'datas por confirmar' in reguas
assert '1557239744369.jpg' not in historia

logistica = (ROOT / "industria" / "montagem-embalagem-expedicao.html").read_text(
    encoding="utf-8"
)
for termo in ("transportador", "morada particular ou empresarial", "armazenamento temporário"):
    assert termo.casefold() in logistica.casefold(), f"Âmbito logístico ausente: {termo}"

robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
assert re.search(r"User-agent:\s*Googlebot\s+Allow:\s*/", robots, re.IGNORECASE)
assert re.search(r"User-agent:\s*OAI-SearchBot\s+Allow:\s*/", robots, re.IGNORECASE)
assert re.search(r"User-agent:\s*GPTBot\s+Allow:\s*/", robots, re.IGNORECASE)

outra_secao = (ROOT / "tecnicas" / "index.html").read_text(encoding="utf-8")
assert re.search(r'<meta\s+name="robots"\s+content="noindex,\s*nofollow"', outra_secao)

print(
    f"OK: {len(esperadas)} páginas da Indústria, metadados, rotas de processos, "
    "imagens e textos alternativos."
)
