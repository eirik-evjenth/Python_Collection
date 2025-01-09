import random
import os
import time
from Typewriter import *  # Assuming you have a Typewriter module for text output effects


# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

winner = 0
gold = 5
farmp = 0
banditp = 0
priestp = 0

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
    def __init__(self, name, level, hp, mana, strength, dexterity, intelligence, vitality, weapon, gold, xp=0):
        Character.__init__(self, name, level, hp, mana)
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.vitality = vitality
        self.weapon = weapon
        self.gold = gold
        self.xp = xp
        self.xp_to_level = 100 * (self.level ** 1.5)

        # Distribute initial stat points

    def distribute_stat_points(self, points):
        while points > 0:
            clear()
            print(f"\nYou have {points} stat points to distribute.")
            print(f"1: Strength ({self.strength})")
            print(f"2: Dexterity ({self.dexterity})")
            print(f"3: Intelligence ({self.intelligence})")
            print(f"4: Vitality ({self.vitality})")
            choice = input("Choose a stat to increase: ")
            try:
                choice = int(choice)
                if choice == 1:
                    self.strength += 1
                elif choice == 2:
                    self.dexterity += 1
                elif choice == 3:
                    self.intelligence += 1
                elif choice == 4:
                    self.vitality += 1
                else:
                    print("Choose a number between 1 and 4")
                    continue
                points -= 1
            except ValueError:
                print("Invalid input! Please enter a number.")

    def magical_attack(self, target=None):
        if self.mana < 5:
            skrivUt("Not enough mana!")
            return 0
        self.mana -= 5
        if target:
            damage = round(random.uniform((self.intelligence + self.weapon.damage) * 0.8, (self.intelligence + self.weapon.damage) * 1.2))
            target.set_hp(target.get_hp() - damage)
            return damage
        else:
            total_damage = 0
            for enemy in self.enemies:
                damage = round(random.uniform((self.intelligence + self.weapon.damage) * 0.5, (self.intelligence + self.weapon.damage) * 1.0))
                enemy.set_hp(enemy.get_hp() - damage)
                total_damage += damage
            return total_damage

    def physical_attack(self, target=None):
        if target:
            damage = round(random.uniform((self.strength + self.weapon.damage) * 0.8, (self.strength + self.weapon.damage) * 1.2))
            target.set_hp(target.get_hp() - damage)
            return damage
        else:
            total_damage = 0
            for enemy in enemies:
                damage = round(random.uniform((self.strength + self.weapon.damage) * 0.5, (self.strength + self.weapon.damage) * 1.0))
                enemy.set_hp(enemy.get_hp() - damage)
                total_damage += damage
            return total_damage

    # Gain XP and check if player can level up
    def gain_xp(self, xp_gain):
        self.xp += xp_gain
        skrivUt(f"{self.name} gained {xp_gain} XP!\n")
        time.sleep(1)
        while self.xp >= self.xp_to_level:
            self.level_up()  # Level up until XP is lower than needed for next level


    # Level up the player
    def level_up(self):
        clear()
        self.level += 1
        self.xp -= self.xp_to_level  # Reset XP
        self.xp_to_level = 100 * (self.level ** 1.5)  # Increase XP needed for next level
        self.distribute_stat_points(4)
        clear()
        skrivUt(f"{self.name} have leveled up to Level {self.level}!")
        skrivUt(f'''\n
New Stats:
    Strength: {self.strength}
    Dexterity: {self.dexterity}
    Intelligence: {self.intelligence}
    vitality: {self.vitality}\n''')
    
        time.sleep(2)

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, HP: {self.hp}, Mana: {self.mana}, Strength: {self.strength}, Dexterity: {self.dexterity}, Intelligence: {self.intelligence}, Vitality: {self.vitality}\n"

