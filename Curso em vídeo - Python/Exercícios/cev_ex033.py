# encontrando maior e menor valor dentre três números

print('Vamos encontrar o maior e o menor valor entre três números.')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

menor = n1
if n2 < n1 and n2 < n3:
	menor = n2
if n3 < n2 and n3 < n1:
	menor = n3
print('+ '*25)

maior = n1
if n2 > n1 and n2 > n3:
	maior = n2
if n3 > n1 and n3 > n2:
	maior = n3

print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))

# solução do professor. considerar uso de elif, caso reveja este exercício
	