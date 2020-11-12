# alistamento militar
from datetime import datetime

ano_nasc = int(input('Em que ano você nasceu? '))
ano_completo = datetime.now().year
idade = ano_completo - ano_nasc
print()

# if prazo == 0:
#    print(
#        'Você deve se alistar esse ano.Procure a Junta de Serviço Militar mais próxima.'
#    )

# elif prazo == 1:
#    print('Fique atento, você deve se alistar em {} ano'.format(prazo))

# elif prazo > 1:
#    print(
#        'Fique tranquilo. Ainda faltam {} anos para o alistamento militar.'.format(
#            prazo
#        )
#    )

# elif prazo < -1:
#    print(
#        'Atenção! Você deveria ter se listado há {} anos.\nProcure a Junta de Serviço Militar mais próxima e regularize sua situação'.format(
#            abs(prazo)
#        )
#    )

# elif prazo == -1:
#    print(
#        'Atenção! Você deveria ter se alistado há {} ano.\nProcure a Junta de Serviço Militar mais próxima e regularize sua situação'.format(
#            abs(prazo)
#        )
#    )

if idade == 18:
    print(
        'Você deve se alistar esse ano.\nProcure a Junta de Serviço Militar mais próxima.'
    )

elif idade > 18:
    prazo = idade - 18
    if prazo > 1:
        print(
            'Atenção! Você deveria ter se listado há {} anos.\nProcure a Junta de Serviço Militar mais próxima e regularize sua situação'.format(
                (prazo)
            )
        )
    else:
        prazo = 1
        print(
            'Atenção! Você deveria ter se listado há {} ano.\nProcure a Junta de Serviço Militar mais próxima e regularize sua situação'.format(
                (prazo)
            )
        )


elif idade < 18:
    prazo = 18 - idade
    if prazo > 1:
        print(
        'Você deve se alistar em {} anos.\nProcure a Junta de Serviço Militar quando chegar a hora.'.format(
            (prazo)
        )
    )
    else:
        prazo = 1
        print(
        'Você deve se alistar em {} ano.\nProcure a Junta de Serviço Militar quando chegar a hora.'.format(
            (prazo)
        )
    )