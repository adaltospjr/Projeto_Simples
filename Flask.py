from flask import Flask, render_template
from Classes import lista

app = Flask(__name__)

@app.route('/usuarios')
def ola():
    return render_template('lista.html', titulo='Usuários', nomes=lista)

app.run(debug=True)
