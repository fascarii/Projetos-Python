def pergunta_idade():
    idadenum = int(input('Idade?'))
    if idadenum >= 18:
        print('Bem-vindo à Heineken!')
    else:
        idadenum < 18
        print('Volte mais tarde :(')
    
    return pergunta_idade
    
pergunta_idade()

confirma = input('Tem certeza?')
conf = int(confirma)
if conf > 18:
    print('continue')
else:
    conf < 18    
    pergunta_idade()
