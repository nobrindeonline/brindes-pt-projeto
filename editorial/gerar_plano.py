"""Atualiza o inventário de conteúdos sem criar páginas públicas vazias."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from conteudos.catalogo import SECCOES, ARTIGOS

published={a['titulo'] for a in ARTIGOS}
requirements={
 'tecnicas':'Descrição e fontes do processo; equipamento; compatibilidade; cores; arte; limites; diagnóstico; comparação; casos reais autorizados.',
 'materiais':'Propriedades e composição; acabamentos; técnicas condicionais; ensaios de aderência/resistência; exemplos e fontes.',
 'produtos':'Variantes; utilização; materiais; áreas acessíveis; técnicas condicionais; problemas e ligações aos guias.',
 'guias':'Pergunta e objetivo; passos verificáveis; exemplos de arte autorizados; problemas; fontes e revisão técnica.',
 'publicos':'Necessidades próprias desse público; critérios; exemplos de utilização; produtos e guias relacionados, sem duplicar textos.',
 'industria':'Descrição do processo/equipamento; fontes primárias; fotografias autorizadas; relações entre etapas. História: datas e contexto português documentados.',
 'mercado':'Atividade e âmbito geográfico; fontes públicas atuais; utilidade editorial; data de revisão. Excluir dados internos.',
 'tendencias':'Data de publicação; acontecimento ou questão concreta; fontes atuais; âmbito de alegações ambientais; distinção dos guias permanentes.',
}
lines=['# Mapa e plano editorial','', 'Inventário gerado a partir de `conteudos/catalogo.py`. Os temas pendentes têm uma posição nos índices, mas não uma página individual vazia.', '', '## Páginas de entrada', '', '- `/index.html` — página inicial', '- `/pesquisa.html` — pesquisa local', '']
for s in SECCOES:
    lines+=['## '+s['titulo'],'',f"Índice: `/{s['id']}/index.html`",'', 'Para completar novos artigos: '+requirements[s['id']], '']
    for _,group,_,topics in s['grupos']:
        lines+=['### '+group,'']
        for topic in topics.split('|'):
            article=next((a for a in ARTIGOS if a['titulo']==topic),None)
            state=f"Pronto para revisão local — `/{article['sec']}/{article['id']}.html`" if article else ('Pronto para revisão local — `/industria/index.html#fluxo`' if s['id']=='industria' and topic=='O percurso de uma encomenda' else 'Por validar pela Nobrinde — reunir conteúdo e fontes antes de criar página')
            lines += [f'- **{topic}**: {state}.']
        lines += ['']
(ROOT/'editorial/plano.md').write_text('\n'.join(lines),encoding='utf-8')
print('Plano editorial atualizado.')
