# faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print("Descubra se o número é PRIMO.\n")

num = int(input("Digite um número inteiro: "))
cont = 0

for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
if cont == 2:
     print("O número {} é um número PRIMO.".format(num))
else:
    print("O número {} é não um número PRIMO.".format(num))
