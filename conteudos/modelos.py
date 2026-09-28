"""Copie o modelo pretendido para ARTIGOS em catalogo.py e complete-o.
Os modelos não são publicados. Os quatro tipos usam o mesmo renderizador.
"""
from copy import deepcopy

BASE = {'id':'', 'sec':'', 'tipo':'', 'titulo':'', 'resumo':'', 'seccoes':[],
        'problemas':[], 'fontes':[], 'relacionados':[], 'ancoras':[], 'tags':''}
TITULOS = {
 'tecnica': ['Como funciona','Equipamentos','Materiais e produtos','Cores e acabamentos','Preparação da arte','Condições a confirmar','Limitações','Comparar alternativas'],
 'material': ['Propriedades relevantes','Acabamentos habituais','Produtos frequentes','Técnicas a considerar','Condições que precisam de teste','Limitações e cuidados'],
 'produto': ['Variantes e utilização','Materiais e acabamentos','Técnicas a considerar','Área e preparação da arte','Problemas frequentes','Antes de escolher'],
 'guia': ['Objetivo','Informação necessária','Passos a seguir','Erros a evitar','O que confirmar no final'],
}
def novo(tipo):
    modelo=deepcopy(BASE)
    modelo.update(tipo=tipo,sec={'tecnica':'tecnicas','material':'materiais','produto':'produtos','guia':'guias'}[tipo],seccoes=[(t,'') for t in TITULOS[tipo]])
    return modelo
