import psycopg2

class Conexao():
    def __init__(self, localhost="localhost", db="postgres", user="postgres", password="admin", port=5432):
        self.conn = psycopg2.connect(host=localhost, database=db, user=user , password=password, port=port)
        self.cur = self.conn.cursor()

    def criar(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def inserir(self, query, data):
        self.cur.execute(query, data)
        self.conn.commit()

    def sair(self):
        self.cur.close()
        self.conn.close()
