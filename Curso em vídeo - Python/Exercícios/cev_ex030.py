#par ou ímpar
num = int(input('Digite um número inteiro qualquer: '))

teste = num % 2

if teste == 0:
	print('O número {} é par.'.format(num))
	
else:
	print('O número {} é ímpar.'.format(num))