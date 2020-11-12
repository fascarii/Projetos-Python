nome = input('Digite seu nome completo:\n')

nome_sep = nome.split()

print(nome.upper())
print(nome.strip())
print('Seu nome completo possui {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primerio nome possui {} letras.'.format(len(nome_sep[0])))
