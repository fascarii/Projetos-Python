# faça um programa que mostre na tela uma contagem regressiva para fogos de artifício,
# indo de 10 até 0, com um pausa de  1 segundo entre eles

from time import sleep

print("CONTAGEM REGRESSIVA!!")

for segundo in range(10, 0, -1):
    print(segundo)
    sleep(1)
print("{:=^30}".format("FELIZ ANO NOVO!!"))