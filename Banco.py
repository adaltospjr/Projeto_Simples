from flask import Flask, render_template
import psycopg2
import psycopg2.extras

host = "localhost"
dbname = "postgres"
user = "postgres"
password = "123456"

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

#cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

teste = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR, departamento VARCHAR);")

#teste.execute("CREATE TABLE empresa  (id SERIAL PRIMARY KEY, name VARCHAR, departamento VARCHAR);")

#teste.execute("INSERT INTO empresa (name) VALUES(%s)", ("Beatriz",))
#teste.execute("INSERT INTO empresa (departamento) VALUES(%s)", ("RH",))

'''
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Beatriz", "RH"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Amilton", "ADM"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Guilherme", "TI"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Ana", "TI"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Mauricio", "BI"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Andreia", "RH"))
teste.execute("INSERT INTO empresa (name, departamento) VALUES (%s, %s)",("Carlos", "ADM"))
'''

#teste.execute('TRUNCATE TABLE empresa')

teste.execute("SELECT * FROM empresa;")

#print(teste.fetchall())

lista = [teste.fetchall()]
lista_programa = []
dicionario = {}

conn.commit()

conn.close()

for x in dicionario:
    print(dicionario[x])

class Usuario:
    def __init__(self):
        self.nome = []
        self.departamento = []

    def set_usuario(self, pessoa):
        for x in pessoa:
            for y in x:
                dicionario[y[1]] = y[2]
            self.nome.append(dicionario)

    def get_usuario(self):
        return self.nome

pessoa1 = Usuario()
pessoa1.set_usuario(lista)
teste = pessoa1.get_usuario()
print(teste)

app = Flask(__name__)

@app.route('/')
def ola():
    return render_template('lista.html', titulo='Usuários', nomes=teste)

app.run(debug=True)
