import requests
from database import tabelas
from models import herois_models, herois_descricao


url2 = requests.get("https://api.opendota.com/api/heroes")
dicionario2 = url2.json()

for i in range(0,137):
    payload = {'hero_id': i}
    url = requests.get('https://www.dota2.com/datafeed/herodata?language=brazilian', params=payload)
    dicionario = url.json()
    
    if url.status_code == 200 and dicionario['result']['status'] != 8:
        if dicionario['result']['data']['heroes'] != []:
            herois_models.api_herois(dicionario)
            
            print(i)

        else:
            print('Requisição sem retorno')
    else:
        print('Requisição sem retorno')

for p in range(0,136):
    herois_descricao.api_herois_descricao(dicionario2, p)

tabelas.sair_app()