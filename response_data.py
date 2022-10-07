import json
import pandas as pd
doses_aplicadas = 0

with open("data.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)
    triagem = dados['hits']['hits']
sources = list(map(lambda x: x["_source"],triagem))

df = pd.DataFrame(sources)

for dose in triagem:
    if '_id' in dose.keys():
        doses_aplicadas +=1

print(f'Doses aplicadas: {doses_aplicadas}')

fabricantes = list(map(lambda x: x['_source']['vacina_fabricante_nome'], triagem))

d = {x:fabricantes.count(x) for x in fabricantes}
for k,v in d.items():
    print(k,v)

df_contagem_municipio = df.groupby(["vacina_fabricante_nome", "estabelecimento_municipio_nome"])["vacina_fabricante_nome"].count().reset_index(name="contagem")
print(df_contagem_municipio)