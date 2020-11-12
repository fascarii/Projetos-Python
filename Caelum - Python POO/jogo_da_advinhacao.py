# jogo da adivinhação

from time import sleep

# cabeçalho do jogo
print(30 * "*")
print("{: ^30}".format("Jogo da adivinhação"))
print(30 * "*", "\n")

# número que deverá ser adivinhado
numero_secreto = 30

# variáveis sobvre a dinâmica do jogo
total_de_tentativas = 3
rodada = 1
pontos = 1000

print("Selecione o nível de dificuldade:")

nivel = int(
    input(
        """
            [ 1 ] Fácil   - 20 tentativas
            [ 2 ] Médio   - 10 tentativas
            [ 3 ] Difícil -  5 tentativas\n\nNÍVEL>> """
    )
)

# variáveis nivel de dificuldade
if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
elif nivel == 3:
    total_de_tentativas = 5


# chute do jogador
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu número: "))
    print("Você digitou: {}\n".format(chute))
    sleep(1)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
        print(30 * "=")
        break
    elif chute != numero_secreto:
        if maior:
            print("Você errou! Seu chute foi MAIOR que o número secreto.\n")
            print(30 * "=")
            dano = chute - numero_secreto
        elif menor:
            print("Você errou! Seu chute foi MENOR que o número secreto.\n")
            print(30 * "=")
            dano = chute - numero_secreto

    rodada += 1
    pontos -= abs(dano)

print("Você fez {} pontos.\n".format(pontos))
print("{: ^30}".format("Fim do Jogo!"))
