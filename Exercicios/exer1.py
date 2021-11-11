# # Lista de exercicios contidas no site: https://wiki.python.org.br/ListaDeExercicios
# Coloquei tudo como comentario, caso for executar um programa é só tirar o comentário.
# # 1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
# print("Hello World")
#
# # 2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
# numero = int(input("Escolha um número qualquer: "))
# print(f"O número informado foi: {numero}")
#
# # 3 - Faça um Programa que peça dois números e imprima a soma.
# numero1 = int(input("Escolha um número para somar: "))
# numero2 = int(input("Escolha outro número para somar: "))
# print(numero1+numero2)
#
# # 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# q1 = int(input("Qual foi a sua nota no primeiro bimestre? "))
# q2 = int(input("Qual foi a sua nota no segundo bimestre? "))
# q3 = int(input("Qual foi a sua nota no terceiro bimestre? "))
# q4 = int(input("Qual foi a sua nota no quarto bimestre? "))
# media = (q1+q2+q3+q4)/4
# print(media)
#
# # 5 - Faça um Programa que converta metros para centímetros.
# metros = int(input("Quantos metros deseja converter?"))
# print(metros/100)
#
# # 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# raio = int(input("Qual o raio do circulo que deseja calcular?"))
# pi = 3.14
# print(pi*(raio**2))
#
# # 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# lado = int(input("Qual o lado que deseja calcular?"))
# print(f"A área do quadrado é: {lado*lado} ")
# print(f"O drobro da área é: {2*lado*lado}")
#
# # 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# # Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# # comprar apenas latas de 18 litros;
# # comprar apenas galões de 3,6 litros;
# # misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
#
# area = int(input("Qual a área a ser pintada?"))
# uso_de_tinta = area*1.1/6
# latas = int(uso_de_tinta/18) + 1
# galoes = int(uso_de_tinta/3.6) + 1
# print(f"Caso compre apenas latas de 18 litros o consumo será: {latas} que custará {latas*80}R$")
# print(f"Caso compre apenas galoes de 3,6 lietros o consumo será: {galoes} que custará {galoes*25}R$")
# total = 0
# total_de_galoes = 0
# total_de_latas = 0
# while total <= uso_de_tinta:
#     if (total + 18) < uso_de_tinta:
#         total += 18
#         total_de_galoes += 1
#     else:
#         total += 3.6
#         total_de_latas += 1
#
# custo_total = total_de_galoes*80 + total_de_latas*25
# print(f"Para menor desperdício, pode-se utilizar, {total_de_galoes} de galoes e {total_de_latas} de latas, totalizando {custo_total}R$")
#
#
# # Estrutura de decisão:
# # 5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# # A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# # A mensagem "Reprovado", se a média for menor do que sete;
# # A mensagem "Aprovado com Distinção", se a média for igual a dez.
#
# nota_1 = float(input("Digite a primeira nota: "))
# nota_2 = float(input("Digite a segunda nota: "))
# media = (nota_1 + nota_2)/2
# if media == 10:
#     print("Aprovado com Distinção")
# elif media >= 7:
#     print("Aprovado")
# elif media < 7:
#     print("Reprovado")
# else:
#     print("Não parece algo valido")
#
#
# # 21 -
#
#
# saque = 299
#
# notas_de_100 = notas_de_50 = notas_de_10 = notas_de_5 = notas_de_1 = 0
#
# notas_de_100, saque = divmod(saque, 100)
#
# notas_de_50, saque = divmod(saque, 50)
#
# notas_de_10, saque = divmod(saque, 10)
#
# notas_de_5, notas_de_1 = divmod(saque, 5)
#
# if notas_de_100 > 0:
#     print(f'{notas_de_100} nota(s) de 100')
# if notas_de_50 > 0:
#     print(f'{notas_de_50} nota(s) de 50')
# if notas_de_10 > 0:
#     print(f'{notas_de_10} nota(s) de 10')
# if notas_de_5 > 0:
#     print(f'{notas_de_5} nota(s) de 5')
# if notas_de_1 > 0:
#     print(f'{notas_de_1} nota(s) de 1')

