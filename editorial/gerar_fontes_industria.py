"""Gera o registo de fontes públicas usado nos guias da secção Indústria."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from conteudos.industria import (  # noqa: E402
    AREAS_INDUSTRIA,
    DATA_REVISAO_TEXTO,
    ETAPAS,
    FONTES_INDUSTRIA,
    GRUPOS_INDUSTRIA,
    INDUSTRIA,
)

DATA_CONSULTA = "14 de outubro de 2026"
AMBITOS = {
    "ind_pad": "Componentes e funcionamento geral da tampografia.",
    "ind_screen": "Descrição geral da preparação e aplicação serigráfica.",
    "ind_screen_ink": "Dependência da cura UV em relação ao sistema de tinta e equipamento; não extrapolada a outras tintas.",
    "ind_laser": "Riscos do feixe e riscos não associados diretamente ao feixe; não é um procedimento operacional.",
    "ind_uv": "Impressão UV direta e dependência da configuração do equipamento.",
    "ind_dtf": "Definição e sequência geral de DTF, segundo a documentação do fabricante consultado.",
    "ind_embroidery": "Distinção e características gerais de pontos de bordado; sem transformar parâmetros de exemplo em limites universais.",
    "ind_seams": "Classificação e construção geral de costuras.",
    "ind_sublimation": "Exemplos de aplicação têxtil por sublimação em poliéster.",
    "ind_cutting": "Distinção entre corte, corte parcial e vinco em dados estruturais.",
    "ind_diecutting": "Exemplos de equipamentos planos e rotativos para corte e estampagem.",
    "ind_binding": "Exemplo de equipamento de encadernação adesiva e respetivas etapas gerais.",
    "ind_wire": "Sistema de argolagem e fatores que condicionam os resultados descritos pelo fabricante.",
    "ind_spiral": "Descrição geral de como uma espiral contínua atravessa furos no bordo de um documento.",
    "ind_history_ppai": "Relato da reunião de fabricantes em Chicago, em 1903; não sustenta uma origem universal dos objetos promocionais.",
    "ind_history_unesco": "Documentação de uma tradição chinesa de impressão a partir de blocos gravados; não apresentada como origem dos brindes.",
    "ind_history_espr": "Quadro regulamentar europeu para a conceção ecológica de produtos sustentáveis; não certifica artigos promocionais concretos.",
}

lines = [
    "# Fontes da secção Indústria",
    "",
    f"Última revisão editorial: {DATA_REVISAO_TEXTO}.",
    f"Consulta das fontes abaixo: {DATA_CONSULTA}.",
    "",
    "As páginas sintetizam documentação pública e explicações educativas. As referências",
    "de fabricantes descrevem os seus próprios sistemas; não estabelecem compatibilidade",
    "universal, capacidades locais ou condições de produção. Orientações de validação",
    "são editoriais e não instruções de operação.",
    "",
    "## Registo de fontes",
    "",
    "| Chave | Entidade ou autor | Título | URL | Data de consulta | Âmbito usado |",
    "| --- | --- | --- | --- | --- | --- |",
]

for key, (title, url) in FONTES_INDUSTRIA.items():
    entity, separator, source_title = title.partition(" — ")
    if not separator:
        entity, source_title = "Não indicado na página", title
    lines.append(
        f"| `{key}` | {entity} | {source_title} | <{url}> | {DATA_CONSULTA} | "
        f"{AMBITOS[key]} |"
    )

lines.extend(
    [
        "",
        "## Fontes por página",
        "",
        "| Página | Chaves de fontes |",
        "| --- | --- |",
    ]
)

for article in INDUSTRIA + AREAS_INDUSTRIA:
    source_keys = ", ".join(f"`{key}`" for key in article["fontes"]) or "Orientação editorial"
    lines.append(f"| `industria/{article['id']}.html` | {source_keys} |")

lines.extend(
    [
        "",
        "## Limites editoriais",
        "",
        "- O relato da PPAI documenta uma reunião associativa em 1903; não é usado como",
        "  prova da origem dos brindes ou da história do mercado português.",
        "- A referência de segurança laser não identifica materiais processáveis nem",
        "  substitui avaliação de risco, documentação do material ou instruções do fabricante.",
        "- Para UV DTF, a página distingue impressão direta de transferência em filme e",
        "  remete a validação de cada sistema para a respetiva documentação. A fonte UV",
        "  citada descreve impressão direta, não é apresentada como fonte de UV DTF.",
        "- As etapas de `Da ideia à entrega` são um exemplo editorial adaptável; podem",
        "  variar, ser opcionais ou decorrer em paralelo.",
        "- Foram selecionadas imagens locais apenas quando o conteúdo visível é pertinente.",
        "  As imagens da pasta da História foram excluídas por conterem datas ou marcas que",
        "  não podem ser usadas como evidência histórica ou imagem pública independente.",
        "- Não há imagens próprias por processo técnico em `assets/Industria`; não foram",
        "  preenchidos esses cartões com fotografias de outros temas.",
        "",
        "## Organização dos guias",
        "",
    ]
)

for group_id, title, description, ids in GRUPOS_INDUSTRIA:
    lines.append(f"- **{title}:** {description} Guias: {', '.join(ids)}.")

lines.extend(
    [
        "",
        "As etapas de `Da ideia à entrega` são:",
        "",
    ]
)
lines.extend(f"- {title}" for title, _, _ in ETAPAS)
lines.append("")

(ROOT / "editorial" / "fontes-industria.md").write_text(
    "\n".join(lines),
    encoding="utf-8",
)
print("Registo de fontes da secção Indústria atualizado.")
