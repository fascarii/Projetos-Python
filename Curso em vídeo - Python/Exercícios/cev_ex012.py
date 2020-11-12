total = float(float("Insira o valor total do produto para conhecer seu desconto:R$ "))
vlr_desconto = (total * 95) / 100

print("Com o desconto de 5% você pagará \033[32mR${:.2f}\033[m".format(vlr_desconto))