# 4 -Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
# escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a
# população do país B, mantidas as taxas de crescimento.

# populacao_a = 80000
# populacao_b = 200000
# crescimento_a = 1 + 3/100
# crescimento_b = 1 + 1.5/100
# anos = 0
#
# while populacao_a <= populacao_b:
#     populacao_a *= crescimento_a
#     populacao_b *= crescimento_b
#     anos += 1
#
# print(anos)

# # 7 - Faça um programa que leia 5 números e informe o maior número.
# maximo = float(input('Digite um número: '))
# soma = [maximo,]
# for _ in range(4):
#     num = float(input('Digite um número: '))
#     maximo = max(maximo, num)
#     print(f'Número máximo encontrado até agora é: {maximo}')
#     soma.append(num)
# print(sum(soma)/len(soma))

# # Método 2
# soma = float(input('Digite um número: '))
# for n in range(2,6):
#     soma += float(input('Digite um número: '))
#     media = soma / n
#     print(f'A soma dos número é {soma}, e a média é {media}')
#

# 2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
#
# lst = []
#
# for _ in range(10):
#     numero = float(input("Digite um número: "))
#     lst.append(numero)
# print(lst[::-1])

# 15 - Faça um programa que leia um número indeterminado de valores,
# correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

#
# notas = []
#
# while True:
#     entrada = input('Digite um número: ')
#     if entrada == '-1':
#         break
#     notas.append(float(entrada))
#
#
# tamanho = len(notas)
# print(f"Foram lidas {tamanho} notas")
# print(' '.join([str(nota) for nota in notas]))
# notas.reverse
# print('\n'.join([str(nota) for nota in notas]))
#
# soma = sum(notas)
# print(f'Soma das notas é: {soma}')
# media = soma/tamanho
# print(f'A média das notas é: {media}')
#
# print("Notas acima da média: ")
# print(' '.join([str(nota) for nota in notas if nota > media]))
# print("Notas abaixo de 7: ")
# print(' '.join([str(nota) for nota in notas if nota < 7]))
#
# print("Encerrado programa de estatística de notas")


# 16 -
#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante

# salarios = [200, 250, 320, 413, 516, 680, 791, 877, 999, 1000, 2000, 3000]
# contagem_de_faixa_salarial = [0] * 9
# for salario in salarios:
#     indice = (salario // 100) - 2
#     indice_maximo = len(contagem_de_faixa_salarial) - 1
#     indice = min(indice, indice_maximo)
#     contagem_de_faixa_salarial[indice] += 1
#
# print(contagem_de_faixa_salarial)

# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

# def imprimir_triangulo_de_numeros(n: int):
#     for i in range(1, n+1):
#         for _ in range(i):
#             print(i, end = '   ')
#         print('')
#
#
# print("Triangulo com 1")
# imprimir_triangulo_de_numeros(1)
# print("Triangulo com 2")
# imprimir_triangulo_de_numeros(2)
# print("Triangulo com 3")
# imprimir_triangulo_de_numeros(3)

#Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
#
# def imprimir_triangulo_de_numeros(n: int):
#     for i in range(1, n+1):
#         n = 1
#         for _ in range(i):
#             print(n, end = '   ')
#             n+=1
#         print('')
#
#
# print("Triangulo com 1")
# imprimir_triangulo_de_numeros(1)
# print("Triangulo com 2")
# imprimir_triangulo_de_numeros(2)
# print("Triangulo com 3")
# imprimir_triangulo_de_numeros(20)


#
#Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

# #Maneira do professor
# def imprimir_triangulo_de_numeros(n: int):
#     for linha in range(1, n+1):
#         for coluna in range(1,linha+1):
#             print(coluna, end = '   ')
#         print('')
#
#
# print("Triangulo com 1")
# imprimir_triangulo_de_numeros(1)
# print("Triangulo com 2")
# imprimir_triangulo_de_numeros(2)
# print("Triangulo com 3")
# imprimir_triangulo_de_numeros(20)
#


