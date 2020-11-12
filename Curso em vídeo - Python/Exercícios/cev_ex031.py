# Desenvolva um programa que:
# Pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distância = float(
    input('Vamos calcular o valor da sua viagem. \nQual a distância da viagem?  ')
)

preço_1 = distância * 0.50
preço_2 = distância * 0.45

if distância <= 200:
    print('Por essa distância você paga apenas R${:.2f}.'.format(preço_1))
else:
    print('Por essa distância você paga apenas R${:.2f}.'.format(preço_2))
