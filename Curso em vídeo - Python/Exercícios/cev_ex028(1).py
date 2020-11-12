from random import randrange

num_usuario = int(input('De 1 a 5 em que número o computador está pensando?\n'))

num_comp = randrange(5)
print(num_comp)

if num_comp == num_usuario:
	print('Parabéns!')
else:
	print('Tente outra vez.')