# 1 - Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
#
# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

# s1 = input("DIgite uma string ")
# s2 = input("DIgite outras string ")
#
# tamanho1 = len(s1)
# tamanho2 = len(s2)
#
# print(f'"{s1}" : {tamanho1} caracteres')
# print(f'"{s2}" : {tamanho2} caracteres')
# comparacao_de_tamanho = 'diferentes'
# comparacao_de_conteudo = 'diferentes'
#
# if s1 == s2:
#     comparacao_de_tamanho = 'iguais'
#     comparacao_de_conteudo = 'igual'
# elif tamanho1 == tamanho2:
#     comparacao_de_tamanho = 'iguais'
#
#
# print(f'As duas strings são de tamanhos {comparacao_de_tamanho}')
# print(f'As duas strings possuem conteúdo {comparacao_de_conteudo}')

# 2 - Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome
# e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

# s1 = input("Digite uma string ")
# print(s1[::-1].upper())

#Resolucao professor

# nome = "Luiz Otavio Ibrahim".upper()
#
# nome_invertido_por_letras = ''.join(reversed(nome))
#
# nome_invertido_por_palavras = ' '.join(reversed(nome.split()))
#
# print(f'Nome com letras em maiúsculo: {nome}')
# print(f'Nome com letras em maiúsculo invertido por letras: {nome_invertido_por_letras}')
# print(f'Nome com letras em maiúsculo invertido por palavras: {nome_invertido_por_palavras}')

# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
#
# F
# U
# L
# A
# N
# O


# s1 = input("Digite uma string ")
# counter = 0
# for i in s1:
#     print(s1[:counter])
#     counter += 1
# print(s1[::])



# s1 = input("Digite uma string ")
# while s1 != '':
#     print(s1)
#     s1 = s1[:-1]
# 11 - Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
#
# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!
#
# Digite uma letra: O
# A palavra é: _ _ _ _ O
#
# Digite uma letra: E
# A palavra é: _ E _ _ O
#
# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

# palavra = "DevPro".upper()
#
# print("Jogo da Forca")
# print("Descubra a palavra")
#
# numero_de__= ["_" for letra in palavra]
# print(numero_de__)
# print(f"A palavra é {' '.join(numero_de__)}")
# counter = 0
# print(palavra.split())

# palavra = "DevPro".upper()
#
# print("Jogo da Forca")
# print("Descubra a palavra")
# print('A Palavra é: ', end='')
# for letra in palavra:
#     print('_ ', end='')
#
# conjunto_letras_palavra = set(palavra)
# conjunto_letras_digitadas = set()
# erros = 0
#
# while not conjunto_letras_palavra.issubset(conjunto_letras_digitadas) and erros < 7:
#     print()
#     print()
#     letra_digitada = input('Digite uma letra: ').upper()
#     conjunto_letras_digitadas.add(letra_digitada)
#     if letra_digitada in conjunto_letras_palavra:
#         print('A Palavra é: ', end='')
#         for letra in palavra:
#             if letra in conjunto_letras_digitadas:
#                 print(f'{letra} ', end='')
#             else:
#                 print('_ ', end='')
#     else:
#         erros += 1
#         print(f'--> Erro {erros} de 6. Tente de novo!')
#
#     print()
#     print('Letras já digitadas: ', conjunto_letras_digitadas)
#
# if erros < 7:
#     print("Parabéns, você ganhou!")
# else:
#     print("Infelizmente, você perdeu")


# Contagem de caracteres com uma lista

