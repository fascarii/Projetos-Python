#  Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500

#declara a variável que receberá o acumulador da soma dos ímpares múltiplos de 3
soma = 0
#declara a variável que receberá o contador dos ímpares múltiplos de 3
cont = 0

# o comando for "procura" pelos múltiplos, e os soma em seguida
for num in range(1, 501, 2):
    if num % 3 == 0:
# a variável 'soma' acumula os números ímpares, somando todos eles
        soma += num
# a variável 'cont' justamente conta quantas vezes os números ímpares ocorrem no intervalo definido
        cont += 1
print("O resultado das soma de todos os {} valores no intervalo de 1 a 500 é: {}".format(cont, soma))
