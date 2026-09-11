from enum import Enum
import elements
import random

class ZoneType(Enum):
    HOME = 1
    CAMP = 2
    CASTLE = 3

class Zone:
    CAMP_POOL : dict[elements.Element, dict[str, list]] = {
        elements.Element.LIGHT: {
            "Tier 1": [],
            "Tier 2": [],
            "Tier 3": []
        },
        elements.Element.SHADOW: {
            "Tier 1": [],
            "Tier 2": [],
            "Tier 3": []
        },
        elements.Element.WATER: {
            "Tier 1": [],
            "Tier 2": [],
            "Tier 3": []
        },
        elements.Element.WIND: {
            "Tier 1": [],
            "Tier 2": [],
            "Tier 3": []
        },
        elements.Element.EARTH: {
          "Tier 1": [],
          "Tier 2": [],
          "Tier 3": []  
        },
        elements.Element.CHAOS: {
            "Tier 1": [],
            "Tier 2": [],
            "Tier 3": []
        }
    }
        
    def __init__(self, name, zone_type, tier= None):
        self.name = name
        self.zone_type = zone_type
        self.tier = tier
    
    