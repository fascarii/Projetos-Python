# crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

#informa ao úsuario o que o programa faz
print("Vamos encontrar os números pares no intervalo de 1 a 50.")
print(50 * "=")
# o comando for 'procura' pelos número pares no intervalo definido, a seguir exibe o resultado na tela
for par in range(2, 50, 2)
    if par % 2 == 0:
        print(par)
print(50 * "=")
print("\nFim")
