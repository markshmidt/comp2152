import random
class Character:
    def __init__(self):
        self._combat_strength = 1
        self._health_points = 1


    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        self._combat_strength = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if isinstance(value, int) and value >= 0:
            self._health_points = value
        else:
            raise ValueError("Health points must be a non-negative integer.")

    def __del__(self):
        print("Character object is being destroyed by the garbage collector")


