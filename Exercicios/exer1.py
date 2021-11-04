# Lista de exercicios contidas no site: https://wiki.python.org.br/ListaDeExercicios

# 1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Hello World")

# 2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = int(input("Escolha um número qualquer: "))
print(f"O número informado foi: {numero}")

# 3 - Faça um Programa que peça dois números e imprima a soma.
numero1 = int(input("Escolha um número para somar: "))
numero2 = int(input("Escolha outro número para somar: "))
print(numero1+numero2)

# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
q1 = int(input("Qual foi a sua nota no primeiro bimestre? "))
q2 = int(input("Qual foi a sua nota no segundo bimestre? "))
q3 = int(input("Qual foi a sua nota no terceiro bimestre? "))
q4 = int(input("Qual foi a sua nota no quarto bimestre? "))
media = (q1+q2+q3+q4)/4
print(media)

# 5 - Faça um Programa que converta metros para centímetros.
metros = int(input("Quantos metros deseja converter?"))
print(metros/100)

# 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = int(input("Qual o raio do circulo que deseja calcular?"))
pi = 3.14
print(pi*(raio**2))

# 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = int(input("Qual o lado que deseja calcular?"))
print(f"A área do quadrado é: {lado*lado} ")
print(f"O drobro da área é: {2*lado*lado}")

# 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = int(input("Qual a área a ser pintada?"))
uso_de_tinta = area*1.1/6
latas = int(uso_de_tinta/18) + 1
galoes = int(uso_de_tinta/3.6) + 1
print(f"Caso compre apenas latas de 18 litros o consumo será: {latas} que custará {latas*80}R$")
print(f"Caso compre apenas galoes de 3,6 lietros o consumo será: {galoes} que custará {galoes*25}R$")
total = 0
total_de_galoes = 0
total_de_latas = 0
while total <= uso_de_tinta:
    if (total + 18) < uso_de_tinta:
        total += 18
        total_de_galoes += 1
    else:
        total += 3.6
        total_de_latas += 1

custo_total = total_de_galoes*80 + total_de_latas*25
print(f"Para menor desperdício, pode-se utilizar, {total_de_galoes} de galoes e {total_de_latas} de latas, totalizando {custo_total}R$")


# Estrutura de decisão:
# 5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_1 = int(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
media = (nota_1 + nota_2)/2
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
else:
    print("Não parece algo valido")