import random

# Game settings
MAP_WIDTH = 10
MAP_HEIGHT = 10

# Dungeon tiles
TILES = {
    'FLOOR': '.',
    'WALL': '#',
    'PLAYER': '@',
    'ENEMY': 'E',
    'BOSS': 'B',
    'EXIT': 'X',
    'TREASURE': 'T',
}

# Elements and types
ELEMENTS = ['Fire', 'Water', 'Earth', 'Air']

# Directions for movement
DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Character stats and leveling
class Character:
    def __init__(self, x, y, element, level=1, hp=10, atk=5, defense=2):
        self.x = x
        self.y = y
        self.level = level
        self.element = element
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.exp = 0
        self.symbol = '@' if element == 'Player' else 'E'

    def attack(self, target):
        # Damage calculation with possible critical hit
        crit_chance = random.random()
        damage = self.atk - target.defense
        if crit_chance < 0.1:  # 10% critical hit
            damage *= 2
            print(f"Critical hit!")
        damage = max(0, damage)  # Ensure damage isn't negative
        target.take_damage(damage)

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.element} character took {amount} damage!")
        if self.hp <= 0:
            print(f"{self.element} character has died!")

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hp += 5
        self.atk += 2
        self.defense += 1
        print(f"Level up! Now level {self.level}")

class Boss(Character):
    def __init__(self, x, y, element):
        super().__init__(x, y, element, level=5, hp=30, atk=10, defense=5)
        self.symbol = 'B'
    
    def special_attack(self, player):
        print(f"{self.element} boss uses a special attack!")
        # Boss deals massive damage to the player
        player.take_damage(self.atk * 2)

# Dungeon generation and interaction
class Dungeon:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [['#' for _ in range(width)] for _ in range(height)]
        self.player = None
        self.enemies = []
        self.boss = None
        self.exit = None

    def generate_map(self):
        # Generate random map with walls and floor
        for i in range(self.width):
            for j in range(self.height):
                if random.random() > 0.2:  # Open space for floor tiles
                    self.map[i][j] = TILES['FLOOR']

    def add_player(self):
        while True:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if self.map[x][y] == TILES['FLOOR']:
                self.player = Character(x, y, 'Player')
                self.map[x][y] = TILES['PLAYER']
                break

    def add_exit(self):
        while True:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if self.map[x][y] == TILES['FLOOR']:
                self.exit = (x, y)
                self.map[x][y] = TILES['EXIT']
                break

    def add_enemies(self, num_enemies):
        for _ in range(num_enemies):
            while True:
                x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
                if self.map[x][y] == TILES['FLOOR']:
                    element = random.choice(ELEMENTS)
                    enemy = Character(x, y, element, hp=8, atk=3)
                    self.enemies.append(enemy)
                    self.map[x][y] = TILES['ENEMY']
                    break

    def add_boss(self):
        while True:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if self.map[x][y] == TILES['FLOOR']:
                element = random.choice(ELEMENTS)
                self.boss = Boss(x, y, element)
                self.map[x][y] = TILES['BOSS']
                break

    def draw(self):
        for row in self.map:
            print(' '.join(row))
        print(f"Player HP: {self.player.hp}, Level: {self.player.level}, EXP: {self.player.exp}")

    def update_player_position(self, new_x, new_y):
        self.map[self.player.x][self.player.y] = TILES['FLOOR']
        self.player.x, self.player.y = new_x, new_y
        self.map[self.player.x][self.player.y] = TILES['PLAYER']

    def move_player(self, direction):
        dx, dy = DIRECTIONS[direction]
        new_x = self.player.x + dx
        new_y = self.player.y + dy

        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            tile = self.map[new_x][new_y]
            if tile == TILES['FLOOR']:
                self.update_player_position(new_x, new_y)
            elif tile == TILES['EXIT']:
                print("You reached the exit and win the game!")
            elif tile == TILES['ENEMY']:
                enemy = self.get_character_at(new_x, new_y, self.enemies)
                self.combat(enemy)
            elif tile == TILES['BOSS']:
                print("Boss battle begins!")
                self.boss.special_attack(self.player)
                self.combat(self.boss)

    def get_character_at(self, x, y, characters):
        for character in characters:
            if character.x == x and character.y == y:
                return character
        return None

    def combat(self, enemy):
        print(f"Combat with {enemy.element}!")
        # Simple combat: Player and enemy take turns to attack
        self.player.attack(enemy)
        if enemy.hp > 0:
            enemy.attack(self.player)
        if enemy.hp <= 0:
            print(f"You defeated the {enemy.element}!")
            self.player.gain_exp(10000000000000 * 1 / 2 * self.player.level)
            if isinstance(enemy, Boss):
                print("You defeated the boss! Game over!")
                exit(5)
            self.enemies.remove(enemy)
            self.map[enemy.x][enemy.y] = TILES['FLOOR']

# Main game loop
def main():
    dungeon = Dungeon(MAP_WIDTH, MAP_HEIGHT)
    dungeon.generate_map()
    dungeon.add_player()
    dungeon.add_exit()
    dungeon.add_enemies(100)
    dungeon.add_boss()

    print("Welcome to the Elemental Dungeon!")
    while dungeon.player.hp > 0:
        dungeon.draw()
        move = input("Move (up/down/left/right): ").lower()
        if move in DIRECTIONS:
            dungeon.move_player(move)
        else:
            print("Invalid move.")
        if dungeon.player.hp <= 0:
            print("Game over!")

if __name__ == "__main__":
    main()
    if __name__ == "__main__":
        main()