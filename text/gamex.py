
class Player:
    def __init__(self, name):
        self.name = name
        self.affection = 50  # Começa com um nível neutro de afeto
        self.charm = 50      # Começa com um nível neutro de charme
        self.inventory = []

    def display_stats(self):
        print(f"\n--- Estatísticas de {self.name} ---")
        print(f"Afeto: {self.affection}")
        print(f"Charme: {self.charm}")
        print(f"Inventário: {", ".join(self.inventory) if self.inventory else "Vazio"}")
        print("----------------------------------")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"Você adicionou {item} ao seu inventário.")

    def affect_affection(self, amount):
        self.affection += amount
        if self.affection > 100:
            self.affection = 100
        elif self.affection < 0:
            self.affection = 0
        print(f"Seu nível de afeto mudou em {amount}. Afeto atual: {self.affection}")

    def affect_charm(self, amount):
        self.charm += amount
        if self.charm > 100:
            self.charm = 100
        elif self.charm < 0:
            self.charm = 0
        print(f"Seu nível de charme mudou em {amount}. Charme atual: {self.charm}")

def start_game():
    print("Bem-vindo ao 'Reconquista da Ex: A Aventura'!")
    player_name = input("Qual o nome do seu amigo (o protagonista)? ")
    player = Player(player_name)
    print(f"Olá, {player.name}! Sua missão é reconquistar o coração da sua ex-namorada/o.")
    player.display_stats()

    # Aqui começaremos a adicionar as cenas e escolhas do jogo
    print("\nCapítulo 1: O Primeiro Contato")
    print("Você decide enviar uma mensagem para sua ex. O que você diz?")
    print("1. 'Oi, como você está? Faz tempo...'")
    print("2. 'Sinto sua falta. Podemos conversar?'")
    print("3. 'Vi algo que me lembrou de você. Espero que esteja bem.'")

    choice = input("Escolha (1, 2 ou 3): ")

    if choice == '1':
        print("Você enviou uma mensagem casual. Ela respondeu com um 'Tudo bem, e você?'.")
        player.affect_affection(5)
    elif choice == '2':
        print("Você foi direto ao ponto. Ela pareceu um pouco surpresa, mas concordou em conversar.")
        player.affect_affection(10)
        player.affect_charm(-5) # Pode parecer um pouco desesperado
    elif choice == '3':
        print("Você usou uma abordagem mais sutil. Ela achou fofo e perguntou o que era.")
        player.affect_affection(15)
        player.affect_charm(10)
    else:
        print("Escolha inválida. Você hesitou e não enviou nada. Oportunidade perdida.")

    player.display_stats()

    print("\nCapítulo 2: O Encontro Inesperado")
    print("Dias depois, você a encontra por acaso no seu café favorito. Ela está com uma amiga.")
    print("O que você faz?")
    print("1. Acena de longe e sorri.")
    print("2. Vai até a mesa dela para cumprimentá-la.")
    print("3. Tenta evitar o contato visual e sai discretamente.")

    choice = input("Escolha (1, 2 ou 3): ")

    if choice == '1':
        print("Você acenou e ela retribuiu com um sorriso educado. Sem grandes avanços.")
        player.affect_affection(2)
    elif choice == '2':
        print("Você se aproximou e a cumprimentou. A amiga dela pareceu um pouco desconfortável, mas sua ex foi simpática.")
        player.affect_affection(8)
        player.affect_charm(5)
    elif choice == '3':
        print("Você tentou sair, mas ela te viu. Ela pareceu um pouco desapontada. Oportunidade perdida.")
        player.affect_affection(-10)
    else:
        print("Escolha inválida. Você congelou e não fez nada. Ela te notou, mas você não agiu.")

    player.display_stats()

    print("\nO jogo continua... (Este é apenas o começo!)")
    print("Para continuar a aventura, precisaremos adicionar mais capítulos e escolhas!")

if __name__ == "__main__":
    start_game()
