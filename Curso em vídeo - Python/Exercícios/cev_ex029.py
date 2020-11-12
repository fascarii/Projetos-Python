vel = int(input('Velocidade: '))

if vel >= 80:
	print('VOCÊ FOI MULTADO.\nVELOCIDADE ACIMA DO LIMITE PERMITIDO DE 80 km/h.\nA VELOCIDADE REGISTRADA FOI {}km/h.'.format(vel))
	print('O VALOR DA MULTA É DE R$ {:.2f}.'.format((vel - 80)*7))

else:
	print('CONTINUE DIRIGINDO COM SEGURANÇA. BOA VIAGEM.')