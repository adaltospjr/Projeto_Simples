from Banco import lista
import json

nome = []
departamento = []

lista = dict(zip(nome, departamento))

with open('dados.json', 'w') as json_file:
    json.dump(lista, json_file, indent=4)


#criando uma classe usuário
class Usuarios:
    def __init__(self):
        self.nome = []
        self.departamento = []

    def set_usuario(self, pessoa):
        for i in lista:
            for x in i:
                nome.append(x[1])
                departamento.append(x[2])
        
    def get_usuario(self):
        print(self.nome)

#instanciando a classe
pessoa1 = Usuarios()

#inserindo dados na pessoa1
pessoa1.set_usuario(lista)
pessoa1.get_usuario()
