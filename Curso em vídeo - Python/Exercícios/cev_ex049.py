# usando método comando for
# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada

fator1 = int(input("Digite um número para saber sua tabuada: "))
for fator2 in range(1, 11):
    res = fator1 * fator2
    print("{} x {:2} = {}".format(fator1, fator2, res))
