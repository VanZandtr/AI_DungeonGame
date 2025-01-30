import random

class Character:
    CLASSES = {
        "Warrior": {"hp": 25, "mana": 5, "attack": 7, "defense": 5, "skills": {1: "Power Strike", 5: "Cleave", 10: "Whirlwind", 15: "Earth Shatter"}},
        "Mage": {"hp": 15, "mana": 20, "attack": 5, "defense": 3, "skills": {1: "Fireball", 5: "Lightning Bolt", 10: "Ice Storm", 15: "Meteor Strike"}},
        "Rogue": {"hp": 18, "mana": 10, "attack": 6, "defense": 4, "skills": {1: "Backstab", 5: "Shadow Strike", 10: "Poison Blade", 15: "Death Mark"}},
        "Cleric": {"hp": 20, "mana": 15, "attack": 4, "defense": 6, "skills": {1: "Heal", 5: "Greater Heal", 10: "Divine Smite", 15: "Holy Wrath"}},
        "Paladin": {"hp": 22, "mana": 12, "attack": 6, "defense": 6, "skills": {1: "Smite", 5: "Blessed Hammer", 10: "Retribution", 15: "Judgment"}}
    }
    
    def __init__(self, name, char_class):
        stats = self.CLASSES[char_class]
        self.name = name
        self.char_class = char_class
        self.hp = stats["hp"]
        self.mana = stats["mana"]
        self.attack = stats["attack"]
        self.defense = stats["defense"]
        self.skills = stats["skills"]
        self.xp = 0
        self.level = 1
        self.equipment = []
    
    def equip(self, item):
        self.equipment.append(item)
        self.attack += item.attack_bonus
        self.defense += item.defense_bonus
    
    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 10:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.hp += 5
        self.mana += 3
        self.attack += 2
        self.defense += 2
        self.xp = 0
        if self.level in self.skills:
            print(f"{self.name} leveled up to {self.level} and learned {self.skills[self.level]}!")

class Maze:
    ROOM_TYPES = {"empty": ".", "battle": "B", "heal": "H", "stairs": "S"}
    
    def __init__(self, layers=4):
        self.layers = layers
        self.current_layer = 0
        self.rooms = self.generate_maze()
        self.player_pos = random.choice(list(self.rooms.keys()))
    
    def generate_maze(self):
        num_rooms = random.randint(15, 20)
        rooms = {}
        for _ in range(num_rooms - 1):
            rooms[(random.randint(0, 4), random.randint(0, 4))] = random.choice(list(self.ROOM_TYPES.keys())[:-1])
        stairs_pos = random.choice(list(rooms.keys()))
        rooms[stairs_pos] = "stairs"
        return rooms
    
    def print_maze(self):
        for i in range(5):
            row = ""
            for j in range(5):
                if (i, j) == self.player_pos:
                    row += " P "
                elif (i, j) in self.rooms:
                    row += f" {self.ROOM_TYPES[self.rooms[(i, j)]]} "
                else:
                    row += "   "
            print(row)
        print()
    
    def move(self, direction):
        x, y = self.player_pos
        if direction == "quit":
            print("Game over. Thanks for playing!")
            exit()
        elif direction == "legend":
            print("Legend: P = Player, . = Empty, B = Battle, H = Heal, S = Stairs")
            return
        
        new_pos = {
            "n": (x-1, y),
            "s": (x+1, y),
            "e": (x, y+1),
            "w": (x, y-1)
        }.get(direction, self.player_pos)
        
        if new_pos in self.rooms:
            self.player_pos = new_pos
            self.print_maze()
            print(f"You entered a {self.rooms[new_pos]} room.")
        else:
            print("You can't move that way!")

def game_loop():
    print("Choose your class:")
    for cls, stats in Character.CLASSES.items():
        print(f"{cls}: HP {stats['hp']}, Mana {stats['mana']}, Attack {stats['attack']}, Defense {stats['defense']}, Skills: {stats['skills']}")
    
    chosen_class = ""
    while chosen_class not in Character.CLASSES:
        chosen_class = input("Enter class name: ")
    
    name = input("Enter your character's name: ")
    global player
    player = Character(name, chosen_class)
    
    maze = Maze()
    maze.print_maze()
    
    while player.hp > 0:
        move = input("Move (n, s, e, w, legend, quit): ").lower()
        maze.move(move)

game_loop()