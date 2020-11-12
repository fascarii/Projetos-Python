# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# Um palíndromo é uma palavra, frase ou qualquer outra sequência de unidades que tenha
# a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita.

print("{:=^50}".format("DETECTOR DE PALINDROMOS"))

# capta a frase do usuário, removendo os espaçoes do fim e começo
# em seguida converte todas as letras para maiúsculas
frase = str(input("Digite um frase qualquer:\n")).strip().upper()

# reúne as palavras em uma lista
palavras = frase.split()

# junta as palavras da lista criando uma unica string sem espaços
junto = ''.join(palavras)

# variável que receberá o inverso da frase
inverso = ''

# inverte a ordem das letras da variável 'junto'
for letra in range(len(junto) - 1 , -1, -1):
    inverso += junto[letra]

# se a frase formar um palíndromo a messagem abaixo é escrita na tela
if inverso == junto:
    print("A frase digitada forma o palíndromo {: ^3}.".format(inverso))
else:
    print("A frase digitada não forma um palíndromo.")

# método sem usar o for
# inverso = junto[::-1]