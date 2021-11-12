
class Pessoa:
    OLHOS = 2

    def __init__(self, *filhos, nome = None, idade = 27):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é  {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.OLHOS}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    OLHOS = 3

if __name__ == "__main__":
    luiz = Mutante(nome='Luiz')
    carlos = Homem(luiz, nome='Carlos')
    print(Pessoa.cumprimentar(luiz))
    print(id(luiz))
    print(luiz.cumprimentar())
    print(luiz.nome)
    print(carlos.nome)
    print(carlos.idade)
    for filho in carlos.filhos:
        print(filho.nome)
    luiz.OLHOS = 1
    del luiz.OLHOS
    carlos.sobrenome = "Ibrahim"
    print(carlos.sobrenome)
    del carlos.filhos
    print(carlos.__dict__)
    print(luiz.__dict__)
    print(Pessoa.OLHOS)
    print(luiz.OLHOS)
    print(id(Pessoa.OLHOS), id(luiz.OLHOS), id (carlos.OLHOS))
    print(Pessoa.metodo_estatico(), luiz.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luiz.nome_e_atributos_de_classe())
    pessoa = Pessoa("Anonimo")
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(luiz, Pessoa))
    print(isinstance(luiz, Homem))
    print(luiz.OLHOS)
    print(luiz.cumprimentar())
    print(carlos.cumprimentar())