from flask import Flask, render_template
from Classes import teste

app = Flask(__name__)

@app.route('/')
def ola():
    return render_template('lista.html', titulo='Usuários', nomes=teste)

app.run(debug=True)
