"""
Você deve criar uma classe carro que vai ossuir dois atributos compostos por outras duas classes:

1 ) Motor
2 ) DIrecao

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1- Atributo de dado Velocidade
2- Método acelerar, que deverá incrementar a velocidade da unidade em 1
3- Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1- Valor da direção com valores possíveis: Norte, Sul, Leste, Oeste.
2- Método girar_a_direita
3- Método girar_a_esquerda

    N
O       L
    S

    Exemplo:
    >>> # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> #Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    3
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Sul'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
"""

class Motor():

    def __init__(self, velocidade = 0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

class Direcao:

    direcao = ["Norte", "Leste", "Sul", "Oeste"]
    index = 0

    def __init__(self, valor = "Norte"):
        self.valor = valor

    def girar_a_direita(self):
        self.index += 1
        self.valor = self.direcao[self.index%4]

    def girar_a_esquerda(self):
        self.index -= 1
        self.valor = self.direcao[self.index%4]

class Carro():

    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()