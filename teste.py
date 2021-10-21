import requests

from config.conexao import Conexao

db = Conexao()

payload = {'hero_id': 111}
url = requests.get('https://www.dota2.com/datafeed/herodata?language=brazilian', params=payload)
dicionario = url.json()

amostrar=dicionario['result']['data']['heroes'][0]['name']


#foto1= 'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/' + str(amostrar).replace('npc_dota_hero_', '') +'.png'

#foto2='https://cdn.cloudflare.steamstatic.com/apps/dota2/videos/dota_react/heroes/renders/'+ str(amostrar).replace('npc_dota_hero_', '') +'.png'

#foto3='https://cdn.cloudflare.steamstatic.com/apps/dota2/videos/dota_react/heroes/renders/'+ str(amostrar).replace('npc_dota_hero_', '') +'.webm'



# for x in list(dicionario['result']['data']['heroes'][0]):
#     if x not in remover:
#         lista.append(x)
            
# for y in lista:
#     data.append(dicionario['result']['data']['heroes'][0][y])


# print(lista)
# print()
# print(data)

#data.append(foto1)
#data.append(foto2)
#data.append(foto3)

#print(data)

#foto 3x4 do heroi
#https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/ancient_apparition.png

#foto 16' do heroi
#https://cdn.cloudflare.steamstatic.com/apps/dota2/videos/dota_react/heroes/renders/ancient_apparition.png

#vídeo do heroi
#https://cdn.cloudflare.steamstatic.com/apps/dota2/videos/dota_react/heroes/renders/ancient_apparition.webm

lista = []
data = []
            
remover = ['notes_loc','channel_times', 'cooldowns', 'durations', 'damages', 'special_values', 'cast_ranges', 'cast_points' , 'mana_costs', 'gold_costs']
 
a = list(dicionario['result']['data']['heroes'][0]['abilities'][0])

#print(dicionario['result']['data']['heroes'][0]['abilities'][0])  

for l in list(dicionario['result']['data']['heroes'][0]['abilities'][0]):
    if l not in remover:
        lista.append(l)

#print(lista)

for m in lista:
    data.append(dicionario['result']['data']['heroes'][0]['abilities'][0][m])

#print(data)

data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['notes_loc'])

#for in
for o in range(0,3):
    data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['channel_times'][o])
    data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['cooldowns'][o])
    data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['durations'][o])
    data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['damages'][o])

data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['cast_ranges'][0])
data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['cast_points'][0])
data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['mana_costs'][0])
data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['gold_costs'])

# print(dicionario['result']['data']['heroes'][0]['abilities'][0]['special_values'][0])

data2 =[]


try:
    for p in range(0,20):
        if dicionario['result']['data']['heroes'][0]['abilities'][p]['id'] > 0:
            data2.append(dicionario['result']['data']['heroes'][0]['abilities'][p])
           
            lista = []
            data = []
           
            remover = ['notes_loc','channel_times', 'cooldowns', 'durations', 'damages', 'special_values', 'cast_ranges', 'cast_points' , 'mana_costs', 'gold_costs']
 

            for l in list(dicionario['result']['data']['heroes'][0]['abilities'][0]):
                if l not in remover:
                    lista.append(l)

            for m in lista:
                data.append(dicionario['result']['data']['heroes'][0]['abilities'][0][m])


            for o in range(0,3):
                data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['channel_times'][o])
                data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['cooldowns'][o])
                data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['durations'][o])
                data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['damages'][o])

            data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['cast_ranges'][0])
            data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['cast_points'][0])
            data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['mana_costs'][0])
            data.append(dicionario['result']['data']['heroes'][0]['abilities'][0]['gold_costs'])

            print(data)
        else:
            print('Requisição sem retorno')
except IndexError:
    pass






# print(data)

#outro for in 
#print(dicionario['result']['data']['heroes'][0]['abilities'][0]['special_values'][0])



#print(list(dicionario['result']['data']['heroes'][0]['abilities'][0]))

#pega icone do poder 'name' = invoker_invoke
#https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/abilities/invoker_invoke.png

#print(dicionario['result']['data']['heroes'][0]['abilities'][0])

#print(len(dicionario['result']['data']['heroes'][0]['abilities'][1]['special_values']))

# dataset1 = []
# talento = []
# lista = list(dicionario['result']['data']['heroes'][0]['abilities'][0]) 

# retirar = ['notes_loc', 'special_values', 'lore_loc']



