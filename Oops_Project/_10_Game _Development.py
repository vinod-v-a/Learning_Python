"Game Development (RPG Game)"

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_enemy(self, enemy):
        enemy.health -= self.attack
        print(f"{self.name} attacked {enemy.name} for {self.attack} damage.")
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!")
        else:
            print(f"{enemy.name}'s health: {enemy.health}")


class Warrior(Character):
    def attack_enemy(self, enemy):
        print(f"{self.name} swings a sword!")
        super().attack_enemy(enemy)


class Mage(Character):
    def attack_enemy(self, enemy):
        print(f"{self.name} casts a spell!")
        super().attack_enemy(enemy)


class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health


# Example Usage
warrior = Warrior("Conan", 100, 15)
mage = Mage("Gandalf", 80, 20)
enemy = Enemy("Orc", 50)

warrior.attack_enemy(enemy)
mage.attack_enemy(enemy)
