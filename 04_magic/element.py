class Water:
    def __str__(self):
        return "Вода"

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Land):
            return Dirt()
        else:
            return None

class Air:
    def __str__(self):
        return 'Воздух'
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Land):
            return Dust()
        else:
            return None

class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Land):
            return Lava()
        elif isinstance(other, Lightning):
            return Fiery_lightning()
        else:
            return None

class Land:
    def __str__(self):
        return 'Земля'

class Storm:
    def __str__(self):
        return 'Шторм'

class Steam:
    def __str__(self):
        return 'Пар'

class Dirt:
    def __str__(self):
        return 'Грязь'

class Lightning:
    def __str__(self):
        return 'Молния'

class Dust:
    def __str__(self):
        return 'Пыль'

class Lava:
    def __str__(self):
        return 'Лава'

class Fiery_lightning:
    def __str__(self):
        return 'Огненная молния'
