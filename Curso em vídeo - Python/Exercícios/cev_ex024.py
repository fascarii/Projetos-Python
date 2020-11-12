# confirmar primeiro nome

'''cid = str(input('Digite o nome da sua cidade: ')).split()

print(cid[0].upper() == 'SANTO')'''




cidade = input('Digite o nome da sua cidade:\n')

cidade_1 = cidade.upper()
cidade_mai = cidade_1.split()
santo = cidade_mai[0]

print('SANTO' in santo)