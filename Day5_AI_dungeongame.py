import random
import json
import os

class Items:
    RARITIES = {
        "Common": 0.6,
        "Rare": 0.3,
        "Epic": 0.1
    }
    
    POTIONS = {
        "Health": {
            "Common": {"heal": 10},
            "Rare": {"heal": 25},
            "Epic": {"heal": 50}
        },
        "Mana": {
            "Common": {"restore": 10},
            "Rare": {"restore": 25},
            "Epic": {"restore": 50}
        }
    }
    
    def __init__(self, name, item_type, rarity):
        self.name = f"{rarity} {name} Potion"
        self.type = item_type
        self.rarity = rarity
        self.effect = self.POTIONS[item_type][rarity]

class Equipment:
    EQUIPMENT_TYPES = {
        "Weapon": {
            "Rusty Sword": {"attack": 2},
            "Steel Sword": {"attack": 5},
            "Magical Blade": {"attack": 8},
            "Legendary Sword": {"attack": 12}
        },
        "Armor": {
            "Leather Armor": {"defense": 2},
            "Chain Mail": {"defense": 5},
            "Plate Armor": {"defense": 8},
            "Enchanted Armor": {"defense": 10}
        }
    }
    
    def __init__(self, name, eq_type):
        self.name = name
        self.type = eq_type
        self.stats = self.EQUIPMENT_TYPES[eq_type][name]
class Pet:
    PET_TYPES = {
        "Mystic Cat": {
            "max_hp": 8,
            "attack": 3,
            "defense": 2,
            "passive_bonus": {"mana": 5},  # Increases player's max mana
            "description": "A mysterious feline with glowing eyes that enhances magical abilities"
        },
        "Spirit Wolf": {
            "max_hp": 10,
            "attack": 4,
            "defense": 1,
            "passive_bonus": {"attack": 2},  # Increases player's attack
            "description": "A loyal spectral wolf that strengthens its master's attacks"
        }
    }
    
    def __init__(self, name):
        self.name = name
        stats = self.PET_TYPES[name]
        self.max_hp = stats["max_hp"]
        self.current_hp = self.max_hp
        self.attack = stats["attack"]
        self.defense = stats["defense"]
        self.passive_bonus = stats["passive_bonus"]
        self.description = stats["description"]

