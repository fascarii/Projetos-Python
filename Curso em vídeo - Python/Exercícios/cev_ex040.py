# calculo de média, reprovação, recuperação e aprovação

print('Digite as notas e saiba se o aluno foi aprovado.')

aluno = input('Nome do aluno: ').upper().strip()
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

média = (nota_1 + nota_2) / 2

if média < 5:
    print('A primeira nota é {:.2f} e a segunda é {:.2f}.\nSua nota média é {:.2f}'.format(
        nota_1, nota_2, média))
    print('O aluno {} foi REPROVADO.'.format(aluno))

elif média >= 5.0 and média < 6.9:
    print('Sua primeira nota é {:.2f} e a segunda é {:.2f}.\nSua média é {:.2f}'.format(
        nota_1, nota_2, média))
    print('O aluno {} deve fazer RECUPERAÇÃO.'.format(aluno))

elif média >= 7.0:
    print('Sua primeira nota é {:.2f} e a segunda é {:.2f}.\nSua média é {:.2f}'.format(
        nota_1, nota_2, média))
    print('O aluno {} foi APROVADO.'.format(aluno))
