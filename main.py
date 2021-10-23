import requests
from database import tabelas
from models import herois_models

for i in range(0,136):
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


tabelas.sair_app()