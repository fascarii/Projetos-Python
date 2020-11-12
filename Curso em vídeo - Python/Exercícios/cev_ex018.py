from math import radians,sin, cos, tan
ang = int(input('Digite um ângulo: '))
graus = radians(ang)
print('Para o ângulo de {}° temos:\n Seno: {:.2f} \n  Cosseno: {:.2f}\n   Tangente: {:.2f}'.format(ang,sin(graus),cos(graus),tan(graus)))