#conversor de moeda
cart = float(input('Quantos Reais você possui? '))
preco_dolar = 4.09
qtde_dolar = cart/preco_dolar
print('Com R${:.2f} você consegue comprar US${:.2f}.'.format(cart,qtde_dolar))