class Character:
    
    CLASSES = {
        "Warrior": {"hp": 30, "mana": 10, "attack": 8, "defense": 6, "skills": {
            1: {"name": "Power Strike", "damage": 12, "mana_cost": 5},
            5: {"name": "Cleave", "damage": 15, "mana_cost": 8},
            10: {"name": "Whirlwind", "damage": 20, "mana_cost": 12},
            15: {"name": "Earth Shatter", "damage": 25, "mana_cost": 15}
        }},
        "Mage": {"hp": 20, "mana": 25, "attack": 5, "defense": 3, "skills": {
            1: {"name": "Fireball", "damage": 10, "mana_cost": 6},
            5: {"name": "Lightning Bolt", "damage": 15, "mana_cost": 10},
            10: {"name": "Ice Storm", "damage": 20, "mana_cost": 14},
            15: {"name": "Meteor Strike", "damage": 30, "mana_cost": 20}
        }},
        "Rogue": {"hp": 22, "mana": 15, "attack": 7, "defense": 4, "skills": {
            1: {"name": "Backstab", "damage": 11, "mana_cost": 5},
            5: {"name": "Shadow Strike", "damage": 16, "mana_cost": 8},
            10: {"name": "Poison Blade", "damage": 18, "mana_cost": 12},
            15: {"name": "Death Mark", "damage": 25, "mana_cost": 15}
        }},
        "Cleric": {"hp": 25, "mana": 20, "attack": 5, "defense": 5, "skills": {
            1: {"name": "Heal", "healing": 10, "mana_cost": 5},
            5: {"name": "Greater Heal", "healing": 15, "mana_cost": 10},
            10: {"name": "Divine Smite", "damage": 15, "mana_cost": 12},
            15: {"name": "Holy Wrath", "damage": 25, "mana_cost": 15}
        }}
    }
    
    def __init__(self, name, char_class):
        stats = self.CLASSES[char_class]
        self.name = name
        self.char_class = char_class
        self.max_hp = stats["hp"]
        self.current_hp = stats["hp"]  # Changed from hp to current_hp
        self.max_mana = stats["mana"]
        self.current_mana = stats["mana"]  # Changed from mana to current_mana
        self.attack = stats["attack"]
        self.defense = stats["defense"]
        self.skills = stats["skills"]
        self.xp = 0
        self.level = 1
        self.inventory = []
        self.equipped = {"Weapon": None, "Armor": None}
        self.pet = None  # Add this line

    def to_dict(self):
        return {
            'name': self.name,
            'char_class': self.char_class,
            'current_hp': self.current_hp,
            'max_hp': self.max_hp,
            'current_mana': self.current_mana,
            'max_mana': self.max_mana,
            'attack': self.attack,
            'defense': self.defense,
            'xp': self.xp,
            'level': self.level,
            'inventory': [{'name': item.name, 'type': item.type, 'rarity': item.rarity if hasattr(item, 'rarity') else None, 
                          'stats': item.stats if hasattr(item, 'stats') else None,
                          'effect': item.effect if hasattr(item, 'effect') else None} for item in self.inventory],
            'equipped': {slot: {'name': item.name, 'type': item.type, 'stats': item.stats} if item else None 
                        for slot, item in self.equipped.items()},
            'pet': {
                'name': self.pet.name,
                'current_hp': self.pet.current_hp,
                'max_hp': self.pet.max_hp,
                'attack': self.pet.attack,
                'defense': self.pet.defense
            } if self.pet else None
        }

    @classmethod
    def from_dict(cls, data):
        character = cls(data['name'], data['char_class'])
        character.current_hp = data['current_hp']
        character.max_hp = data['max_hp']
        character.current_mana = data['current_mana']
        character.max_mana = data['max_mana']
        character.attack = data['attack']
        character.defense = data['defense']
        character.xp = data['xp']
        character.level = data['level']
        
        character.inventory = []
        for item_data in data['inventory']:
            if 'rarity' in item_data and item_data['rarity']:
                item = Items(item_data['name'].split()[-2], item_data['type'], item_data['rarity'])
            else:
                item = Equipment(item_data['name'], item_data['type'])
            character.inventory.append(item)
        
        character.equipped = {slot: Equipment(item_data['name'], item_data['type']) if item_data else None 
                            for slot, item_data in data['equipped'].items()}
        if data.get('pet'):
            character.pet = Pet(data['pet']['name'])
            character.pet.current_hp = data['pet']['current_hp']
        return character
    
    def add_pet(self, pet):
        if self.pet is None:
            self.pet = pet
            # Apply passive bonuses
            if "mana" in pet.passive_bonus:
                self.max_mana += pet.passive_bonus["mana"]
                self.current_mana += pet.passive_bonus["mana"]
            if "attack" in pet.passive_bonus:
                self.attack += pet.passive_bonus["attack"]
            print(f"You gained a {pet.name}!")
            print(f"Pet description: {pet.description}")
        else:
            print("You already have a pet!")
    
    # 3. Add method to remove pet's passive bonuses when knocked out
    def update_pet_status(self):
        if self.pet and self.pet.current_hp <= 0:
            # Remove passive bonuses temporarily
            if "mana" in self.pet.passive_bonus:
                self.max_mana -= self.pet.passive_bonus["mana"]
                self.current_mana = min(self.current_mana, self.max_mana)
            if "attack" in self.pet.passive_bonus:
                self.attack -= self.pet.passive_bonus["attack"]
            print(f"Your {self.pet.name}'s bonuses are inactive while it's knocked out!")

    # 4. Add method to restore pet's passive bonuses when healed
    def restore_pet_bonuses(self):
        if self.pet and self.pet.current_hp > 0:
            if "mana" in self.pet.passive_bonus:
                self.max_mana += self.pet.passive_bonus["mana"]
            if "attack" in self.pet.passive_bonus:
                self.attack += self.pet.passive_bonus["attack"]
            print(f"Your {self.pet.name}'s bonuses have been restored!")
    
    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty!")
            return

        print("\nInventory:")
        for idx, item in enumerate(self.inventory, 1):
            if isinstance(item, Equipment):
                stats = next(iter(item.stats.items()))
                print(f"{idx}. {item.name} ({stats[0]}: +{stats[1]})")
            else:
                print(f"{idx}. {item.name}")

        item_choice = input("\nSelect item to use/equip (number) or 'c' to cancel: ")
        if item_choice.lower() == 'c':
            return

        try:
            item_idx = int(item_choice) - 1
            if 0 <= item_idx < len(self.inventory):
                item = self.inventory[item_idx]
                
                if isinstance(item, Equipment):
                    old_item = self.equip(item)
                    self.inventory.remove(item)
                    if old_item:
                        self.inventory.append(old_item)
                    print(f"Equipped {item.name}")
                elif isinstance(item, Items):
                    if self.use_potion(item):
                        print(f"Used {item.name}")
            else:
                print("Invalid selection!")
        except ValueError:
            print("Invalid selection!")
    
    def show_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Class: {self.char_class}")
        print(f"Level: {self.level}")
        print(f"HP: {self.current_hp}/{self.max_hp}")
        print(f"Mana: {self.current_mana}/{self.max_mana}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"XP: {self.xp}/{self.level * 10}")

        print("\nEquipped:")
        for slot, item in self.equipped.items():
            print(f"{slot}: {item.name if item else 'None'}")
        
        if self.pet:
            print(f"\nPet: {self.pet.name}")
            print(f"Pet HP: {self.pet.current_hp}/{self.pet.max_hp}")
            print(f"Pet Attack: {self.pet.attack}")
            print(f"Pet Defense: {self.pet.defense}")
    
    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 10:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.max_hp += 5
        lost_hp = self.max_hp - self.current_hp
        self.current_hp = self.max_hp - (lost_hp // 2)  # Restore 50% of lost health
        
        self.max_mana += 3
        lost_mana = self.max_mana - self.current_mana
        self.current_mana = self.max_mana - (lost_mana // 2)  # Restore 50% of lost mana
        
        self.attack += 2
        self.defense += 2
        self.xp = 0
        print(f"{self.name} leveled up to {self.level}!")
        if self.level in self.skills:
            print(f"Learned new skill: {self.skills[self.level]['name']}!")
    
    def equip(self, item):
        if item.type in ["Weapon", "Armor"]:
            old_item = self.equipped[item.type]
            self.equipped[item.type] = item
            
            # Adjust stats based on equipment
            if item.type == "Weapon":
                self.attack += item.stats["attack"]
                if old_item:
                    self.attack -= old_item.stats["attack"]
            elif item.type == "Armor":
                self.defense += item.stats["defense"]
                if old_item:
                    self.defense -= old_item.stats["defense"]
            
            return old_item
        return None
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
    
    def use_skill(self, skill_level):
        if skill_level in self.skills:
            skill = self.skills[skill_level]
            if self.current_mana >= skill["mana_cost"]:
                self.current_mana -= skill["mana_cost"]
                return skill
        return None
    
    # 2. Add pet healing functionality to potion usage
    def use_potion(self, potion):
        if potion.type == "Health":
            self.current_hp = min(self.max_hp, self.current_hp + potion.effect["heal"])
            # Add pet healing - heal for 50% of potion value
            if self.pet and self.pet.current_hp > 0:
                pet_heal = potion.effect["heal"] // 2
                self.pet.current_hp = min(self.pet.max_hp, self.pet.current_hp + pet_heal)
                print(f"Your {self.pet.name} was healed for {pet_heal} HP!")
        elif potion.type == "Mana":
            self.current_mana = min(self.max_mana, self.current_mana + potion.effect["restore"])
        self.inventory.remove(potion)
        return True

class Monster:
    MONSTER_TYPES = {
        "Goblin": {"hp": 15, "attack": 4, "defense": 2, "xp_reward": 10, "drop_chance": 0.3},
        "Skeleton": {"hp": 20, "attack": 5, "defense": 3, "xp_reward": 15, "drop_chance": 0.4},
        "Orc": {"hp": 25, "attack": 6, "defense": 4, "xp_reward": 20, "drop_chance": 0.5},
        "Troll": {"hp": 35, "attack": 7, "defense": 5, "xp_reward": 30, "drop_chance": 0.6},
        "Dragon": {"hp": 50, "attack": 10, "defense": 8, "xp_reward": 50, "drop_chance": 1.0},
    }
    
    
    # 1. Fix Monster class pet drop generation by adding player reference
    def __init__(self, name, difficulty_multiplier, player):  # Add player parameter
        stats = self.MONSTER_TYPES[name].copy()
        if name not in ["Troll", "Dragon"]:
            difficulty_multiplier = 1 + (difficulty_multiplier * 0.05)
        
        stats["hp"] *= difficulty_multiplier
        stats["attack"] *= difficulty_multiplier
        stats["defense"] *= difficulty_multiplier
        stats["xp_reward"] *= difficulty_multiplier
        
        self.name = name
        self.max_hp = int(stats["hp"])
        self.current_hp = self.max_hp
        self.attack = int(stats["attack"])
        self.defense = int(stats["defense"])
        self.xp_reward = int(stats["xp_reward"])
        self.drop_chance = stats["drop_chance"]
        self.pet_drop_chance = 0.05 if name in ["Troll", "Dragon"] else 0.02
        self.player = player  # Store player reference
    
    def generate_drop(self):
        if random.random() < self.drop_chance:
            # Check for pet drop first
            if self.pet_drop_chance > random.random() and not self.player.pet:
                pet_type = random.choice(list(Pet.PET_TYPES.keys()))
                return Pet(pet_type)

            # Determine item type
            item_type = random.choice(["Health", "Mana"])
            
            # Determine rarity
            rarity_roll = random.random()
            if rarity_roll < Items.RARITIES["Common"]:
                rarity = "Common"
            elif rarity_roll < Items.RARITIES["Common"] + Items.RARITIES["Rare"]:
                rarity = "Rare"
            else:
                rarity = "Epic"
            
            return Items(item_type, item_type, rarity)
        return None

class Maze:
    ROOM_TYPES = {"empty": ".", "battle": "B", "heal": "H", "stairs": "S", "boss": "X"}
    
    def __init__(self, player, layers=4, width=7, height=6):
        self.player = player
        self.layers = layers
        self.current_layer = 0
        self.width = width
        self.height = height
        self.explored_rooms = set()
        self.visited_rooms = set()
        self.boss_room = None  # Track boss room location
        self.generate_valid_maze()
    
    def to_dict(self):
        return {
            'layers': self.layers,
            'current_layer': self.current_layer,
            'width': self.width,
            'height': self.height,
            'rooms': {f"{k[0]},{k[1]}": v for k, v in self.rooms.items()},
            'player_pos': self.player_pos,
            'boss_room': self.boss_room,
            'stairs_pos': self.stairs_pos if hasattr(self, 'stairs_pos') else None,
            'explored_rooms': list(self.explored_rooms),
            'visited_rooms': list(self.visited_rooms)
        }

    @classmethod
    def from_dict(cls, data, player):
        maze = cls(player, data['layers'], data['width'], data['height'])
        maze.current_layer = data['current_layer']
        maze.rooms = {tuple(map(int, k.split(','))): v for k, v in data['rooms'].items()}
        maze.player_pos = tuple(data['player_pos'])
        maze.boss_room = tuple(data['boss_room']) if data['boss_room'] else None
        maze.stairs_pos = tuple(data['stairs_pos']) if data['stairs_pos'] else None
        maze.explored_rooms = set(map(tuple, data['explored_rooms']))
        maze.visited_rooms = set(map(tuple, data['visited_rooms']))
        return maze

    
    def generate_valid_maze(self):
        self.rooms = {}
        self.explored_rooms.clear()
        self.visited_rooms.clear()
        
        for x in range(self.width):
            for y in range(self.height):
                if random.random() < 0.8:
                    room_type = random.choices(
                        ["battle", "heal", "empty"], 
                        weights=[0.4, 0.1, 0.5]
                    )[0]
                    self.rooms[(x, y)] = room_type
        
        start_pos = (random.randint(0, self.width-1), random.randint(0, self.height-1))
        self.player_pos = start_pos
        self.visited_rooms.add(start_pos)
        
        available_positions = list(self.rooms.keys())
        if available_positions:
            self.boss_room = random.choice(available_positions)
            self.rooms[self.boss_room] = "boss"
            available_positions.remove(self.boss_room)
        
        if self.current_layer < self.layers - 1 and available_positions:
            stairs_pos = random.choice(available_positions)
            self.rooms[stairs_pos] = "stairs"
            self.stairs_pos = stairs_pos

    def print_maze(self):
        print("\n--- Current Dungeon Map ---")
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if (x, y) == self.player_pos:
                    row += " P "
                elif (x, y) in self.rooms:
                    room_type = self.rooms[(x, y)]
                    row += f" {self.ROOM_TYPES[room_type]} "
                else:
                    row += "   "
            print(row)
        print()

    def move(self, direction):
        self.print_maze()
        
        if direction == "status":
            self.player.show_status()
            return
        if direction == "inventory" or direction == "i":
            self.player.show_inventory()
            return
        if direction == "map":
            return
        if direction == "quit":
            print("Game over. Thanks for playing!")
            exit()
        elif direction == "legend":
            print("Legend: P = Player, . = Explored, ? = Unexplored, B = Battle, H = Heal, S = Stairs, X = Boss")
            return
        
        x, y = self.player_pos
        moves = {
            "n": (x, y-1), 
            "s": (x, y+1), 
            "e": (x+1, y), 
            "w": (x-1, y)
        }
        
        new_pos = moves.get(direction, self.player_pos)
        
        if (0 <= new_pos[0] < self.width and 0 <= new_pos[1] < self.height and 
            new_pos in self.rooms):
            self.player_pos = new_pos
            self.visited_rooms.add(new_pos)
            self.explored_rooms.add(new_pos)
            
            if new_pos == self.stairs_pos and len(self.explored_rooms) < len(self.rooms):
                print("The stairs are locked! You must explore all rooms first.")
                return

            room_type = self.rooms[new_pos]
            self.rooms[new_pos] = "empty"
            self.enter_room(room_type)

            #self.print_maze()
    
    def enter_room(self, room_type):
        if room_type == "stairs" and len(self.explored_rooms) == len(self.rooms):
            print("All rooms explored! Stairs unlocked!")
            print("Moving to the next floor...")
            self.current_layer += 1
            self.generate_valid_maze()
        
        if room_type == "battle":
            self.battle()
        elif room_type == "heal":
            print("You found a healing room! Restoring HP and Mana.")
            self.player.current_hp = min(self.player.current_hp + 10, self.player.max_hp)
            self.player.current_mana = min(self.player.current_mana + 5, self.player.max_mana)
        elif room_type == "boss":
            print("A BOSS APPEARS!")
            self.battle(is_boss=True)
    
    def battle(self, is_boss=False):
        difficulty_multiplier = 1 + (self.current_layer * 0.1)
        
        if is_boss:
            if self.current_layer == self.layers - 1:
                enemy = Monster("Dragon", difficulty_multiplier * 1.2, self.player)
            else:
                enemy = Monster("Troll", difficulty_multiplier, self.player)
        else:
            monster_types = ["Goblin", "Skeleton", "Orc"]
            enemy = Monster(random.choice(monster_types), difficulty_multiplier, self.player)
        
        print(f"You are fighting {enemy.name}!")
        
        battle_hp = self.player.current_hp
        battle_mana = self.player.current_mana
        
        while battle_hp > 0 and enemy.current_hp > 0:
            print(f"\n{self.player.name}: HP {battle_hp}/{self.player.max_hp}, Mana {battle_mana}/{self.player.max_mana}")
            if self.player.pet:
                status = "Ready" if self.player.pet.current_hp > 0 else "Knocked Out"
                print(f"Pet {self.player.pet.name}: HP {self.player.pet.current_hp}/{self.player.pet.max_hp} ({status})")
            print(f"{enemy.name}: HP {enemy.current_hp}/{enemy.max_hp}")
            
            # Add command help
            print("\nCommands: (a)ttack, (s)kill, (p)otion, (i)nventory, (r)un")
            action = input("What will you do? ").lower()
            
            if action == "p":
                potions = [item for item in self.player.inventory if isinstance(item, Items)]
                if not potions:
                    print("No potions in inventory!")
                    continue
                
                print("\nAvailable Potions:")
                for idx, potion in enumerate(potions, 1):
                    print(f"{idx}. {potion.name}")
                    if potion.type == "Health":
                        print(f"   Heals you for {potion.effect['heal']} HP")
                        if self.player.pet:
                            print(f"   Heals pet for {potion.effect['heal']//2} HP")
                    else:
                        print(f"   Restores {potion.effect['restore']} Mana")
                
                choice = input("\nSelect potion (number) or cancel (c): ")
                if choice.lower() == 'c':
                    continue
                
                try:
                    potion_idx = int(choice) - 1
                    if 0 <= potion_idx < len(potions):
                        potion = potions[potion_idx]
                        was_pet_knocked_out = self.player.pet and self.player.pet.current_hp <= 0
                        
                        if potion.type == "Health":
                            battle_hp = min(self.player.max_hp, battle_hp + potion.effect["heal"])
                            if self.player.pet:
                                pet_heal = potion.effect["heal"] // 2
                                self.player.pet.current_hp = min(self.player.pet.max_hp, 
                                                               self.player.pet.current_hp + pet_heal)
                                print(f"Your {self.player.pet.name} was healed for {pet_heal} HP!")
                                
                                # Check if pet was revived
                                if was_pet_knocked_out and self.player.pet.current_hp > 0:
                                    self.player.restore_pet_bonuses()
                        
                        elif potion.type == "Mana":
                            battle_mana = min(self.player.max_mana, battle_mana + potion.effect["restore"])
                        
                        self.player.inventory.remove(potion)
                        print(f"Used {potion.name}")
                    else:
                        print("Invalid selection!")
                except ValueError:
                    print("Invalid selection!")
                    continue
            
            if action == "a":
                # Player attack
                damage = max(1, self.player.attack - enemy.defense + random.randint(-2, 2))
                enemy.current_hp -= damage
                print(f"You dealt {damage} damage!")
                
                # Pet attack if alive
                if self.player.pet and self.player.pet.current_hp > 0:
                    pet_damage = max(1, self.player.pet.attack - enemy.defense + random.randint(-1, 1))
                    enemy.current_hp -= pet_damage
                    print(f"Your {self.player.pet.name} dealt {pet_damage} damage!")
            elif action == "s":
                print("Available Skills:")
                for level, skill in self.player.skills.items():
                    if level <= self.player.level:
                        print(f"{skill['name']} (Level {level}, Mana Cost: {skill.get('mana_cost', 0)})")
                skill_input = input("Choose a skill level: ")
                try:
                    skill_level = int(skill_input)
                    if skill_level in self.player.skills and battle_mana >= self.player.skills[skill_level]["mana_cost"]:
                        skill = self.player.skills[skill_level]
                        battle_mana -= skill["mana_cost"]
                        if "damage" in skill:
                            enemy.current_hp -= skill["damage"]
                            print(f"You used {skill['name']} and dealt {skill['damage']} damage!")
                        elif "healing" in skill:
                            battle_hp = min(self.player.max_hp, battle_hp + skill["healing"])
                            print(f"You used {skill['name']} and healed {skill['healing']} HP!")
                    else:
                        print("Invalid skill or not enough mana!")
                        continue
                except ValueError:
                    print("Invalid skill selection!")
                    continue
                    
            elif action == "i":
                if not self.player.inventory:
                    print("Your inventory is empty!")
                    continue
                
                print("\nInventory:")
                for idx, item in enumerate(self.player.inventory, 1):
                    if isinstance(item, Equipment):
                        stats = next(iter(item.stats.items()))
                        print(f"{idx}. {item.name} ({stats[0]}: +{stats[1]})")
                    else:
                        print(f"{idx}. {item.name}")

                item_choice = input("\nSelect item to use/equip (number) or 'c' to cancel: ")
                if item_choice.lower() == 'c':
                    continue

                try:
                    item_idx = int(item_choice) - 1
                    if 0 <= item_idx < len(self.player.inventory):
                        item = self.player.inventory[item_idx]
                        
                        if isinstance(item, Equipment):
                            old_item = self.player.equip(item)
                            self.player.inventory.remove(item)
                            if old_item:
                                self.player.inventory.append(old_item)
                            print(f"Equipped {item.name}")
                        elif isinstance(item, Items):
                            if item.type == "Health":
                                battle_hp = min(self.player.max_hp, battle_hp + item.effect["heal"])
                            elif item.type == "Mana":
                                battle_mana = min(self.player.max_mana, battle_mana + item.effect["restore"])
                            self.player.inventory.remove(item)
                            print(f"Used {item.name}")
                            potion_used = True
                    else:
                        print("Invalid selection!")
                except ValueError:
                    print("Invalid selection!")
                    continue
            elif action == "r":
                if random.random() < 0.5:
                    print("You successfully ran away!")
                    self.player.current_hp = battle_hp  # Update player HP before running
                    self.player.current_mana = battle_mana  # Update player mana before running
                    return
                else:
                    print("Failed to run away!")
            
            if enemy.current_hp > 0:
                # Enemy attacks player
                damage = max(1, enemy.attack - self.player.defense + random.randint(-1, 1))
                battle_hp -= damage
                print(f"{enemy.name} dealt {damage} damage to you!")
                
                # Enemy might attack pet
                if self.player.pet and self.player.pet.current_hp > 0 and random.random() < 0.3:  # 30% chance to attack pet
                    pet_damage = max(1, enemy.attack - self.player.pet.defense + random.randint(-1, 1))
                    self.player.pet.current_hp -= pet_damage
                    print(f"{enemy.name} dealt {pet_damage} damage to your {self.player.pet.name}!")
                    # When pet gets knocked out during battle
                    if self.player.pet and self.player.pet.current_hp <= 0:
                        self.player.update_pet_status()
                        print(f"Your {self.player.pet.name} was knocked out!")
                        
            if battle_hp <= 0:
                self.player.current_hp = 0
                print("Game Over! You were defeated.")
                exit()
            # Persist battle results to player
            self.player.current_hp = battle_hp
            self.player.current_mana = battle_mana
        
        if enemy.current_hp <= 0:
            print(f"You defeated {enemy.name}!")
            xp_gained = max(5, enemy.xp_reward - (self.current_layer * 2))
            self.player.gain_xp(xp_gained)
            
            xp_gained = max(5, enemy.xp_reward - (self.current_layer * 2))
            self.player.gain_xp(xp_gained)
            
            if random.random() < 0.5:
                eq_types = list(Equipment.EQUIPMENT_TYPES.keys())
                eq_type = random.choice(eq_types)
                eq_names = list(Equipment.EQUIPMENT_TYPES[eq_type].keys())
                eq_name = random.choice(eq_names)
                equipment = Equipment(eq_name, eq_type)
                print(f"You found: {equipment.name}")
                self.player.add_to_inventory(equipment)
            
            drop = enemy.generate_drop()
            if isinstance(drop, Pet):
                self.player.add_pet(drop)
            elif drop:
                print(f"You found: {drop.name}")
                self.player.add_to_inventory(drop)


def save_game(player, maze, filename='savegame.txt'):
    save_data = {
        'player': player.to_dict(),
        'maze': maze.to_dict(),
        'version': '1.1'  # Add version tracking
    }
    try:
        with open(filename, 'w') as f:
            json.dump(save_data, f)
        print("Game saved successfully!")
    except Exception as e:
        print(f"Error saving game: {e}")

# 7. Add better error handling to load game function
def load_game(filename='savegame.txt'):
    if not os.path.exists(filename):
        print("No save file found.")
        return None, None
    
    try:
        with open(filename, 'r') as f:
            save_data = json.load(f)
        
        # Version check for future compatibility
        if 'version' not in save_data:
            print("Warning: Loading legacy save file")
            
        player = Character.from_dict(save_data['player'])
        maze = Maze.from_dict(save_data['maze'], player)
        return player, maze
    except Exception as e:
        print(f"Error loading save file: {e}")
        return None, None


def create_new_game():
    print("Choose your class:")
    for cls, stats in Character.CLASSES.items():
        print(f"{cls}: HP {stats['hp']}, Mana {stats['mana']}, Attack {stats['attack']}, Defense {stats['defense']}")
    
    chosen_class = ""
    while chosen_class not in Character.CLASSES:
        chosen_class = input("Enter class name: ")
    
    name = input("Enter your character's name: ")
    player = Character(name, chosen_class)
    maze = Maze(player)
    return player, maze

def game_loop():
    print(r"""

"You awaken in a place long forgotten. 
The stone walls breathe with unseen life, whispering secrets of those who came before.
Darkness coils in the corners, hiding creatures that hunger for your presence.
A single path lies ahead.

Will you conquer the dungeon… or become part of its legend?"
""")
    
    if os.path.exists('savegame.txt'):
        load_choice = input("Load saved game? (y/n): ").lower()
        if load_choice == 'y':
            player, maze = load_game()
            if player and maze:
                print(f"Welcome back, {player.name}!")
            else:
                print("Failed to load save. Starting new game...")
                player, maze = create_new_game()
        else:
            player, maze = create_new_game()
    else:
        player, maze = create_new_game()

    maze.print_maze()
    while player.current_hp > 0:
        command = input("Move (n, s, e, w, inventory/i, status, save, legend, quit): ").lower()
        if command == 'save':
            save_game(player, maze)
        else:
            maze.move(command)

game_loop()