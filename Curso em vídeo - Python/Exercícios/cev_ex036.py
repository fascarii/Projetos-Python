# aprovando um empréstimo
valor_casa = float(input('Valor do imóvel: R$'))
salario = float(input('Salário: R$'))
tempo = int(input('Em quantos anos deseja pagar? '))*12

parcela = valor_casa / tempo
limite_parc = salario * 30 / 100

if parcela <= limite_parc:
	print('Seu empréstimo foi \033[32mAPROVADO\033[m.')
	print('Serão {} parcelas no valor de R${:.2f}.'.format(tempo,parcela))

else:
	print('Seu empréstimo foi \033[31mNEGADO\033[m.')