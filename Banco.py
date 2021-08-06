import psycopg2
import psycopg2.extras
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import json

#definindo as configurações do banco de dados
host = "localhost"
dbname = "postgres"
user = "postgres"
password = "123456"

#colocando as informações declaradas na variavel conn
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

#cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#realizando a conexão com o banco e atribuindo essa conexão para a variavel teste
teste = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#criando a tabela empresa e definindo os campos
#teste.execute("CREATE TABLE empresa  (id SERIAL PRIMARY KEY, name VARCHAR, departamento VARCHAR);")

#teste.execute("INSERT INTO empresa (name) VALUES(%s)", ("Beatriz",))
#teste.execute("INSERT INTO empresa (departamento) VALUES(%s)", ("RH",))


#inserindo os dados na tabela empresa
'''
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Beatriz", "RH"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Amilton", "ADM"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Guilherme", "TI"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Ana", "TI"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Mauricio", "BI"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Andreia", "RH"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Carlos", "ADM"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Igor", "BI"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Ronald", "Suporte"))
'''

#executando um select na tabela empresa
teste.execute("SELECT * FROM empresa;")

#inserindo a lista de informações na variável lista
lista = [teste.fetchall()]

#realizando um commit no banco de dados
conn.commit()

#fechando a conexão com o banco
conn.close()

nome = []
departamento = []

for i in lista:
    for x in i:
        nome.append(x[1])
        departamento.append(x[2])

lista = dict(zip(nome, departamento))

with open('dados.json', 'w') as json_file:
    json.dump(lista, json_file, indent=4)