class Enemy(Character):
    def __init__(self, name, level, hp, mana, attack, defense, xp_reward):
        super().__init__(name, level, hp, mana)
        self.attack = attack
        self.defense = defense
        self.xp_reward = xp_reward

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_xp_reward(self):
        return self.xp_reward

    def attack_player(self, player):
        damage = max(0, self.attack - player.get_defense())
        player.set_hp(player.get_hp() - damage)
        return damage

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, HP: {self.hp}, Mana: {self.mana}, Attack: {self.attack}, Defense: {self.defense}, XP Reward: {self.xp_reward}\n"

# Weapon class
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return self.name

# Sword and Staff subclasses
class Sword(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

class Staff(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)


# Armor class
class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def __str__(self):
        return self.name

# Add get_defense method to Player class
def get_defense(self):
    if hasattr(self, 'armor'):
        return self.armor.defense
    return 0

Player.get_defense = get_defense


# Function to use a health potion
def use_health_potion(player):
    if "Health Potion" in potions:
        player.set_hp(player.get_hp() + 30)
        potions.remove("Health Potion")
        clear()
        skrivUt("You used a Health Potion and gained 30 HP!\n")
    else:
        skrivUt("You don't have any Health Potions left.\n")

# Create initial weapon and potion list
potions = ["Health Potion"]
inventory = []


slime = Enemy("Slime", 1, 30, 10, 5, 2, 20)
goblin = Enemy("Goblin", 1, 50, 10, 7, 3, 30)
orc = Enemy("Orc", 1, 70, 10, 10, 5, 50)
bandit_leader = Enemy("Bandit Leader", 3, 75, 10, 15, 8, 100)
bandit = Enemy("Bandit", 3, 50, 10, 7, 3, 55)

enemies = [slime, goblin, orc]
# Define subclasses for different player classes
class Rogue(Player):
    def __init__(self, name, level, hp, mana, strength, dexterity, intelligence, vitality, weapon, gold, xp=0):
        super().__init__(name, level, hp, mana, strength, dexterity, intelligence, vitality, weapon, gold, xp)
        self.strength += 3

class Mage(Player):
    def __init__(self, name, level, hp, mana, strength, dexterity, intelligence, vitality, weapon, gold, xp=0):
        super().__init__(name, level, hp, mana, strength, dexterity, intelligence, vitality, weapon, gold, xp)
        self.intelligence += 3

class Archer(Player):
    def __init__(self, name, level, hp, mana, strength, dexterity, intelligence, vitality, weapon, gold, xp=0):
        super().__init__(name, level, hp, mana, strength, dexterity, intelligence, vitality, weapon, gold, xp)
        self.dexterity += 1
        self.intelligence += 1 
        self.strength += 1

class Assassin(Player):
    def __init__(self, name, level, hp, mana, strength, dexterity, intelligence, vitality, weapon, gold, xp=0):
        super().__init__(name, level, hp, mana, strength, dexterity, intelligence, vitality, weapon, gold, xp)
        self.dexterity += 3  # Assassins have higher dexterity

def battle(enemies, xp_reward, escape_callback):
    global winner  # Access global winner variable
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
        print("Attack ----- Magic ----- Potions ----- Escape")
        choice = input("Choose what to do: ").lower()

        # Player attack choice
        if choice == "attack":
            if isinstance(helt.weapon, Sword):
                attack_type = input("Choose attack type (single/multiple): ").lower()
                if attack_type == "single":
                    # Check if only one enemy is alive and select it automatically
                    alive_enemies = [enemy for enemy in enemies if enemy.is_alive()]
                    if len(alive_enemies) == 1:
                        target = alive_enemies[0]
                    else:
                        target_index = int(input(f"Choose target (1-{len(alive_enemies)}): ")) - 1
                        target = alive_enemies[target_index] if 0 <= target_index < len(alive_enemies) else None

                    if target and target.is_alive():
                        damage = helt.physical_attack(target)
                        display_battle_status()
                        skrivUt(f"{helt.name} attacked {target.name} for {damage} damage!\n")
                        time.sleep(1)
                    else:
                        skrivUt("Invalid target.")
                elif attack_type == "multiple":
                    total_damage = helt.physical_attack()
                    display_battle_status()
                    skrivUt(f"{helt.name} attacked all enemies for {total_damage} total damage!\n")
                    time.sleep(1)
                else:
                    skrivUt("Invalid attack type.")
            else:
                skrivUt("You can't use this attack with your current weapon.")
                skrivUt("In your indecision, you get attacked while looking like a fool.")
                time.sleep(1)

            # Enemy attacks
            for enemy in enemies:
                if enemy.is_alive():
                    enemy_attack = enemy.get_attack()
                    helt.set_hp(helt.get_hp() - enemy_attack)
                    if helt.get_hp() < 0:
                        helt.set_hp(0)
                    display_battle_status()
                    skrivUt(f"{enemy.name} attacks and deals {enemy_attack} damage!\n")
                    time.sleep(2)

        elif choice == "magic":
            if isinstance(helt.weapon, Staff):
                attack_type = input("Choose attack type (single/multiple): ").lower()
                if attack_type == "single":
                    alive_enemies = [enemy for enemy in enemies if enemy.is_alive()]
                    if len(alive_enemies) == 1:
                        target = alive_enemies[0]
                    else:
                        target_index = int(input(f"Choose target (1-{len(alive_enemies)}): ")) - 1
                        target = alive_enemies[target_index] if 0 <= target_index < len(alive_enemies) else None

                    if target and target.is_alive():
                        damage = helt.magical_attack(target)
                        display_battle_status()
                        skrivUt(f"{helt.name} cast a spell on {target.name} for {damage} damage!\n")
                        time.sleep(1)
                    else:
                        skrivUt("Invalid target.")
                elif attack_type == "multiple":
                    total_damage = helt.magical_attack()
                    display_battle_status()
                    skrivUt(f"{helt.name} cast a spell on all enemies for {total_damage} total damage!\n")
                    time.sleep(1)
                else:
                    skrivUt("Invalid attack type.")
            else:
                skrivUt("You can't use this attack with your current weapon.")
                time.sleep(1)

            # Enemy attacks
            for enemy in enemies:
                if enemy.is_alive():
                    enemy_attack = enemy.get_attack()
                    helt.set_hp(helt.get_hp() - enemy_attack)
                    if helt.get_hp() < 0:
                        helt.set_hp(0)
                    display_battle_status()
                    skrivUt(f"{enemy.name} attacks and deals {enemy_attack} damage!\n")
                    time.sleep(2)

        elif choice == "potions":
            clear()
            if "Health Potion" in potions:
                for index, potion in enumerate(potions):
                    skrivUt(f"{index + 1}: {potion}")
                potion_choice = int(input("\nChoose a potion to use: \n")) - 1
                if 0 <= potion_choice < len(potions):
                    if potions[potion_choice] == "Health Potion":
                        use_health_potion(helt)
                        time.sleep(1)

                        # Enemies attack after using a potion
                        for enemy in enemies:
                            if enemy.is_alive():
                                enemy_attack = random.randint(5, 15)
                                helt.set_hp(helt.get_hp() - enemy_attack)
                                if helt.get_hp() < 0:
                                    helt.set_hp(0)
                                display_battle_status()
                                skrivUt(f"{enemy.name} attacks and deals {enemy_attack} damage!\n")
                                time.sleep(2)
                else:
                    skrivUt("Invalid potion choice.")
            else:
                skrivUt("You have no potions to use!\n")
                time.sleep(1)

        elif choice == "escape":
            clear()
            skrivUt("You escaped the battle!\n")
            time.sleep(2)
            winner = 1  # Player wins by escaping
            escape_callback()
            return

        else:
            skrivUt("Invalid choice, please try again.\n")
            time.sleep(1)

    # Determine the winner
    if not helt.is_alive():
        clear()
        skrivUt(f"{helt.name} have been defeated!\n")
        time.sleep(2)
        winner = 2  # Player loses
        exit()
    elif not any(enemy.is_alive() for enemy in enemies):
        skrivUt("You defeated the opposition!\n")
        helt.gain_xp(xp_reward)
        winner = 3  # Player wins
        time.sleep(2)
        clear()


def game_start():
    clear()
    helt.distribute_stat_points(10)
    clear()
    skrivUt('''
You wake up in a dimly lit cave.
Dripping water echoes around you, and you can make out two paths ahead:
1: Go towards the distant light
2: Head deeper into the dark cave
3: Investigate the surroundings carefully\n''')
    first_choice = int(input(" "))
    clear()

    if first_choice == 1:
        outside_cave()
    elif first_choice == 2:
        deeper_cave()
    elif first_choice == 3:
        passage_entrance()


def deeper_cave():
    clear()
    skrivUt(''' 
You venture further into the depths of the cave.
Rounding a corner, you find a group of three sleeping goblins in front of a treasure chest.
1: Sneak past them to reach the chest
2: Attack the goblins head-on
3: Retreat to the cave entrance\n''')
    deeper_choice = int(input(" "))
    clear()

    if deeper_choice == 1:
        if helt.dexterity >= 5:
            skrivUt('''
You successfully sneak past the goblins and reach the chest.
You find a magical staff and 10 gold in the chest.
You decide to take everything and move to the light.
            
    + Magical Staff
    + 10 gold
                    
\n''')            
            helt.weapon = (Staff("Magical Staff", 9))
            global gold
            gold += 10
            time.sleep(2)
            outside_cave()
            

        elif helt.dexterity in [3, 4]:
            skrivUt("You attempt to sneak past, but one goblin wakes.\n")
            time.sleep(1)
            battle([goblin], 50, outside_cave)
            if winner == 3:
                skrivUt('''
You successfully sneak past the goblins and reach the chest.
You find a magical staff and 10 gold in the chest.
You decide to take everything and move to the light.
            
    + Magical Staff
    + 10 gold
                    
\n''')            
                helt.weapon = (Staff("Magical Staff", 9))
                gold += 10
                time.sleep(2)
                outside_cave()
            
        elif helt.dexterity == 2:
            skrivUt("You attempt to sneak past, but one goblin stirs, waking another.\n")
            time.sleep(1)
            battle([Enemy("Goblin", 1, 50, 10, 7, 3, 30), Enemy("Goblin", 1, 50, 10, 7, 3, 30)], 100, outside_cave)
            if winner == 3:
                skrivUt('''
You successfully sneak past the goblins and reach the chest.
You find a magical staff and 10 gold in the chest.
You decide to take everything and move to the light.
            
    + Magical Staff
    + 10 gold
                    
\n''')            
                helt.weapon = (Staff("Magical Staff", 9))
                gold += 10
                time.sleep(2)
                outside_cave()
            
        skrivUt("You attempt to sneak past, but one goblin stirs, waking the others.\n")
        time.sleep(1)
        battle([Enemy("Goblin", 1, 50, 10, 7, 3, 30), Enemy("Goblin", 1, 50, 10, 7, 3, 30), Enemy("Goblin", 1, 50, 10, 7, 3, 30)], 150, outside_cave)
        if winner == 3:
            skrivUt('''
You successfully sneak past the goblins and reach the chest.
You find a magical staff and 10 gold in the chest.
You decide to take everything and move to the light.
            
    + Magical Staff
    + 10 gold
                    
\n''')            
            helt.weapon = (Staff("Magical Staff", 9))
            gold += 10
            time.sleep(2)
            outside_cave()
                


    elif deeper_choice == 2:
        skrivUt("You charge at the goblins!\n")
        time.sleep(1)
        battle([Enemy("Goblin", 1, 50, 10, 7, 3, 30), Enemy("Goblin", 1, 50, 10, 7, 3, 30), Enemy("Goblin", 1, 50, 10, 7, 3, 30)], 150, outside_cave)
        if winner == 3:
            skrivUt('''
You successfully sneak past the goblins and reach the chest.
You find a magical staff and 10 gold in the chest.
You decide to take everything and move to the light.
            
    + Magical Staff
    + 10 gold
\n''')            
            helt.weapon = (Staff("Magical Staff", 9))
            gold += 10
            time.sleep(3)
            outside_cave()
        
    elif deeper_choice == 3:
        skrivUt("You decide it's better to turn back.\n")
        outside_cave()


def passage_entrance():
    clear()
    skrivUt('''
Exploring the surroundings, you find a hidden passage with a slime blocking the way.
1: Fight the slime
2: Run away, back to the light\n''')
    passage_choice = int(input(" "))
    clear()
    
    if passage_choice == 1:
        battle([slime], 30, outside_cave)
        skrivUt('''
After defeating the slime, you go down the hidden passage.
You descend down the dark passage and find a bag with 5 gold coins,
Beside it is a dagger inscribed with a gem.

    + 5 gold coins
    + Shardfang Sword''')

        helt.weapon = (Sword("Shardfang", 7))
        global gold
        gold += 5
        time.sleep(2)
        clear()
        skrivUt('''
After collecting the loot you get out of the passage and look around
1. Go towards the light
2. Go deeper in the cave''')
        
        passage_exit_choice = int(input("\nChoose where to go next: \n"))
        if passage_exit_choice == 1:
            outside_cave()
        elif passage_exit_choice == 2:
            deeper_cave()
        else:
            skrivUt("In you indecision you stumble deeper into the cave.\n")
            time.sleep(1)
            deeper_cave()
            
    elif passage_choice == 2:
        skrivUt("You run away with your tail between your legs leaving the cave.\n")
        time.sleep(2)
        outside_cave()
    else:
        skrivUt("Invalid choice, try again.\n")
        time.sleep(1)
        passage_entrance()


def outside_cave():
    clear()
    skrivUt('''
Emerging from the cave, you find yourself on a hillside overlooking a small village.
1: Head straight to the village
2: Investigate a nearby forest path
3: Explore the hillside further\n''')
    outside_choice = int(input(" "))
    clear()
    
    if outside_choice == 1:
        clear()
        skrivUt("You make your way towards the village.\n")
        time.sleep(1)
        village()
    elif outside_choice == 2:
        skrivUt("The forest is thick and dark, but you proceed cautiously.")
        forest()
    elif outside_choice == 3:
        skrivUt('''
You search the hillside, finding some herbs.
                
    + magical herbs
                
As it's getting dark you decide to hurry over to the village\n''')

        inventory.append["magical herbs"]
        time.sleep(2)
        village()
    else:
        skrivUt("Invalid choice, try again\n.")
        time.sleep(1)
        outside_cave()



def village():
    clear()
    skrivUt('''
Upon reaching the village, you see several locations:
1: Visit the blacksmith for weapon upgrades
2: Go to the church for healing or blessings
3: Enter the town hall to seek quests or information\n''')
    town_choice = int(input(" "))
    clear()
    if town_choice == 1:
        blacksmith_area()
    elif town_choice == 2:
        church()
    elif town_choice == 3:
        town_hall()
    else:
        skrivUt("Invalid choice, try again.\n")
        village()

# Blacksmith function
def blacksmith_area():
    clear()
    global gold
    skrivUt(f'''
    You have {gold} gold.
The blacksmith greets you, looking you up and down.
He offers the following items for sale:
1. Iron Sword (Damage: 5) - 10 gold
2. Steel Sword (Damage: 10) - 15 gold
3. Leather Armor (Defense: 5) - 10 gold
4. Chainmail Armor (Defense: 10) - 20 gold
5. Dragonslayer (Damage: 15) - 25 gold
6. Leave silently.\n''')
    blacksmith_request = int(input(" "))

    if blacksmith_request == 1 and gold >= 10:
        if helt.weapon.damage >= 5:
            confirm = input("The Iron Sword is weaker than your current weapon. Are you sure you want to buy it? (yes/no): ").lower()
            if confirm != "yes":
                blacksmith_area()
                return
        skrivUt("You purchase the Iron Sword.\n")
        helt.weapon = Sword("Iron Sword", 5)
        gold -= 10
        time.sleep(1)
        village()
    elif blacksmith_request == 2 and gold >= 15:
        if helt.weapon.damage >= 10:
            confirm = input("The Steel Sword is weaker than your current weapon. Are you sure you want to buy it? (yes/no): ").lower()
            if confirm != "yes":
                blacksmith_area()
                return
        skrivUt("You purchase the Steel Sword.\n")
        helt.weapon = Sword("Steel Sword", 10)
        gold -= 15
        time.sleep(1)
        village()
    elif blacksmith_request == 3 and gold >= 10:
        if hasattr(helt, 'armor') and helt.armor.defense >= 5:
            confirm = input("The Leather Armor is weaker than your current armor. Are you sure you want to buy it? (yes/no): ").lower()
            if confirm != "yes":
                blacksmith_area()
                return
        skrivUt("You purchase the Leather Armor.\n")
        helt.armor = Armor("Leather Armor", 5)
        gold -= 10
        time.sleep(1)
        village()
    elif blacksmith_request == 4 and gold >= 20:
        if hasattr(helt, 'armor') and helt.armor.defense >= 10:
            confirm = input("The Chainmail Armor is weaker than your current armor. Are you sure you want to buy it? (yes/no): ").lower()
            if confirm != "yes":
                blacksmith_area()
                return
        skrivUt("You purchase the Chainmail Armor.\n")
        helt.armor = Armor("Chainmail Armor", 10)
        gold -= 20
        time.sleep(1)
        village()
    elif blacksmith_request == 5 and gold >= 25:
        skrivUt("You purchase the Dragonslayer.\n")
        helt.weapon = Sword("Dragonslayer", 15)
        gold -= 25
        time.sleep(1)
        village()
    elif blacksmith_request in [1, 2, 3, 4, 5]:
        skrivUt("You do not have enough gold.\n")
        time.sleep(1)
        village()
    elif blacksmith_request == 6:
        skrivUt('''
The blacksmith sighs ---
Come again when you have enough money
                \n''')
        time.sleep(1)
        village()
    else:
        skrivUt("Invalid choice.")
        time.sleep(1)
        clear()
        blacksmith_area()

# Church function
def church():
    clear()
    skrivUt('''
You enter the church and feel a holy feel
You see a priest standing by the altar, looking troubled
The priest looks at you and asks what you want
1. Ask to be healed
2. Ask why the priest looks troubled
3. Bow and leave\n''')
    church_choice = int(input(" "))


    if church_choice == 1:
        clear()
        skrivUt(f'''
The priest looks at you and your scars
He says you have {helt.hp} Hp
The priest blesses you, restoring your health.\n''')
        helt.hp = ((helt.level - 1 + helt.vitality) * 10) + 100
        helt.mana = helt.intelligence * 5 + 5
        time.sleep(1)
        village()
    elif church_choice == 2:
        clear()
        if "Artifact" in inventory:
            skrivUt(f'''
Well these bandits took my artif-
Oh, you found the artifact!
The priest takes the artifact to a marble statue
The whole church lights up
The priest uses the power of the artifact to bless you
restoring your health and granting you a divine shield.


    + 3 strength
    + 3 dexterity
    + 3 intelligence

    - Artifact\n''')
            time.sleep(3)
            clear()
            skrivUt("The divine power will last the rest of your life")
            helt.hp = ((helt.level - 1 + helt.vitality) * 10) + 110
            helt.mana = helt.intelligence * 5 + 15
            helt.strength += 3
            helt.dexterity += 3
            helt.intelligence += 3
            helt.vitality += 3
            inventory.remove("Artifact")
            global priestp
            priestp += 1
            time.sleep(3)
            village()
        elif priestp == 1:
            skrivUt("I think i forgot if the oven was on")
            time.sleep(1)
            village()
        else:
            skrivUt('''
The priest explains that bandits have stolen a sacred artifact, 
and he cannot perform blessings without it.
You decide to help the priest retrieve the artifact.\n''')
    elif church_choice == 3:
        clear()
        skrivUt("You bow respectfully and leave the church.\n")
        time.sleep(1)
        village()
    else:
        clear()
        skrivUt("Invalid choice, try again.\n")
        time.sleep(1)
        church()

# Town hall function
def town_hall():
    clear()

    if helt.name == "You":

        skrivUt('''
You approach the quest board and see many of varying difficulties.
The village chief approaches you while you are studying the various quests.
He asks you, "What is your name, hero?
Enter your name: ''')

    # Set player name
        helt.set_name(input(""))
        clear()
        skrivUt(f'''
\nHello {helt.get_name()}, I am the Town Chief.
Our village has been terrorized by a red drake.
I hope you will be the one that saves us.
Though for now, you should look at some of the easier quests.
1: Help the farmer with a pest problem (Easy)
2: Retrieve a stolen artifact from bandits (Medium)
3: Defeat the drake terrorizing the region (Hard)\n''')


        quest_choice = int(input("Choose a quest: "))
        clear()
        if quest_choice == 1:
            skrivUt("You decide to help the farmer with his pest problem.\n")
            time.sleep(1)
            farm()
        elif quest_choice == 2:
            skrivUt("You set out to retrieve the stolen artifact from the bandits.\n")
            time.sleep(1)
            bandit_camp()
        elif quest_choice == 3:
            skrivUt("You prepare yourself to face the drake.\n")
            time.sleep(1)
            drake_lair()
        else:
            skrivUt("Invalid choice, try again.\n")
            time.sleep(1)
            town_hall()
    
    else:
        clear()
        skrivUt(f'''
\nHello {helt.get_name()}, I am the Town Chief.
Our village has been terrorized by a red drake.
I hope you will be the one that saves us.
Though for now, you should look at some of the easier quests.
1: Help the farmer with a pest problem (Easy)
2: Retrieve a stolen artifact from bandits (Medium)
3: Defeat the dragon terrorizing the region (Hard)\n''')


        quest_choice = int(input("Choose a quest: "))
        clear()
        if quest_choice == 1:
            if farmp == 0:
                skrivUt("You decide to help the farmer with his pest problem.\n")
                time.sleep(1)
                farm()
            else:
                skrivUt('''
The village chief looks at the quest and tells you
"Damn that farmer has not taken down his quest yet."
I'll ask my assistant to fix this later.\n''')
                time.sleep(2)
                village()
        elif quest_choice == 2:
            if banditp == 0:
                skrivUt("You set out to retrieve the stolen artifact from the bandits.\n")
                time.sleep(1)
                bandit_camp()
            else:
                skrivUt('''
The village chief looks at the quest and tells you
"Those bandits are long gone, no need to worry."
I'll ask my assistant to take the quest away later.\n''')
                time.sleep(2)
                village()
        elif quest_choice == 3:
            skrivUt("You prepare yourself to face the drake.\n")
            time.sleep(1)
            drake_lair()
        else:
            skrivUt("Invalid choice, try again.\n")
            time.sleep(1)
            town_hall()

# Farm quest function
def farm():
    clear()
    skrivUt("You arrive at the farm and see giant rats attacking the crops.\n")
    time.sleep(2)
    battle([Enemy("Giant rat", 3, 45, 10, 5, 0, 55)], 55, village)
    skrivUt('''
You have cleared the farm of pests and return to the village.

    + 5 gold\n''')
    global farmp
    farmp += 1
    global gold
    gold += 5
    time.sleep(2)
    village()


    # Bandit camp quest function
def bandit_camp():
    clear()
    skrivUt("You find the bandit camp and prepare for battle.\n")
    time.sleep(2)
    battle([Enemy("Bandit", 3, 50, 10, 7, 3, 55), Enemy("Bandit", 3, 50, 10, 7, 3, 55)], 110, village)
    skrivUt('''
After a hard fought battle the priest heals you 
            
    + 20 HP

But the battle is not over
The bandit leader appears with the artifact in hand.\n''')
    time.sleep(2)
    helt.hp += 20
    battle([bandit_leader], 75, village)
    skrivUt('''
After a hard fought battle you defeat the bandit leader
You retrieve the stolen artifact and some gold and return to the village.
            
    + Artifact
    + 15 gold\n''')

    global gold
    gold += 15
    inventory.append("Artifact")
    global banditp
    banditp += 1
    time.sleep(2)
    village()


    # Drake lair quest function
def drake_lair():
    clear()
    skrivUt("You enter the drake's lair, ready for the final battle.\n")
    time.sleep(2)
    battle([Enemy("Bandit", 3, 200, 10, 30, 10, 55)], 500, village)
    clear()
    skrivUt("You have defeated the drake and return to the village as a hero.\n")
    skrivUt("You have won the demo of this game!")
    time.sleep(3)
    exit()

# Forest exploration with unique encounters
def forest():
    skrivUt('''
The forest is dark and dense, with eerie sounds all around.
1: Follow a small trail deeper into the forest
2: Set up a camp to rest
3: Return to the village\n''')
    forest_choice = int(input(" "))
    clear()
    
    if forest_choice == 1:
        skrivUt("You encounter a wild wolf!\n")
        time.sleep(1)
        battle([Character("Wolf", 1, 40, 0)], 50, village)
        skrivUt('''
After defeating the wolf you wander the entire night in order to find the village
Arriving to the village with no sleep and pain swelling
                
    \n''')
        helt.hp -= 20
        if helt.hp < 1:
            helt.hp == 1
        time.sleep(2)
        clear()
        village()
    elif forest_choice == 2:
        skrivUt('''
You rest, recovering some health 

    + 10 Xp
    + 20 HP.\n''')
        helt.hp += 20
        time.sleep(2)
        village()
    elif forest_choice == 3:
        skrivUt("You head back to the village.\n")
        time.sleep(2)
        village()
    else:
        skrivUt("Invalid choice, try again.\n")
        time.sleep(1)
        forest()

while True:
    clear()
    skrivUt('''
Welcome to the Game!
1: Start Game
2: Exit\n''')

    choice = input("Choose an option: \n")

    if choice == "1":
        clear()
        skrivUt('''
Choose your class:
1: Rogue
2: Archer
3: Assasin
4: Mage\n''')

        class_choice = input("Choose a class: \n")

        if class_choice == "1":
            helt = Rogue("You", 1, 100, 10, 1, 1, 1, 1, Sword("Shortsword", 3), 5)
        elif class_choice == "2":
            helt = Archer("You", 1, 100, 10, 1, 1, 1, 1, Sword("Bow", 3), 5)
        elif class_choice == "3":
            helt = Assassin("You", 1, 100, 10, 1, 1, 1, 1, Sword("Dagger", 3), 5)
        elif class_choice == "4":
            helt = Mage("You", 1, 100, 10, 1, 1, 1, 1, Staff("Basic Staff", 3), 5)
        else:
            skrivUt("Invalid class choice.\n")
            time.sleep(2)
            continue

        game_start()
    elif choice == "2":
        clear()
        skrivUt("Goodbye soldier o7")
        time.sleep(2)
        exit()
    else:
        skrivUt("Invalid choice.\n")
        time.sleep(2)
