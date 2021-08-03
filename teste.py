from flask import Flask, render_template

app = Flask(__name__)

class Usuario:
    def __init__(self, nome, sobrenome, departamento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.departamento = departamento

    def get_info(self):
        informacoes = self.nome, self.sobrenome, self.departamento
        return informacoes

@app.route('/inicio')
def ola():
    usuario1 = Usuario('Adalto', 'Linhares', 'TI')
    usuario2 = Usuario('Beatriz', 'Silva', 'RH')
    usuario3 = Usuario('Leticia', 'Alves', 'MPN')

    lista = [usuario1.get_info(), usuario2.get_info(), usuario3.get_info()]

    return render_template('lista.html', titulo='Usuários', nomes=lista)

app.run(debug=True)
