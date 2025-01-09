import random
import os
import time
from Typewriter import *

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

winner = 0
gold = 5

# Character class as the base class
class Character:
    def __init__(self, name, level, hp, mana):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana

    def __str__(self):
        return f"\nName: {self.get_name()}, Level: {self.get_level()}, HP: {self.get_hp()}, Mana: {self.get_mana()}\n"

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_level(self):
        return self.level

    def get_hp(self):
        return self.hp

    def set_hp(self, new_hp):
        self.hp = new_hp
    
    def is_alive(self):
        return self.hp > 0

    def get_mana(self):
        return self.mana

# Player class that inherits from Character
class Player(Character):
    def __init__(self, name, level, hp, mana, strength, dexterity, intelligence, weapon, gold, xp=0):
        super().__init__(name, level, hp, mana)
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.weapon = weapon
        self.gold = gold
        self.xp = xp
        self.xp_to_level = 100 * (self.level ** 1.5)

    # Initialize stat points at start
    def allocate_initial_points(self):
        points = 10
        while points > 0:
            clear()
            print(f"Stat Points Remaining: {points}")
            print(f"Strength: {self.strength}, Dexterity: {self.dexterity}, Intelligence: {self.intelligence}")
            choice = input("Allocate point to (1: Strength, 2: Dexterity, 3: Intelligence): ")
            if choice == '1':
                self.strength += 1
            elif choice == '2':
                self.dexterity += 1
            elif choice == '3':
                self.intelligence += 1
            else:
                print("Invalid choice.")
                continue
            points -= 1

    # Stat allocation during leveling
    def level_up(self):
        self.level += 1
        self.xp = 0
        self.xp_to_level = 100 * (self.level ** 1.5)
        print(f"{self.name} has leveled up to Level {self.level}!")
        print(f"Allocate 5 stat points across Strength, Dexterity, and Intelligence.")
        points = 5
        while points > 0:
            choice = input("Allocate point to (1: Strength, 2: Dexterity, 3: Intelligence): ")
            if choice == '1':
                self.strength += 1
            elif choice == '2':
                self.dexterity += 1
            elif choice == '3':
                self.intelligence += 1
            else:
                print("Invalid choice.")
                continue
            points -= 1
        print(f"New Stats - Strength: {self.strength}, Dexterity: {self.dexterity}, Intelligence: {self.intelligence}")

    def physical_attack(self):
        return round(random.uniform((self.strength + self.weapon.damage) * 0.5, (self.strength + self.weapon.damage) * 1.5))

    def magical_attack(self):
        return round(random.uniform((self.intelligence * 1.2), self.intelligence * 1.5))

    # AoE attack
    def aoe_attack(self):
        if self.mana >= 10:
            damage = self.magical_attack() // 2
            self.mana -= 10
            return damage
        else:
            print("Not enough mana for AoE attack.")
            return 0


# Battle function updates
def battle(enemies, xp_reward):
    clear()

    def display_battle_status():
        clear()
        print(f"{helt.name} VS Enemies")
        print(f"HP: {helt.hp:<20} Mana: {helt.mana}")
        print("-" * 40)
        for enemy in enemies:
            print(f"{enemy.name} - HP: {enemy.hp}")
        print("-" * 40)

    while helt.is_alive() and any(enemy.is_alive() for enemy in enemies):
        display_battle_status()
        print("\nWhat will you do?")
        print("1: Single Attack  2: AoE Attack  3: Use Potion  4: Escape")
        choice = input("Choose action: ")

        if choice == "1":
            target = int(input(f"Choose target (1-{len(enemies)}): ")) - 1
            if 0 <= target < len(enemies):
                enemy = enemies[target]
                if enemy.is_alive():
                    damage = helt.physical_attack()
                    enemy.set_hp(enemy.get_hp() - damage)
                    print(f"You dealt {damage} damage to {enemy.name}!")

        elif choice == "2":
            damage = helt.aoe_attack()
            if damage > 0:
                for enemy in enemies:
                    if enemy.is_alive():
                        enemy.set_hp(enemy.get_hp() - damage)
                        print(f"You dealt {damage} AoE damage to {enemy.name}!")
        else:
            print("Invalid choice, try again.")