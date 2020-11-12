km = float(input('Digite os quilômetros rodados: '))
dias = int(input('Digite a quantidade de dias: '))
total = (km * 0.15)+(dias * 60)
print('Total a pagar: R${:.2f}'.format(total))
