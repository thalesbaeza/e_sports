from conexao import Conexao

#Criar
def criar_herois():
    Conexao.criar("CREATE TABLE IF NOT EXISTS herois (id INT,name TEXT, order_id INT, name_loc TEXT, str_base INT, str_gain REAL, agi_base INT, agi_gain REAL, int_base INT, int_gain REAL, primary_attr INT, complexity INT, attack_capability INT, damage_min INT, damage_max INT, attack_rate REAL, attack_range INT, projectile_speed INT, armor REAL, magic_resistance INT, movement_speed INT , turn_rate REAL , sight_range_day INT , sight_range_night INT, max_health INT, health_regen REAL, max_mana INT, mana_regen REAL, link_heroes_p TEXT, link_heroes_p1 TEXT, link_heroes_p2 TEXT)")

def criar_talentos():
    Conexao.criar()

def criar_habilidades():
    Conexao.criar()

def criar_items():
    Conexao.criar()


#Inserir
def inserir_herois(data):
    Conexao.inserir("INSERT INTO herois (id, name, order_id, name_loc, str_base, str_gain, agi_base, agi_gain, int_base, int_gain, primary_attr, complexity, attack_capability, damage_min, damage_max, attack_rate, attack_range, projectile_speed, armor, magic_resistance, movement_speed, turn_rate, sight_range_day, sight_range_night, max_health, health_regen, max_mana, mana_regen, link_heroes_p, link_heroes_p1, link_heroes_p2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", data)

def inserir_talentos():
    pass

def inserir_habilidades():
    pass

def inserir_items():
    pass