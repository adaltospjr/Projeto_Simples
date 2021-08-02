from flask import Flask, render_template
import psycopg2
import psycopg2.extras

host = "localhost"
dbname = "postgres"
user = "postgres"
password = "123456"

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")

#cur.execute("INSERT INTO student (name) VALUES(%s)", ("Beatriz",))

cur.execute("SELECT * FROM student;")

#print(cur.fetchall())

lista = [cur.fetchall()]
lista_dois = []

#cur.fetchall()

#conn.commit()

conn.close()

app = Flask(__name__)

@app.route('/')
def ola():
    for i in lista:
        for y in i:
            lista_dois.append(y[1])
    return render_template('lista.html', titulo='Usuários', nomes=lista_dois)

app.run(debug=True)
