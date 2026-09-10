# The characters available in the selection pool
from game import elements
from game import archetypes


class Character:
    EXP_THRESHOLDS = [1000, 1750, 2500, 4000]
    
    PATH: dict[archetypes.Archetype, dict[str, int]] = { 
        archetypes.Archetype.DPS: {"health": 1100, "damage": 150},
        archetypes.Archetype.TANK : {"health": 1500, "damage": 100},
        archetypes.Archetype.RANGER: {"health": 900, "damage": 170},
        archetypes.Archetype.SUPPORT: {"health": 1000, "damage": 120}
    }
    
    GROWTH: dict[archetypes.Archetype,dict[str, int]] = {
        archetypes.Archetype.DPS: {'health': +10, 'damage': +15},
        archetypes.Archetype.TANK: {'health': +15, 'damage': +10},
        archetypes.Archetype.RANGER: {'health': +5, 'damage': +10},
        archetypes.Archetype.SUPPORT: {'health': +10, 'damage': +10}
    }
    
    def __init__(self, name, affinity: elements.Element, path: archetypes.Archetype, level=1, exp=0, health = None, damage = None):
        self.name = name
        if not isinstance(affinity, elements.Element):
            raise ValueError("...")
        else:
            self.affinity = affinity
        if not isinstance(path, archetypes.Archetype):
            raise ValueError('...')
        else:
            self.path = path
        self.level = level
        self.exp = exp
        if health is None:
            self.health = self.PATH[path]['health']
        else:
            self.health = health
        if damage is None:
            self.damage = self.PATH[path]['damage']
        else:
            self.damage = damage
        