# def contar_caracteres(s):
#     """
#     >>> contar_caracteres('Luiz')
#     i: 1
#     l: 1
#     u: 1
#     z: 1
#     >>> contar_caracteres("banana")
#     a: 3
#     b: 1
#     n: 2
#     :param s: String a ser contada
#     """
#     caracteres_ordenados = sorted(s)
#
#     caracter_anterior = caracteres_ordenados[0]
#     contagem = 1
#
#     for caracter in caracteres_ordenados[1:]:
#         if caracter == caracter_anterior:
#             contagem += 1
#         else:
#             print(f'{caracter_anterior}: {contagem}')
#             caracter_anterior = caracter
#             contagem = 1
#     print(f'{caracter_anterior}: {contagem}')
#
# if __name__ == '__main__':
#     contar_caracteres('luiz')
#     print()
#     contar_caracteres('banana')


#Contagem com um dicionario
# def contar_caracteres(s):
#     """
#     >>> contar_caracteres('Luiz')
#     {'i': 1, 'l': 1, 'u': 1, 'z': 1}
#     >>> contar_caracteres("banana")
#     {'a': 3, 'b': 1, 'n': 2,}
#     :param s: String a ser contada
#     """
#
#     caracteres_ordenados = sorted(s)
#
#     caracter_anterior = caracteres_ordenados[0]
#     contagem = 1
#
#     resultado = {}
#
#     for caracter in caracteres_ordenados[1:]:
#         if caracter == caracter_anterior:
#             contagem += 1
#         else:
#             resultado[caracter_anterior] = contagem
#             caracter_anterior = caracter
#             contagem = 1
#     resultado[caracter_anterior] = contagem
#
#     return resultado
#
# if __name__ == '__main__':
#     print(contar_caracteres('luiz'))
#     print()
#     print(contar_caracteres('banana'))
#
#
# def contar_caracteres(s):
#     """
#     >>> contar_caracteres('Luiz')
#     {'i': 1, 'l': 1, 'u': 1, 'z': 1}
#     >>> contar_caracteres("banana")
#     {'a': 3, 'b': 1, 'n': 2,}
#     :param s: String a ser contada
#     """
#     resultado = {}
#
#     for caracter in s:
#         resultado[caracter] = resultado.get(caracter, 0) + 1
#
#     return resultado
#
# if __name__ == '__main__':
#     print(contar_caracteres('luiz'))
#     print()
#     print(contar_caracteres('banana'))


# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256

# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
#
# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256
#
# def validar(ip:str) -> bool:
#     numeros = ip.split('.')
#
#     if len(numeros) != 4:
#         return False
#
#     for n in numeros:
#         if not (0 <= int(n) <= 255):
#             return False
#     return True
#
# ips_validos = []
# ips_invalidos = []
#
# with open('sample_data/ips.txt', 'r') as arquivo:
#     for linha in arquivo:
#         ip = linha.strip()
#         if validar(ip):
#             ips_validos.append(ip)
#         else:
#             ips_invalidos.append(ip)
#
# with open('sample_data/ips_saida.txt', 'w') as arquivo:
#     arquivo.writelines('[Endereços válidos:]\n')
#
#     for ip in ips_validos:
#         arquivo.writelines(f'{ip}\n')
#
#     arquivo.writelines('\n')
#     arquivo.writelines('\n')
#     arquivo.writelines('[Endereços inválidos:]\n')
#
#     for ip in ips_invalidos:
#         arquivo.writelines(f'{ip}\n')

# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
# e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet,
# ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo,
# você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso
#
# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%
#
# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
# de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco,
# de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal.
# O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
#
# lista_de_dados = []
#
# def transformar_em_megabytes(tamanho_em_bytes:str) -> float:
#     return int(tamanho_em_bytes)/(2**10) **2
#
# with open('sample_data/usuarios.txt', 'r') as arquivo:
#     for linha in arquivo:
#         linha = linha.strip()
#         usuario = linha[:15]
#         tamanho_em_disco = transformar_em_megabytes(linha[16:])
#         lista_de_dados.append((usuario,tamanho_em_disco))
#
# cabecalho = """ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso
# """
#
#
# with open('sample_data/relatorio.txt', 'w') as arquivo:
#     tamanho_total_consumido = sum([tamanho for _,tamanho in lista_de_dados])
#     media = tamanho_total_consumido/len(lista_de_dados)
#     arquivo.writelines(cabecalho)
#
#     for indice, dados in enumerate(lista_de_dados, start=1):
#         usuario, tamanho_em_disco = dados
#         arquivo.writelines(
#             f'{indice:<4} {usuario} {tamanho_em_disco:9.2f} MB         '
#             f'{tamanho_em_disco/tamanho_total_consumido:>6.2%}\n'
#         )
#
#     arquivo.writelines('\n')
#     arquivo.writelines(f'Espaço total ocupado: {tamanho_total_consumido:.2f} MB\n')
#     arquivo.writelines(f'Espaço; médio; ocupado: {media:.2f} MB')

#Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

# class Bola():
#
#     def __init__(self, cor, circunferencia, material):
#         self.cor = cor
#         self.circunferencia = circunferencia
#         self.materia = material
#
#     def troca_cor(self, cor):
#         self.cor = cor
#
#     def mostrar_cor(self):
#         return self.cor
#
# bola1 = Bola("Azul", 30, "Borracha")
# print(bola1.mostrar_cor())
# bola1.troca_cor("Vermelho")
# print(bola1.mostrar_cor())


# 2 - Classe Quadrado: Crie uma classe que modele um quadrado:
#
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

# class Quadrado():
#
#     def __init__(self, lado = 1):
#         self.lado = lado
#
#     def calcular_area(self):
#         return self.lado **2
#
#
# quadrado = Quadrado(5)
# print(quadrado.lado, quadrado.calcular_area())

# 4 - Classe Pessoa: Crie uma classe que modele uma pessoa:
#
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão,
# a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

# class Pessoa():
#
#     def __init__(self, nome, idade, peso, altura):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.altura = altura
#
#     def envelhecer(self):
#         if self.idade < 21:
#             self.altura += 0.5
#         self.idade +=1
#
#     def engordar(self, aumento):
#         self.peso += aumento
#         return self.peso
#
#     def emagrecer(self, perda):
#         self.peso -= perda
#         return self.peso
#
#     def crescer(self, cresceu):
#         self.altura += cresceu
#         return self.altura
#
#
#
# otavio = Pessoa('Otavio', 2, 12, 80)
#
# for _ in range(22):
#     otavio.envelhecer()
#     print(f'Idade de {otavio.nome} é: {otavio.idade} anos. E a sua altura e {otavio.altura} cm')
#
# print(otavio.engordar(5))
# print(otavio.emagrecer(3))
# print(otavio.crescer(10))

# Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
#
# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# tipoCombustivel.
# valorLitro
# quantidadeCombustivel
# Possua no mínimo esses métodos:
# abastecerPorValor( ) – método onde é informado o valor
# a ser abastecido e mostra a quantidade de litros que foi colocada no veículo

# abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e
# mostra o valor a ser pago pelo cliente.

# alterarValor( ) – altera o valor do litro do combustível.
# alterarCombustivel( ) – altera o tipo do combustível.
# alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

