# destacando o primeiro e o último nome

nome = str(input("Digite o seu nome completo: ")).strip().split()
print("Olá! Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu último nome é {}".format(nome[-1]))

