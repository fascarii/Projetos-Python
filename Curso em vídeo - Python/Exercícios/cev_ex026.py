# contando número de aparições de uma letra sem acento

# não consegui fazer sozinho

texto = str(input('Digite seu texto:\n')).strip().lower()

#conta quantas vezes a letra aparece
contagem_a = texto.count('a')

#localiza a posição a partir do começo da frase, depois pelo fim
prim_a = (texto.find('a')+1)
ult_a = (texto.rfind('a')+1)

# mensagens são impressas conforme os resultados acima

# se a letra aparece uma vez
if contagem_a == 1:
	print("No texto digitado a letra 'a' aparece {} vez.".format(contagem_a))

# se a letra não aparece
elif contagem_a == 0:
	print('A letra "a" não aparece no texto digitado.')

#se a letra aparece mais de uma vez
else:
	contagem_a > 1
	print("No texto digitado a letra 'a' aparece {} vezes.".format(contagem_a))

# informa as posições das letras
print("A primeira vez na posição {}.".format(prim_a))
print("A última vez na posição {}.".format(ult_a))