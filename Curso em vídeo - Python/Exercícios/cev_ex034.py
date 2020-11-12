# calcular aumentos diferentes de salario para valores diferentes

sal_atual = float(input('Digite o salário atual:\nR$'))

if sal_atual > 1250:
	print('Com o aumento de 10% seu salário será R${:.2f}'.format((sal_atual * 110) / 100))
else:
	sal_atual <= 1250
	print('Com o aumento de 15% seu salário será R${:.2f}'.format((sal_atual * 115) / 100))