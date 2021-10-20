import room

class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x, y, char, color, name, inventory, blocks=False, fighter=None, ai=None):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks
        self.fighter = fighter
        self.ai = ai
        self.inventory = inventory

        if self.fighter:
            self.fighter.owner = self

        if self.ai:
            self.ai.owner = self

class Warior:
    def __init__(self, hp, defense, power,mana):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
        self.mana = mana

class Mage:
    def __init__(self, hp, defense, power,mana):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
        self.mana = mana