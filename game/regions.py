from game import elements

class Region:
    REGION_NAMES : dict[elements.Element, str] = {
        elements.Element.WATER: "Acquiria",
        elements.Element.LIGHT: "Aeonfall",
        elements.Element.SHADOW: "Voidmare",
        elements.Element.EARTH: "Tectrageon",
        elements.Element.CHAOS: "Limbo",
        elements.Element.WIND: "Evergale"
    }

    def __init__(self, element: elements.Element):
        self.name = self.REGION_NAMES[element]
        if not isinstance(element, elements.Element):
            raise ValueError("...")
        else:
            self.element = element
