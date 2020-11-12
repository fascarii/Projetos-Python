#sorteando um aluno
from random import sample
a1 = input('aluno 1: ')
a2 = input('aluno 2: ')
a3 = input('aluno 3: ')
a4 = input('aluno 4: ')
alunos = sample([a1,a2,a3,a4],k = 4)
print('\nO aluno escolhido para apagar a lousa hoje é: {}'.format(alunos))
