# o programa a seguir é uma simulação do jogo JoKenPo (Pedra Papel Tesoura)
from random import randrange
from time import sleep

print("\nQuero ver você me vencer no JoKenPo!\n")
print("{:=^40}".format("ESCOLHA SUA ARMA!"))

print('''
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

jog = int(input("DIGITE O NÚMERO DA SUA ARMA: \n"))
comp = randrange(1, 3)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("POOO!!")

print("O COMPUTADOR ESCOLHE A OPÇÃO {}".format(comp))

# computador jogou PEDRA
if comp == 1:
    if jog == 1:
        print("EMPATE!")
    elif jog == 2:
        print(" VOCÊ VENCEU?! IMPOSSÍVEL!")
    elif jog == 3:
        print("EU VENCI! HUMANO FRACO!")

# computador jogou PAPEL
elif comp == 2:
    if jog == 1:
        print("HAHA! EU VENCI!")
    elif jog == 2:
        print("EMPATE! VOCÊ ESTÁ MELHORANDO...")
    elif jog == 3:
        print("VOCÊ VENCEU! EU O SUBESTIMEI...")

# computador jogou TESOURA
elif comp == 3:
    if jog == 1:
        print("VOCÊ NÃO TEM CHANCES!")
    elif jog == 2:
        print("ADMITO, VOCÊ É BOM!")
    elif jog == 3:
        print("EMPATE!")
    