#verificando sobrenome

nome = str(input('Qual é o seu nome?\n')).strip().upper()

sbrnom = ('SILVA' in nome)

print('Existe Silva no seu sobrenome? {}'.format(sbrnom))
