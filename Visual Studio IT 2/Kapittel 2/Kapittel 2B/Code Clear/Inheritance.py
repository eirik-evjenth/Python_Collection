class Monster:
    def __init__(self, health: int, energy: int, damage, attack):
        self.health = health
        self.energy = energy
        self.damage = damage
        self.attack = attack

    def get_health(self):
        return self.health

    def set_health(self, health):
        if 0 <= health <= 100:
            self.health = health
        else:
            print("Health must be between 0 and 100")

    def get_energy(self):
        return self.energy

    def set_energy(self, energy):
        if 0 <= energy <= 100:
            self.energy = energy
        else:
            print("Energy must be between 0 and 100")

    def get_damage(self):
        return self.damage

    def set_damage(self, damage):
        self.energy = damage


    def move(self, speed):
        print(f"The Monster has moved with {speed} speed")




class Shark(Monster):
    def __init__(self, health, energy, damage, age):
        super().__init__(health, energy, damage)
        self.age = age

    def move(self, SwimSpeed):
        print(f"The shark has moved with {SwimSpeed} speed")


class Hero:
    def __init__(self, health, energy, damage, monster):
        self.health = health
        self.energy = energy
        self.damage = damage
        self.monster = monster

    def get_health(self):
        return self.health

    def set_health(self, health):
        if 0 <= health <= 100:
            self.health = health
        else:
            print("Health must be between 0 and 100")

    def get_energy(self):
        return self.energy

    def set_energy(self, energy):
        if 0 <= energy <= 100:
            self.energy = energy
        else:
            print("Energy must be between 0 and 100")

    def attack(self, monster):
        new_health = monster.get_health() - self.damage
        monster.set_health(new_health)
        print("The hero attacked the monster using 20 energy!")
        print(f"Monster's health is now {monster.get_health()}")

        new_energy = hero.get_energy() - 20
        hero.set_energy(new_energy)


class Attack:
    def bite(self):
        print("The monster bites")

        new_health = hero.get_health() - monster.get_damage()
        hero.set_health(new_health)

        print(f"The hero took {monster.get_damage()} damage")
        print(f"The heros new health is {hero.get_health()}")

    def claw(self):
        print("The monster has clawed")
        
        new_health = hero.get_health() - monster.get_damage()
        hero.set_health(new_health)

        print(f"The hero took {monster.get_damage()} damage")
        print(f"The heros new health is {hero.get_health()}")

class Scorpion(Monster):
    def __init__(self, health, energy, poison_damage, attack):
        super().__init__(health, energy, attack)
        self.poison_damage = poison_damage

    def get_damage(self):
        return self.poison_damage

    def set_damage(self, poison_damage):
        self.energy = poison_damage






attack = Attack()
monster = Monster(health=50, energy=50, damage = 20, attack = attack.claw)
hero = Hero(health=100, energy=100, damage=20, monster=monster)

print(f"The heros energy is: {hero.energy}")

print(f"The monster has {monster.get_health()} health")


hero.attack(monster)

monster.attack()



'''

1. **Encapsulation**: Use getter and setter methods to access or modify attributes like `health` and `energy` instead of directly accessing them.

2. **Polymorphism**: Add more specific behaviors to the `Shark` class or other potential subclasses of `Monster` to demonstrate polymorphism.

3. **Error Handling**: Add checks to ensure that `health` or `energy` values do not go below zero or exceed a maximum limit.

4. **Attack Variants**: Implement the `Attacks` class methods (`bite` and `claw`) and associate them with specific monsters.

5. **Energy Consumption**: Deduct energy from the hero or monster when they perform actions like attacking or moving.

6. **Game Loop**: Add a simple game loop to simulate interactions between the hero and monsters.

7. **Additional Monsters**: Create more subclasses of `Monster` with unique attributes and behaviors.

8. **Victory/Defeat Conditions**: Add logic to determine when the hero or monster wins or loses based on health.

9. **Documentation**: Add docstrings to classes and methods to explain their purpose.

10. **Input Handling**: Allow user input to control the hero's actions (e.g., attack, move).

These changes can make the program more robust, interactive, and feature-rich.
'''