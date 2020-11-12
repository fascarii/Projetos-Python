#classificando atletas por idade
from datetime import datetime
nasc = int(input('Insira o ano de nascimento do atleta: '))

idade = datetime.now().year - nasc

print(idade)

if idade <= 9:
	print('O atleta está na categoria: Mirim')
elif idade > 9 and idade <= 14:
	print('O atleta está na categoria: Infantil')
elif idade > 14 and idade <= 19:
	print('O atleta está na categoria: Juvenil')
elif idade > 19 and idade <= 25:
	print('O atleta está na categoria: Sênior')
elif idade > 25:
	print('O atleta está na categoria: Master')