#for xis in lista:
#    if xis not in retirar:
#        dataset1.append(xis)

#for yis in dataset1:
#    talento.append(dicionario['result']['data']['heroes'][0]['abilities'][0])


#
#
#

#print(list(dicionario['result']['data']['heroes'][0]['abilities'][0]))
#print()
#print(list(dicionario['result']['data']['heroes'][0]['abilities'][0]['special_values'][0]))
#print()
#print()
# print(list(dicionario['result']['data']['heroes'][0]['talents'][0]))
# print()
# print(list(dicionario['result']['data']['heroes'][0]['talents'][0]['special_values'][0]))
# print()



# for xis in list(dicionario['result']['data']['heroes'][0]['talents'][0]):
#     if xis not in retirar:
#         dataset1.append(xis)

# for yis in dataset1:
#     talento.append(dicionario['result']['data']['heroes'][0]['talents'][0][yis])


# for zis in list(dicionario['result']['data']['heroes'][0]['talents'][0]['special_values'][0]):
#     talento.append(dicionario['result']['data']['heroes'][0]['talents'][0]['special_values'][0][zis])

# print(talento)

# db.criar("CREATE TABLE IF NOT EXISTS talentos (id INT, name TEXT, name_loc TEXT, desc_loc TEXT,	lore_loc TEXT,	notes_loc TEXT,	shard_loc TEXT,	scepter_loc TEXT, type TEXT, behavior TEXT,	target_team TEXT, target_type TEXT,	flags TEXT,	damage TEXT, immunity TEXT,	dispellable TEXT,	max_level TEXT,	cast_ranges TEXT,	cast_points TEXT,	channel_times TEXT,	cooldowns TEXT,	durations TEXT,	damages TEXT,	mana_costs TEXT,	gold_costs TEXT,	special_values TEXT,	is_item TEXT,	ability_has_scepter TEXT,	ability_has_shard TEXT,	ability_is_granted_by_scepter TEXT,	ability_is_granted_by_shard TEXT,	item_cost TEXT,	item_initial_charges TEXT,	item_neutral_tier TEXT,	item_stock_max TEXT, item_stock_time TEXT,	item_quality TEXT, name_id TEXT, values_float TEXT,	values_int TEXT, is_percentage TEXT, heading_loc TEXT)")
# db.inserir("INSERT INTO talentos (id, name, name_loc, desc_loc, lore_loc, notes_loc, shard_loc, scepter_loc, type, behavior, target_team, target_type, flags, damage, immunity, dispellable, max_level, cast_ranges, cast_points, channel_times, cooldowns, durations, damages, mana_costs, gold_costs, special_values, is_item, ability_has_scepter, ability_has_shard, ability_is_granted_by_scepter, ability_is_granted_by_shard, item_cost, item_initial_charges, item_neutral_tier, item_stock_max, item_stock_time, item_quality,name, values_float, values_int, is_percentage, heading_loc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", talento)
# db.sair()
#cast_ranges cast_points
#Habilidade
#print(dicionario['result']['data']['heroes'][0]['abilities'][0]['special_values'][10])

#Talentos
#print(dicionario['result']['data']['heroes'][0]['abilities'][1])





# 'cast_ranges' 'cast_points' 'durations' 'damages' 'mana_costs' 'gold_costs' 'special_values'

#for xis in lista:
#    print(dicionario['result']['data']['heroes'][0]['abilities'][1][xis])

#try:
#    for x in range(0,20):
#        if dicionario['result']['data']['heroes'][0]['abilities'][x]['id'] > 0:
#            print(dicionario['result']['data']['heroes'][0]['abilities'][x])
#        else:
#            print('Requisição sem retorno')
#except IndexError:
#    pass



#lista = list(dicionario['result']['data']['heroes'][0]['abilities'][0])


#execute('''CREATE TABLE IF NOT EXISTS herois (id INT,name TEXT, order_id INT, name_loc TEXT, str_base INT, str_gain REAL, agi_base INT, agi_gain REAL, int_base INT, int_gain REAL, primary_attr INT, complexity INT, attack_capability INT, damage_min INT, damage_max INT, attack_rate REAL, attack_range INT, projectile_speed INT, armor REAL, magic_resistance INT, movement_speed INT , turn_rate REAL , sight_range_day INT , sight_range_night INT, max_health INT, health_regen REAL, max_mana INT, mana_regen REAL, link_heroes_p TEXT, link_heroes_p1 TEXT, link_heroes_p2 TEXT)''')