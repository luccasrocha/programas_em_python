import math

while True:
    print('\nEscolha uma das opções abaixo:')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão de números decimais')
    print('5 - Divisão inteira')
    print('6 - Potenciação')
    print('7 - Raiz quadrada')
    print('8 - Raiz cúbica')
    print('9 - Porcentagem')
    print('10 - Sair do programa')

    try:
        esquema = int(input('Digite sua escolha: '))
    except ValueError:
        print('Entrada inválida. Digite um número entre 1 e 10.')
        continue

    if esquema == 10:
        print('Fim do programa.')
        break

    if esquema < 1 or esquema > 10:
        print('Opção inválida. Tente novamente.')
        continue

    if esquema in [1, 2, 3, 5, 6]:
        try:
            a = int(input('Digite o primeiro número: '))
            b = int(input('Digite o segundo número: '))
        except ValueError:
            print('Entrada inválida. Digite apenas números inteiros.')
            continue

        if esquema == 1:
            print(f'Resultado: {a + b}')
        elif esquema == 2:
            print(f'Resultado: {a - b}')
        elif esquema == 3:
            print(f'Resultado: {a * b}')
        elif esquema == 5:
            if b == 0:
                print('Erro: divisão por zero.')
            else:
                print(f'Resultado: {a // b}')
        elif esquema == 6:
            print(f'Resultado: {a ** b}')

    elif esquema == 4:
        try:
            a = float(input('Digite o primeiro número decimal: '))
            b = float(input('Digite o segundo número decimal: '))
        except ValueError:
            print('Entrada inválida. Digite apenas números decimais.')
            continue

        if b == 0:
            print('Erro: divisão por zero.')
        else:
            print(f'Resultado: {a / b}')

    elif esquema == 7:
        try:
            a = float(input('Digite o número que deseja saber a raiz quadrada: '))
        except ValueError:
            print('Entrada inválida.')
            continue

        if a < 0:
            print('Erro: não existe raiz quadrada real de número negativo.')
        else:
            print(f'Resultado: {math.sqrt(a)}')

    elif esquema == 8:
        try:
            a = float(input('Digite o número que deseja saber a raiz cúbica: '))
        except ValueError:
            print('Entrada inválida.')
            continue
        print(f'Resultado: {a ** (1/3)}')

    elif esquema == 9:
        try:
            a = float(input('Digite o valor total: '))
            b = float(input('Digite o percentual: '))
        except ValueError:
            print('Entrada inválida.')
            continue
        print(f'Resultado: {(a * b) / 100}')
