import itertools
import time
import sys

caracteres = input("Digite os caracteres que quer usar (ex: abc123): ")
tamanho_min = int(input("Tamanho mínimo da palavra: "))
tamanho_max = int(input("Tamanho máximo da palavra: "))
nome_arquivo = input("Nome do arquivo para salvar a wordlist: ")

with open(nome_arquivo, "w") as f:
    for tamanho in range(tamanho_min, tamanho_max + 1):
        for combinacao in itertools.product(caracteres, repeat=tamanho):
            palavra = ''.join(combinacao)
            f.write(palavra + "\n") #fomart

print(f"Wordlist criada com sucesso! Salva em {nome_arquivo}") #mensagem para salvar o arquivo
emoji = input("Escolha um emoji para a barra de progresso (ex: *): ") #escolha do emogi para o carregamento da mensagem 
total = sum((len(caracteres) ** i) for i in range(tamanho_min, tamanho_max + 1))
contador = 0

with open(nome_arquivo, "w") as f:
    for tamanho in range(tamanho_min, tamanho_max + 1):
        for combinacao in itertools.product(caracteres, repeat=tamanho):
            palavra = ''.join(combinacao)
            f.write(palavra + "\n")

            contador += 1
            progresso = int((contador / total) * 50)
            barra = emoji * progresso + '-' * (50 - progresso)
            sys.stdout.write(f"\r[{barra}] {contador}/{total} palavras")
            sys.stdout.flush()
            time.sleep(0.01)

print(f"\nWordlist criada com sucesso! Salva em {nome_arquivo} ✅")
