## Linguagem Python

Este repositório tem como objetivo reunir algoritmos e exemplos desenvolvidos em Python, além de fornecer uma explicação completa sobre a linguagem, sua origem, principais conceitos e funcionalidades.

## Origem e Criação

A linguagem Python foi criada por Guido van Rossum em 1991, com foco em legibilidade e simplicidade de código. Seu nome é uma homenagem ao grupo de comédia britânico Monty Python. Python se destaca por sua sintaxe limpa, versatilidade e vasta biblioteca padrão, sendo amplamente utilizada em ciência de dados, desenvolvimento web, automação, inteligência artificial e muito mais.

## Por que Python

- Sintaxe simples e legível (próxima ao inglês)
- Multiplataforma (Windows, Linux, macOS)
- Enorme ecossistema de bibliotecas (pip)
- Base para Data Science, IA, Web e Automação

## Principais Pontos Importantes

- Linguagem de alto nível e interpretada
- Tipagem dinâmica (o tipo é inferido automaticamente)
- Gerenciamento automático de memória (garbage collector)
- Suporta múltiplos paradigmas: orientado a objetos, funcional e procedural
- Portável entre diferentes plataformas

### Tipos de Dados Básicos

| Tipo    | Descrição                                  | Exemplo de Uso              |
| ------- | ------------------------------------------ | --------------------------- |
| `int`   | Número inteiro (positivos e negativos)     | `idade = 25`                |
| `float` | Número de ponto flutuante                  | `altura = 1.75`             |
| `str`   | Cadeia de caracteres (texto)               | `nome = "Python"`           |
| `bool`  | Valor lógico (True ou False)               | `ativo = True`              |
| `None`  | Ausência de valor                          | `resultado = None`          |

### Estruturas de Dados Embutidas

| Tipo    | Descrição                              | Exemplo de Uso                        |
| ------- | -------------------------------------- | ------------------------------------- |
| `list`  | Coleção ordenada e mutável             | `numeros = [1, 2, 3]`                 |
| `tuple` | Coleção ordenada e imutável            | `coordenadas = (10, 20)`              |
| `dict`  | Pares chave-valor                      | `pessoa = {"nome": "Ana", "idade": 30}` |
| `set`   | Coleção sem duplicatas                 | `frutas = {"maçã", "banana"}`         |

### Exemplo de Declaração de Variáveis

```python
idade = 30
peso = 70.5
genero = 'M'
temperatura = 36.6
pontos = 100
ativo = True
nome = "Luccas"
```

> Em Python, não é necessário declarar o tipo da variável — ele é inferido automaticamente.

# Operadores

## Operadores Aritméticos

| Operador | Nome              | Exemplo       |
| -------- | ----------------- | ------------- |
| +        | Soma              | 5 + 3 = 8     |
| -        | Subtração         | 5 - 3 = 2     |
| *        | Multiplicação     | 5 * 3 = 15    |
| /        | Divisão           | 5 / 2 = 2.5   |
| //       | Divisão inteira   | 5 // 2 = 2    |
| %        | Resto             | 5 % 2 = 1     |
| **       | Potenciação       | 2 ** 3 = 8    |

## Atribuição

| Atribuição | Operador | Exemplo   | Equivalente  |
| ---------- | -------- | --------- | ------------ |
| **=**      | `=`      | `x = 5`   | `x = 5`      |
| **+=**     | `+=`     | `x += 3`  | `x = x + 3`  |
| **-=**     | `-=`     | `x -= 2`  | `x = x - 2`  |
| ***=**     | `*=`     | `x *= 4`  | `x = x * 4`  |
| **/=**     | `/=`     | `x /= 2`  | `x = x / 2`  |
| **%=**     | `%=`     | `x %= 3`  | `x = x % 3`  |
| ****=**    | `**=`    | `x **= 2` | `x = x ** 2` |

## Relacionais

| Operador | Descrição      |
| -------- | -------------- |
| ==       | Igual          |
| !=       | Diferente      |
| >        | Maior          |
| <        | Menor          |
| >=       | Maior ou igual |
| <=       | Menor ou igual |

## Lógicos

- **and (E lógico):** Retorna verdadeiro somente se **ambas** as condições forem verdadeiras.

- **or (OU lógico):** Retorna verdadeiro se **pelo menos uma** das condições for verdadeira.

- **not (negação):** Inverte o valor lógico de uma condição (True vira False e vice-versa).

# Conceitos

## PRINT

O `print()` é a função usada para exibir informações na tela. Suporta texto, variáveis, formatação e muito mais.

Exemplo de uso:

```python
idade = 25
print(f"Minha idade é {idade} anos.")  # f-string (recomendado)
print("Minha idade é", idade, "anos.") # passando variável diretamente
print("Minha idade é %d anos." % idade) # formato antigo (estilo C)
```

## INPUT

