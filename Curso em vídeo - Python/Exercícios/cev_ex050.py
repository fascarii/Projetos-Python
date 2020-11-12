# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    c  = int(input("Digite um número inteiro: "))
    if c % 2 == 0:
        soma += c
        cont += 1
if c % 2 != 0 == 2:
    print("Você não digitou nenhum número par.")
else:
    print("A soma dos {} números pares digitados é: {:2}.\n".format(cont, soma))
