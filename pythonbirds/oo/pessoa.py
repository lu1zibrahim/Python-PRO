
class Pessoa:
    OLHOS = 2

    def __init__(self, *filhos, nome = None, idade = 27):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.OLHOS}'

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
    luiz.OLHOS = 1
    del luiz.OLHOS
    carlos.sobrenome = "Ibrahim"
    print(carlos.sobrenome)
    del carlos.filhos
    print(carlos.__dict__)
    print(luiz.__dict__)
    Pessoa.OLHOS = 3
    print(Pessoa.OLHOS)
    print(luiz.OLHOS)
    print(id(Pessoa.OLHOS), id(luiz.OLHOS), id (carlos.OLHOS))
    print(Pessoa.metodo_estatico(), luiz.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luiz.nome_e_atributos_de_classe())