O `input()` é a função usada para ler dados digitados pelo usuário. **Sempre retorna uma string** — converta quando necessário.

| Tipo esperado | Conversão        | Exemplo de leitura                  |
| ------------- | ---------------- | ----------------------------------- |
| `int`         | `int(input())`   | `idade = int(input("Sua idade: "))` |
| `float`       | `float(input())` | `altura = float(input("Altura: "))` |
| `str`         | `input()`        | `nome = input("Seu nome: ")`        |
| `bool`        | Conversão manual | `ativo = input("Ativo? ") == "s"`   |

## Exemplo de uso:

```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"\n=== RESULTADO ===")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura:.2f} m")
```

- `input()` **sempre retorna string** — converta com `int()`, `float()`, etc.
- Use **f-strings** para formatar saídas: `f"Valor: {variavel:.2f}"`
- Para ler múltiplos valores na mesma linha: `a, b = map(int, input().split())`

## Estruturas de Controle

### IF / ELIF / ELSE

- Uso: Condições simples ou em cadeia

```python
nota = 85

# IF simples (1 condição)
if nota >= 60:
    print("Aprovado!")

# IF-ELSE (2 opções)
if nota >= 70:
    print("Bom trabalho!")
else:
    print("Estude mais!")

# ELIF (múltiplas condições)
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("Reprovado")
```

> **Atenção:** Python usa **indentação** (espaços/tab) para definir blocos — não há `{}`.

### MATCH - CASE (Python 3.10+)

- Uso: Escolha exata por valor, equivalente ao `switch` de outras linguagens

```python
op = input("(+ - * /): ")

match op:
    case '+':
        print(a + b)
    case '-':
        print(a - b)
    case '*':
        print(a * b)
    case '/':
        if b != 0:
            print(a / b)
        else:
            print("Erro: divisão por zero!")
    case _:
        print("Opção inválida!")
```

- `case _:` é o equivalente ao `default` do switch

### WHILE

- Uso: Loop quando a condição é desconhecida antes de começar

```python
soma = 0

print("Digite números (0 para parar):")
while True:  # Loop infinito
    i = int(input())
    if i == 0:
        break  # Sai do loop
    soma += i

print(f"Soma: {soma}")
```

### FOR

- Uso: Iteração sobre sequências (listas, ranges, strings...)

```python
# Tabuada completa
for i in range(1, 11):
    print(f"{i:2d}: ", end="")
    for j in range(1, 11):
        print(f"{i * j:3d} ", end="")
    print()
#  1:   1   2   3 ...  10
#  2:   2   4   6 ...  20
```

#### BREAK e CONTINUE

```python
for i in range(10):
    if i % 2 == 0:
        continue  # PULA pares
    if i == 7:
        break     # PARA em 7
    print(i, end=" ")  # 1 3 5
```

### OPERADOR TERNÁRIO

- Uso: IF de 1 linha (expressão condicional)

```python
a, b = 10, 20
maximo = a if a > b else b  # maximo = 20

status = "Adulto" if idade >= 18 else "Menor"
print(status)

# Aninhado (cuidado com legibilidade!)
conceito = "A" if x >= 90 else ("B" if x >= 80 else "C")
```

## QUANDO USAR CADA ESTRUTURA?

| Estrutura    | Melhor para                      | NÃO use para        | Exemplo Perfeito              |
| ------------ | -------------------------------- | ------------------- | ----------------------------- |
| if/elif      | Ranges, condições complexas      | Menus simples       | Classificação de notas A/B/C  |
| match/case   | Valor EXATO ('a','b',1,2,3)      | Ranges (> <)        | Menu de opções                |
| while        | Condição **desconhecida antes**  | Contadores fixos    | Leitura até digitar 0         |
| for + range  | Iterações fixas (0 a N)          | Condições complexas | Arrays, tabuada               |
| for + lista  | Percorrer coleções               | Contadores simples  | Processar itens de uma lista  |
| x if c else y | IF de 1 linha                  | Lógica complexa     | max(a, b)                     |

## NUNCA FAÇA

```python
# 1. Comparar com True/False explicitamente
if ativo == True:   # :(
    pass

# 2. Usar = ao invés de == na condição
if x = 10:          # SyntaxError!
    pass

# 3. Esquecer de converter o input
idade = input("Idade: ")
if idade > 18:      # TypeError! str vs int

# 4. Indentação inconsistente
if x > 0:
    print("positivo")
  print("ainda aqui")  # IndentationError!
```

## SEMPRE FAÇA

```python
# Use 'in' para checar pertencimento
if opcao in ['s', 'n']:
    pass

# Converta o input sempre!
idade = int(input("Idade: "))
if idade > 18:
    print("Maior de idade")

# Indentação consistente (4 espaços — padrão PEP8)
if x > 0:
    print("Positivo")
else:
    print("Não positivo")

# Use f-strings para formatar saída
print(f"Resultado: {valor:.2f}")
```
