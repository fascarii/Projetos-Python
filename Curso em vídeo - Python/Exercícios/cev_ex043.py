# o programa a seguir calcula o imc do usuário

print(
    "Descubra se você está no seu peso ideal de acordo com seu IMC (ÍNDICE DE MASSA CORPORAL)"
)

peso = float(input("Digite o seu peso atual (Kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)

if imc >= 40:
    print("Seu IMC é {:.1f}.\nSua classificação é : Obesidade Mórbida".format(imc))
elif imc >= 30:
    print("Seu IMC é {:.1f}.\nSua classificação é : Obesidade".format(imc))
elif imc >= 25:
    print("Seu IMC é {:.1f}.\nSua classificação é : Sobrepeso".format(imc))
elif imc >= 18.5:
    print("Seu IMC é {:.1f}.\nSua classificação é : Peso ideal".format(imc))
else:
    print("Seu IMC é {:.1f}.\nSua classificação é : Abaixo do peso ideal".format(imc))
