import requests
from database.tabelas import sair_app
from models.herois_models import api_herois

for i in range(0,200):
    payload = {'hero_id': i}
    url = requests.get('https://www.dota2.com/datafeed/herodata?language=brazilian', params=payload)
    dicionario = url.json()
    
    if url.status_code == 200 and dicionario['result']['status'] != 8:
        if dicionario['result']['data']['heroes'] != []:
            api_herois(dicionario)
            
            print(i)

        else:
            print('Requisição sem retorno')
    else:
        print('Requisição sem retorno')


sair_app()