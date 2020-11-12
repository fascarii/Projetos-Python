# analisando maior número

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 > num2:
    print('O primeiro número é o maior.')
elif num2 > num1:
    print('O segundo numero é o maior.')
else:
    print('Os dois números são iguais.')