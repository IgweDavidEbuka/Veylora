from enum import Enum
import elements
import random

class ZoneType(Enum):
    HOME = 1
    CAMP = 2
    CASTLE = 3

class Zone:
    CAMP_POOL : dict[elements.Element, dict[int, list]] = {
        elements.Element.LIGHT: {
            1 : ["Elarion", "Phos Repostory", "Luminara"],
            2 : ["Krias", "Sunspire"],
            3 : ["Sanctum Aurum", "Elyndor"]
        },
        elements.Element.SHADOW: {
            1 : ["Duskwell", "Veyra", "Morevane"],
            2 : ["Blackreach", "Drazheil"],
            3 : ["Veynhaleth", "Zhaevor"]
        },
        elements.Element.WATER: {
            1 : ["Nerevia", "Ocevaris", "Thasslyr"],
            2 : ["The Sunken Ark", "Nerevia"],
            3 : ["Aetherian Trench", "Crystalline Cenotaph"]
        },
        elements.Element.WIND: {
            1 : ["Windreach", "Aereth", "Aeralis"],
            2 : ["Caelvyr", "Mount Avarra"],
            3 : ["Heaven's Crest", "Nimbus Stratum"]
        },
        elements.Element.EARTH: {
            1 : ["Aderra", "Durnak", "Eldara"],
            2 : ["Morundra", "Lithurila"],
            3 : ["Tectonic Tarbanacle", "Bedrock Vestige"]  
        },
        elements.Element.CHAOS: {
            1 : ["Zyrexhalitha", "Ezkara", "Veznaria"],
            2 : ["Vharaxis", "Orovex"],
            3 : ["Xaevoryn", "Xaltherian Pit"]
        }
    }
        
    def __init__(self, name, zone_type, tier= None):
        self.name = name
        self.zone_type = zone_type
        self.tier = tier
    
    def camp_randomizer(self, element):
        return random.choice(self.CAMP_POOL[element][random.randint(1, 3)])


se = Zone('', '')
print(se.camp_randomizer(elements.Element.CHAOS))