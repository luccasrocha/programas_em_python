# Escolher o que vai acontecer
print('Escolha seu metodo:')
print('1. Adição')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')
print('5. Potencia')

# Escolha do usuario
escolha = input('Escolha entre (1/2/3/4/5): ')

# Variavel
if escolha in ('1', '2', '3', '4', '5'):

    # Entrada de numeros
    numero1 = int(input('Escolha o primeiro numero: '))
    numero2 = int(input('Escolha o segundo numero:'))

# Calculos
    if escolha == '1':
        print(numero1, '+', numero2, '=', numero1 + numero2)
    elif escolha == '2':
        print(numero1, '-', numero2, '=', numero1 - numero2)
    elif escolha == '3':
        print(numero1, '*', numero2, '=', numero1 * numero2)
    if escolha == 0:
        print('Não existe esse numero!!')
    elif escolha == '4':
        print(numero1, '/', numero2, '=', numero1 / numero2)
    elif escolha == '5':
        print(numero1, '**', numero2, '=', numero1 ** numero2)

# Caso alguma anta coloque errado
else:
    print('Vai ser burro, colocou trem que não existe!!!')
