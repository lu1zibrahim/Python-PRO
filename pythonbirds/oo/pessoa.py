
class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 27):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == "__main__":
    luiz = Pessoa(nome='Luiz')
    carlos = Pessoa(luiz, nome='Carlos')
    print(Pessoa.cumprimentar(luiz))
    print(id(luiz))
    print(luiz.cumprimentar())
    print(luiz.nome)
    print(carlos.nome)
    print(carlos.idade)
    for filho in carlos.filhos:
        print(filho.nome)
    carlos.sobrenome = "Ibrahim"
    print(carlos.sobrenome)
    del carlos.filhos
    print(carlos.__dict__)
    print(luiz.__dict__)