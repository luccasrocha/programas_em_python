import random
import time

# --- Classes do Jogo ---

class Player:
    def __init__(self, name="Herói", health=100, attack=15, defense=5):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
        self.inventory = []
        self.current_room = None
        self.is_alive = True

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        print(f"{self.name} sofreu {actual_damage} de dano! Saúde restante: {self.health}")
        if self.health <= 0:
            self.is_alive = False
            print(f"{self.name} foi derrotado!")

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
        print(f"{self.name} curou {amount} de vida! Saúde atual: {self.health}")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{self.name} pegou: {item.name}")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                if item.item_type == "healing":
                    self.heal(item.effect)
                    self.inventory.remove(item)
                    return True
                elif item.item_type == "weapon":
                    print(f"Você equipou {item.name}. Seu ataque aumentou em {item.effect}.")
                    self.attack += item.effect
                    self.inventory.remove(item) # Remove para não poder equipar de novo
                    return True
                else:
                    print(f"Você não pode usar {item.name} agora.")
                    return False
        print(f"Você não tem '{item_name}' no seu inventário.")
        return False

    def display_stats(self):
        print("\n--- Status do Jogador ---")
        print(f"Nome: {self.name}")
        print(f"Saúde: {self.health}/{self.max_health}")
        print(f"Ataque: {self.attack}")
        print(f"Defesa: {self.defense}")
        print("Inventário:", ", ".join([item.name for item in self.inventory]) if self.inventory else "Vazio")
        print("-------------------------")

class Monster:
    def __init__(self, name, health, attack, xp_drop):
        self.name = name
        self.health = health
        self.attack = attack
        self.xp_drop = xp_drop
        self.is_alive = True

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} sofreu {damage} de dano! Saúde restante: {self.health}")
        if self.health <= 0:
            self.is_alive = False
            print(f"{self.name} foi derrotado!")

class Item:
    def __init__(self, name, item_type, effect=0):
        self.name = name
        self.item_type = item_type # e.g., "healing", "weapon", "key"
        self.effect = effect # e.g., healing amount, attack bonus

class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits # Dictionary: {"north": Room_object, "south": Room_object}
        self.monsters = []
        self.items = []
        self.visited = False

    def add_monster(self, monster):
        self.monsters.append(monster)

    def add_item(self, item):
        self.items.append(item)

    def enter(self, player):
        if not self.visited:
            print(f"\nVocê entrou na {self.name}.")
            print(self.description)
            self.visited = True
        else:
            print(f"\nVocê está de volta na {self.name}.")

        if self.monsters:
            print("Cuidado! Há monstros aqui:")
            for monster in self.monsters:
                print(f"- {monster.name} (Saúde: {monster.health})")
        if self.items:
            print("Você vê alguns itens aqui:")
            for item in self.items:
                print(f"- {item.name}")

# --- Funções do Jogo ---

def combat(player, monster):
    print(f"\n--- INÍCIO DO COMBATE: {player.name} vs {monster.name} ---")
    while player.is_alive and monster.is_alive:
        print(f"\n{player.name} (HP: {player.health}) vs {monster.name} (HP: {monster.health})")
        action = input("Sua vez! (atacar/usar item): ").lower()

        if action == "atacar":
            player_damage = random.randint(player.attack - 5, player.attack + 5)
            monster.take_damage(player_damage)
            time.sleep(1)
            if not monster.is_alive:
                print(f"Você derrotou o {monster.name}!")
                break
        elif action == "usar item":
            if not player.inventory:
                print("Seu inventário está vazio.")
                continue
            print("Itens no inventário:", ", ".join([item.name for item in player.inventory]))
            item_to_use = input("Qual item você quer usar? ").strip()
            if not player.use_item(item_to_use):
                continue # Se o item não foi usado, o turno não passa
        else:
            print("Ação inválida. Tente 'atacar' ou 'usar item'.")
            continue

        # Turno do Monstro
        if monster.is_alive:
            monster_damage = random.randint(monster.attack - 3, monster.attack + 3)
            player.take_damage(monster_damage)
            time.sleep(1)
            if not player.is_alive:
                break
    print("--- FIM DO COMBATE ---")

