from flask import Flask, render_template
from Classes import teste, dicionario

app = Flask(__name__)

@app.route('/usuarios')
def ola():
    return render_template('lista.html', titulo='Usuários', nomes=dicionario)

app.run(debug=True)
