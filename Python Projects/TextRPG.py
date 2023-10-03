import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

class Monster(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20)

def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print(f"{player.name}'s health: {player.health}")
        print(f"{enemy.name}'s health: {enemy.health}")
        print("1. Attack")
        print("2. Run away")
        choice = input("Your choice: ")

        if choice == '1':
            player_damage = random.randint(0, player.attack)
            enemy_damage = random.randint(0, enemy.attack)

            print(f"You hit {enemy.name} for {player_damage} damage.")
            print(f"{enemy.name} hits you for {enemy_damage} damage.")

            enemy.health -= player_damage
            player.health -= enemy_damage
        elif choice == '2':
            print("You managed to run away from the battle.")
            return False
        else:
            print("Invalid choice. Try again.")

    if player.is_alive():
        print(f"You defeated {enemy.name}!")
        return True
    else:
        print(f"{enemy.name} defeated you. Game over.")
        return False

def main():
    print("Welcome to the Text-based RPG!")
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    print(f"Welcome, {player.name}! Let's begin your adventure.")

    while True:
        enemy = Monster("Monster", random.randint(50, 100), random.randint(5, 15))
        print(f"You encounter a {enemy.name} with {enemy.health} health.")
        
        if battle(player, enemy):
            print("You continue your adventure.")
        else:
            break

if __name__ == "__main__":
    main()
