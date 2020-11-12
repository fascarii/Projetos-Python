# separador de dígitos
num = int(input('Número: '))

m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

'''m = num // 1000
c = num % 1000 //100
d = num % 100 // 10
u = num % 10'''

print('O dígito dos milhares é {}'.format(m))
print('O dígito das centenas é {}'.format(c))
print('O dígito das dezenas é {}'.format(d))
print('O dígito das unidades é {}'.format(u))


