c = float(input('Insira a temperatura em C°: '))
f = 1.8 * c + 32
print('{} C° equibale a {} F°'.format(c,f))

F = float(input('Insira a temperatura em F°: '))
C = ((F - 32) * 5) / 9
print('{} F° equivale a {} C°'.format(F,C))