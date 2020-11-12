# descobrindo se um ano é bissexto

from calendar import isleap

print("Descubra se o ano é bissexto ou não.")

ano = int(input("Ano: "))

if isleap(ano) == True:
    print("O ano {} é um ano bissexto.".format(ano))

else:
    print("O ano {} não é um ano bissexto.".format(ano))

