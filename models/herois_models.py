from database import tabelas

def api_herois(dicionario):
    lista = []
    data = []
            
    remover = ['bio_loc','hype_loc','npe_desc_loc','role_levels','abilities','talents']
            
    for x in list(dicionario['result']['data']['heroes'][0]):
        if x not in remover:
            lista.append(x)
            
    for y in lista:
        data.append(dicionario['result']['data']['heroes'][0][y])           

    foto1= 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/' + str(dicionario['result']['data']['heroes'][0]['name']).replace('npc_dota_hero_', '') +'.png'
    foto2='https://cdn.cloudflare.steamstatic.com/apps/dota2/videos/dota_react/heroes/renders/'+ str(dicionario['result']['data']['heroes'][0]['name']).replace('npc_dota_hero_', '') +'.png'
    foto3='https://cdn.cloudflare.steamstatic.com/apps/dota2/videos/dota_react/heroes/renders/'+ str(dicionario['result']['data']['heroes'][0]['name']).replace('npc_dota_hero_', '') +'.webm'

    data.append(foto1)
    data.append(foto2)
    data.append(foto3)
            
    #Criação da tabela dos herois
    tabelas.criar_herois()
    tabelas.inserir_herois(data)
