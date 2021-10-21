from ..config.conexao import Conexao

#Criar Tabelas
def criar_herois():
    Conexao.criar("CREATE TABLE IF NOT EXISTS herois (id INT,name TEXT, order_id INT, name_loc TEXT, str_base INT, str_gain REAL, agi_base INT, agi_gain REAL, int_base INT, int_gain REAL, primary_attr INT, complexity INT, attack_capability INT, damage_min INT, damage_max INT, attack_rate REAL, attack_range INT, projectile_speed INT, armor REAL, magic_resistance INT, movement_speed INT , turn_rate REAL , sight_range_day INT , sight_range_night INT, max_health INT, health_regen REAL, max_mana INT, mana_regen REAL, link_heroes_p TEXT, link_heroes_p1 TEXT, link_heroes_p2 TEXT)")

def criar_talentos():
    Conexao.criar("CREATE TABLE IF NOT EXISTS talentos (id INT, name TEXT, name_loc TEXT,	desc_loc TEXT, lore_loc TEXT, notes_loc TEXT, shard_loc TEXT, scepter_loc TEXT, type TEXT, behavior TEXT, target_team TEXT,	target_type TEXT,	flags TEXT,	damage TEXT,	immunity TEXT,	dispellable TEXT,	max_level TEXT,	cast_ranges TEXT,	cast_points TEXT,	channel_times TEXT,	cooldowns TEXT,	durations TEXT,	damages TEXT,	mana_costs TEXT,	gold_costs TEXT,	special_values TEXT,	is_item TEXT,	ability_has_scepter TEXT,	ability_has_shard TEXT,	ability_is_granted_by_scepter TEXT,	ability_is_granted_by_shard TEXT,	item_cost TEXT,	item_initial_charges TEXT,	item_neutral_tier TEXT,	item_stock_max TEXT, item_stock_time TEXT,	item_quality TEXT, name_id TEXT, values_float TEXT,	values_int TEXT, is_percentage TEXT, heading_loc TEXT)")

def criar_habilidades():
    Conexao.criar("CREATE TABLE IF NOT EXISTS habilidades (id INT, name TEXT, name_loc TEXT,	desc_loc TEXT, lore_loc TEXT, notes_loc TEXT, shard_loc TEXT, scepter_loc TEXT, type TEXT, behavior TEXT, target_team TEXT,	target_type TEXT,	flags TEXT,	damage TEXT,	immunity TEXT,	dispellable TEXT,	max_level TEXT,	cast_ranges TEXT,	cast_points TEXT,	channel_times TEXT,	cooldowns TEXT,	durations TEXT,	damages TEXT,	mana_costs TEXT,	gold_costs TEXT,	special_values TEXT,	is_item TEXT,	ability_has_scepter TEXT,	ability_has_shard TEXT,	ability_is_granted_by_scepter TEXT,	ability_is_granted_by_shard TEXT,	item_cost TEXT,	item_initial_charges TEXT,	item_neutral_tier TEXT,	item_stock_max TEXT, item_stock_time TEXT,	item_quality TEXT, name_id TEXT, values_float TEXT,	values_int TEXT, is_percentage TEXT, heading_loc TEXT)")

def criar_items():
    Conexao.criar()

#Inserir Tabelas
def inserir_herois(data):
    Conexao.inserir("INSERT INTO herois (id, name, order_id, name_loc, str_base, str_gain, agi_base, agi_gain, int_base, int_gain, primary_attr, complexity, attack_capability, damage_min, damage_max, attack_rate, attack_range, projectile_speed, armor, magic_resistance, movement_speed, turn_rate, sight_range_day, sight_range_night, max_health, health_regen, max_mana, mana_regen, link_heroes_p, link_heroes_p1, link_heroes_p2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", data)

def inserir_talentos(data):
    Conexao.inserir("INSERT INTO talentos () VALUES ()", data)

def inserir_habilidades(data):
    Conexao.inserir("INSERT INTO habilidades () VALUES ()", data)

def inserir_items(data):
    Conexao.inserir("INSERT INTO items () VALUES ()", data)

#Fechar Conexão
def sair_app():
    Conexao.sair()