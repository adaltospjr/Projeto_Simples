from Banco import lista, dicionario

#declarando um dicionário vazio
dicionario = {}

#criando uma classe usuário
class Usuarios:
    def __init__(self):
        self.informacoes = []

    def set_usuario(self, pessoa):
        for x in pessoa:
            for y in x:
                dicionario[y[1]] = y[2]
            self.informacoes.append(dicionario)

    def get_usuario(self):
        return self.informacoes

#instanciando a classe
pessoa1 = Usuarios()

#inserindo dados na pessoa1
pessoa1.set_usuario(lista)
teste = pessoa1.get_usuario()
