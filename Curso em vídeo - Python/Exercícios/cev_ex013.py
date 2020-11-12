slr_atual = float(input('Insira o salário atual: R$'))
vlr_aumento = (slr_atual*15)/100
slr_aumento = slr_atual + vlr_aumento
print('Seu novo salário, com aumento de 15% ou R${:.2f}, será R${:.2f}'.format(vlr_aumento,slr_aumento))