def game_loop():
    player_name = input("Bem-vindo à Masmorra Sombria! Qual é o nome do seu herói? ")
    player = Player(name=player_name)

    # --- Criação do Mapa (Salas) ---
    room1 = Room("Entrada da Masmorra", "Uma entrada úmida e escura. O cheiro de mofo é forte.", {})
    room2 = Room("Corredor Leste", "Um corredor estreito com tochas bruxuleantes.", {})
    room3 = Room("Câmara dos Goblins", "Uma câmara pequena, com ossos espalhados pelo chão.", {})
    room4 = Room("Arsenal Abandonado", "Armaduras enferrujadas e armas quebradas jazem aqui.", {})
    room5 = Room("Salão Principal", "Um grande salão com pilares imponentes. Parece ser o centro da masmorra.", {})
    room6 = Room("Câmara do Tesouro", "Uma sala cheia de moedas de ouro e um baú brilhante!", {}) # Sala de vitória

    # Definir saídas (conexões entre as salas)
    room1.exits = {"leste": room2, "sul": room5}
    room2.exits = {"oeste": room1, "sul": room3}
    room3.exits = {"norte": room2, "oeste": room4}
    room4.exits = {"leste": room3, "norte": room5}
    room5.exits = {"norte": room1, "leste": room4, "oeste": room6} # Sala central
    room6.exits = {"leste": room5} # Sala do tesouro

    # Adicionar monstros e itens
    room2.add_monster(Monster("Goblin", 30, 8, 10))
    room3.add_monster(Monster("Orc", 50, 12, 20))
    room3.add_item(Item("Poção de Cura", "healing", 30))
    room4.add_item(Item("Espada Envelhecida", "weapon", 10))
    room5.add_monster(Monster("Minotauro", 80, 18, 50))
    room6.add_item(Item("Tesouro Lendário", "key")) # Item de vitória

    player.current_room = room1 # Começa na entrada

    print("\n--- Aventura Começa! ---")

    while player.is_alive:
        player.current_room.enter(player)

        # Lidar com monstros na sala
        if player.current_room.monsters:
            for monster in list(player.current_room.monsters): # Usar list() para iterar sobre uma cópia
                if monster.is_alive:
                    combat(player, monster)
                    if not player.is_alive:
                        break # Sai do loop de monstros se o jogador morrer
                if not monster.is_alive:
                    player.current_room.monsters.remove(monster) # Remove o monstro derrotado

        if not player.is_alive:
            print("\nGAME OVER! Você foi derrotado na masmorra.")
            break

        # Lidar com itens na sala
        if player.current_room.items:
            for item in list(player.current_room.items):
                if item.item_type == "key" and item.name == "Tesouro Lendário":
                    print("\nParabéns! Você encontrou o Tesouro Lendário e escapou da masmorra!")
                    print("VOCÊ VENCEU O JOGO!")
                    return # Termina o jogo

                action = input(f"Você quer pegar o item '{item.name}'? (sim/não): ").lower()
                if action == "sim":
                    player.add_to_inventory(item)
                    player.current_room.items.remove(item)

        player.display_stats()

        # Opções de movimento
        print("\nPara onde você quer ir?")
        for direction, room in player.current_room.exits.items():
            print(f"- {direction} ({room.name})")
        print("- 'inventario' para ver seus itens")
        print("- 'usar item' para usar um item")
        print("- 'sair' para desistir")

        command = input("Sua escolha: ").lower()

        if command == "sair":
            print("Você desistiu da masmorra. Até a próxima!")
            break
        elif command == "inventario":
            player.display_stats()
            continue # Volta para o início do loop para não mover
        elif command == "usar item":
            if not player.inventory:
                print("Seu inventário está vazio.")
                continue
            print("Itens no inventário:", ", ".join([item.name for item in player.inventory]))
            item_to_use = input("Qual item você quer usar? ").strip()
            player.use_item(item_to_use)
            continue # Volta para o início do loop para não mover
        elif command in player.current_room.exits:
            player.current_room = player.current_room.exits[command]
        else:
            print("Comando ou direção inválida. Tente novamente.")

# --- Iniciar o Jogo ---
if __name__ == "__main__":
    game_loop()
