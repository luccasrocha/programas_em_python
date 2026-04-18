import random


def jogar():
    print('*********************************')
    print('Bem-vindo ao jogo de adivinhação!')
    print('*********************************')

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    try:
        nivel = int(input('Defina o nível: '))
    except ValueError:
        print('Entrada inválida. Digite apenas números.')
        return

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    elif nivel == 3:
        total_tentativas = 5
    else:
        print('Nível inválido')
        return

    for rodada in range(1, total_tentativas + 1):
        print(f'\nTentativa {rodada} de {total_tentativas}')
        try:
            chute = int(input('Digite um número entre 1 e 100: '))
        except ValueError:
            print('Por favor, digite apenas números inteiros.')
            continue

        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100.')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f'\nParabéns! Você acertou e fez {pontos} pontos!')
            break
        else:
            if maior:
                print('O número secreto é menor.')
            elif menor:
                print('O número secreto é maior.')

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print(f'\nO número secreto era {numero_secreto}.')
    print('Fim do jogo!')


# Executa o jogo
jogar()
