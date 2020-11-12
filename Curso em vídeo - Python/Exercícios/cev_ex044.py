# condições de pagamento

print("{:=^30}".format("LOJAS GUARULHOS"))

preco = float(input("Valor da compra: R$ "))
print("""FORMAS DE PAGAMENTO
[ 1 ] Pagamento à vista dinheiro / cheque
[ 2 ] Pagamento à vista no cartão
[ 3 ] Pagamento em 2X no cartão de crédito
[ 4 ] Pagamento em 3x ou mais no cartão de crédito""")

print(30 * "=")

opcao = int(input("Digite a opção de pagamento: "))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f}, sem juros.".format(
        parcela))
elif opcao == 4:
    total = preco * 120 / 100
    totparc = int(input("Em quantas parcelas? "))
    parcela = total / totparc
    print("Sua compra será parcelada em {}x de R${:.2f}, com juros.".format(
        totparc, parcela))
else:
    total = preco
    print("OPÇÃO DE PAGAMENTO INVÁLIDA. tENTE NOVAMENTE.")
print("Total da sua compra : R${:.2f}".format(total))

