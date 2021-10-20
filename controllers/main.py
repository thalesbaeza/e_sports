import requests
from ..models.conexao import Conexao

db = Conexao()


for i in range(0,200):
    payload = {'hero_id': i}
    url = requests.get('https://www.dota2.com/datafeed/herodata?language=brazilian', params=payload)
    dicionario = url.json()
    
    if url.status_code == 200 and dicionario['result']['status'] != 8:
        if dicionario['result']['data']['heroes'] != []:
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
            db.criar("CREATE TABLE IF NOT EXISTS herois (id INT,name TEXT, order_id INT, name_loc TEXT, str_base INT, str_gain REAL, agi_base INT, agi_gain REAL, int_base INT, int_gain REAL, primary_attr INT, complexity INT, attack_capability INT, damage_min INT, damage_max INT, attack_rate REAL, attack_range INT, projectile_speed INT, armor REAL, magic_resistance INT, movement_speed INT , turn_rate REAL , sight_range_day INT , sight_range_night INT, max_health INT, health_regen REAL, max_mana INT, mana_regen REAL, link_heroes_p TEXT, link_heroes_p1 TEXT, link_heroes_p2 TEXT)")
            db.inserir("INSERT INTO herois (id, name, order_id, name_loc, str_base, str_gain, agi_base, agi_gain, int_base, int_gain, primary_attr, complexity, attack_capability, damage_min, damage_max, attack_rate, attack_range, projectile_speed, armor, magic_resistance, movement_speed, turn_rate, sight_range_day, sight_range_night, max_health, health_regen, max_mana, mana_regen, link_heroes_p, link_heroes_p1, link_heroes_p2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", data)

            #Criação da tabela das Habilidades
            db.criar("CREATE TABLE IF NOT EXISTS habilidades (id INT, name TEXT, name_loc TEXT,	desc_loc TEXT, lore_loc TEXT, notes_loc TEXT, shard_loc TEXT, scepter_loc TEXT, type TEXT, behavior TEXT, target_team TEXT,	target_type TEXT,	flags TEXT,	damage TEXT,	immunity TEXT,	dispellable TEXT,	max_level TEXT,	cast_ranges TEXT,	cast_points TEXT,	channel_times TEXT,	cooldowns TEXT,	durations TEXT,	damages TEXT,	mana_costs TEXT,	gold_costs TEXT,	special_values TEXT,	is_item TEXT,	ability_has_scepter TEXT,	ability_has_shard TEXT,	ability_is_granted_by_scepter TEXT,	ability_is_granted_by_shard TEXT,	item_cost TEXT,	item_initial_charges TEXT,	item_neutral_tier TEXT,	item_stock_max TEXT, item_stock_time TEXT,	item_quality TEXT, name_id TEXT, values_float TEXT,	values_int TEXT, is_percentage TEXT, heading_loc TEXT)")
            db.inserir("INSERT INTO habilidades () VALUES ()",data)

            #Criação da tabela Árvore de Talentos
            db.criar("CREATE TABLE IF NOT EXISTS talentos (id INT, name TEXT, name_loc TEXT, desc_loc TEXT,	lore_loc TEXT,	notes_loc TEXT,	shard_loc TEXT,	scepter_loc TEXT, type TEXT, behavior TEXT,	target_team TEXT, target_type TEXT,	flags TEXT,	damage TEXT, immunity TEXT,	dispellable TEXT,	max_level TEXT,	cast_ranges TEXT,	cast_points TEXT,	channel_times TEXT,	cooldowns TEXT,	durations TEXT,	damages TEXT,	mana_costs TEXT,	gold_costs TEXT,	special_values TEXT,	is_item TEXT,	ability_has_scepter TEXT,	ability_has_shard TEXT,	ability_is_granted_by_scepter TEXT,	ability_is_granted_by_shard TEXT,	item_cost TEXT,	item_initial_charges TEXT,	item_neutral_tier TEXT,	item_stock_max TEXT, item_stock_time TEXT,	item_quality TEXT, name_id TEXT, values_float TEXT,	values_int TEXT, is_percentage TEXT, heading_loc TEXT)")
            db.inserir("INSERT INTO talentos () VALUES ()", data)

            print(i)

        else:
            print('Requisição sem retorno')
    else:
        print('Requisição sem retorno')


db.sair()