# class BombaCombustivel():
#
#     def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
#         self.tipo_combustivel = tipo_combustivel
#         self.valor_litro = valor_litro
#         self.quantidade_combustivel = quantidade_combustivel
#
#     def abastecer_por_valor(self, valor):
#         litros_abastecidos = valor / self.valor_litro
#         self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)
#
#     def abastercer_por_litro(self, litros_abastecidos):
#         valor = litros_abastecidos * self.valor_litro
#         self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)
#
#     def _apresentar_abastecimento_se_possivel(self, litros_abastecidos, valor):
#         if litros_abastecidos > self.quantidade_combustivel:
#             print(f'Não é possivel abastecer, faltam {litros_abastecidos - self.quantidade_combustivel} litros')
#             print("Abasteça a bomba")
#         else:
#             self.quantidade_combustivel -= litros_abastecidos
#             print(f'Foram abastecidos {litros_abastecidos:.2f} litros, a um valor de R$ {valor:.2f}')
#             print(f'Sobraram na bomba {self.quantidade_combustivel:.2f} litros')
#
#     def alterar_valor(self, valor):
#         self.valor_litro = valor
#         return self.valor_litro
#
#     def alterar_combustivel(self, combustivel):
#         self.tipo_combustivel = combustivel
#         return self.tipo_combustivel
#
#     def alterar_quantidade_combustivel(self, quantidade):
#         if quantidade >= 0:
#             self.quantidade_combustivel += quantidade
#         else:
#             print("Não pode")
#
#
# bomba_combustivel = BombaCombustivel("gasolina", 5, 100)
# bomba_combustivel.abastecer_por_valor(20)
# bomba_combustivel.quantidade_combustivel
# bomba_combustivel.abastercer_por_litro(50)
# bomba_combustivel.quantidade_combustivel
# bomba_combustivel.alterar_valor(5.5)
# bomba_combustivel.abastercer_por_litro(50)
# bomba_combustivel.alterar_quantidade_combustivel(100)
# bomba_combustivel.abastercer_por_litro(50)
# bomba_combustivel.alterar_quantidade_combustivel(-100)

# Projetos
# 1. Controle de cotas de disco. A ACME Inc., uma organização com mais de 1500 funcionários,
# está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema,
# o Administrador de Rede precisa saber qual o espaço em disco ocupado pelas contas dos usuários, e identificar os usuários
# com maior espaço ocupado. Através de um aplicativo baixado da Internet, ele conseguiu gerar o seguinte arquivo,
# chamado usuarios.txt:
#
#
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o primeiro campo corresponde ao login do usuário e o segundo ao espaço em disco ocupado pelo seu diretório home. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado relatório.txt, no seguinte formato:
#
#
# ACME Inc.           Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso
#
# 1    alexandre       434,99 MB            16,85%
# 2    anderson       1187,99 MB            46,02%
# 3    antonio         117,73 MB             4,56%
# 4    carlos           87,03 MB             3,37%
# 5    cesar             0,94 MB             0,04%
# 6    rosemary        752,88 MB            29,16%
#
# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória,
# caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco,
# de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal.
# O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
# Recursos adicionais: opcionalmente, desenvolva as seguintes funcionalidades:
#
# Ordenar os usuários pelo percentual de espaço ocupado;
# Mostrar apenas os n primeiros em uso, definido pelo usuário;
#
# Gerar a saída numa página html;
# Criar o programa que lê as pastas e gera o arquivo inicial;



lista_de_dados = []

def transformar_em_megabytes(tamanho_em_bytes:str) -> float:
    return int(tamanho_em_bytes)/(2**10) **2

with open('sample_data/usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_em_disco = transformar_em_megabytes(linha[16:])
        lista_de_dados.append((tamanho_em_disco, usuario))

cabecalho = """ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
"""

n = int(input('Digite o numero de usuários a serem exibidos: '))
lista_de_dados.sort(reverse=True)
lista_de_dados = lista_de_dados[:n]

with open('sample_data/relatorio.txt', 'w') as arquivo:
    tamanho_total_consumido = sum([tamanho for tamanho, _ in lista_de_dados])
    media = tamanho_total_consumido/len(lista_de_dados)
    arquivo.writelines(cabecalho)

    for indice, dados in enumerate(lista_de_dados, start=1):
        tamanho_em_disco, usuario  = dados
        arquivo.writelines(
            f'{indice:<4} {usuario} {tamanho_em_disco:9.2f} MB         '
            f'{tamanho_em_disco/tamanho_total_consumido:>6.2%}\n'
        )

    arquivo.writelines('\n')
    arquivo.writelines(f'Espaço total ocupado: {tamanho_total_consumido:.2f} MB\n')
    arquivo.writelines(f'Espaço; médio; ocupado: {media:.2f} MB')

