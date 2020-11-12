# convertendo um número decimal em binário, octal ou hexadecimal
print('Conversor de bases numéricas.\n')

decimal = int(input('Digite um número inteiro: '))
print(
    '''Escolha uma base para conversão:
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL'''
)

opção = int(input('Opção: '))

if opção == 1:
    print('O número DECIMAL {} convertido para BINARIO é {}'.format(decimal, bin(decimal)[2:]))

elif opção == 2:
    print('O número DECIMAL {} convertido para OCTAL é {}'.format(decimal, oct(decimal)[2:]))

elif opção == 3:
    print('O número DECIMAL {} convertido para HEXADECIMAL é {}'.format(decimal, hex(decimal).upper()[2:]))

else:
    print('Opção inválida. Tente novamente.')
    
#exercício resolvido com ajuda. eu estava considerando converter com cálculos