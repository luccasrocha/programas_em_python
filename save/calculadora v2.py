import math

# Perguntas

print('Escolha umas das opções abaixo:')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão de numeros decimais')
print('5 - Divisão inteira')
print('6 - Potênciação')
print('7 - Raiz quadrada')
print('8 - Raiz cúbica')
print('9 - Porcentagem')
print('10 - Sair do programa')

# Esquema de contas

esquema = int(input('Digite sua escolha: '))
if esquema < 1 or esquema > 10:
    print('Opção inválida. Tente novamente.')

elif esquema == 1:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(f'O resultado da adição entre {a} e {b} é: {a + b}')

elif esquema == 2:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(f'Resultado da subtração entre {a} e {b} é: {a - b}')

elif esquema == 3:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(f"Resultado da multiplicação entre {a} e {b} é: {a * b}")

elif esquema == 4:
    a = float(input('Digite o primeiro número decimal: '))
    b = float(input('Digite o segundo número decimal: '))
    def divisao(a, b):
        return a / b
    print(f'Resultado da divisão entre {a} e {b} é: {divisao(a, b)}')

elif esquema == 5:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(f'Resultado da divisão inteira entre {a} e {b} é: {a // b}')

elif esquema == 6:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(f'Resultado da potênciação entre {a} e {b} é: {a ** b}')

elif esquema == 7:
    a = int(input('Digite o número que deseja saber a raiz: '))
    print(f'Resultado: {math.sqrt(a)}')

elif esquema == 8:
    a = int(input('Digite o número que deseja saber a raiz cúbica: '))
    print(f'Resultado: {a ** (1/3)}')

elif esquema == 9:
    a = float(input('Digite o valor total: '))
    b = float(input('Digite o percentual: '))
    def porcentagem(a, b):
        return (a * b) / 100
    print(f'O resultado de {b}% de {a} é: {porcentagem(a, b)}')


elif esquema == 10:
    print('O programa foi acabado aqui.')
exit()
