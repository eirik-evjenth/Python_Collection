class Monster:

    # attributes
    health = 90
    energy = 40

    # methods
    def attack(self, amount):
        print("the monster was attacked!")
        print(f'{amount} damage was dealt')
        monster.energy -= 20
        print(monster.energy)

    def move(self, speed):
        print(f"The monster has moved")
        print(f"It has a speed of {speed}")
        monster.energy -= 10
        print(monster.energy)

monster = Monster()
# monster.attack(40)
monster.move(10)