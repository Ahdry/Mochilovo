import random

# Класс героя
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(10, self.attack_power)  # Случайный урон
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")
        if other.health < 0:
            other.health = 0
        print(f"У {other.name} осталось {other.health} здоровья.\n")

    def is_alive(self):
        return self.health > 0


# Класс игры
class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("\nДобро пожаловать в игру 'Битва героев'!\n")
        round_number = 1

        while self.player.is_alive() and self.computer.is_alive():
            print(f"=== Раунд {round_number} ===")
            if round_number % 2 != 0:
                print(f"Ходит {self.player.name}...")
                self.player.attack(self.computer)
            else:
                print("Ходит Компьютер...")
                self.computer.attack(self.player)

            print(f"Состояние после раунда {round_number}:")
            print(f"{self.player.name}: {self.player.health} здоровья")
            print(f"{self.computer.name}: {self.computer.health} здоровья\n")

            round_number += 1

        # Объявление победителя
        if self.player.is_alive():
            print(f"{self.player.name} побеждает! Поздравляем!")
        else:
            print("Компьютер побеждает! Попробуйте еще раз!")


# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.start()

