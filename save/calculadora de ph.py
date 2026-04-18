ph = int(input('Me de variaveis de ph entre 0 a 14: '))

if 0 <= ph <= 14:

    if ph < 7:
        print('Acido')
    elif ph > 7:
        print('Basico')
    else:
        print('Neutro')
else:
    print('Não existe esse numero nas variaveis de ph, tente novamente!!')
