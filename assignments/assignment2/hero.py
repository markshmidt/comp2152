import random
from character import Character
class Hero:
    def __init__(self):
        super().__init__()

    def hero_attacks(self, monster):
        print("Hero attacks Monster!")
        monster.health_points -= self.combat_strength
        print(f"Monster's health reduced to {monster.health_points}")

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")

    @property
    def combat_strength(self):
        return self.combat_strength

    @property
    def health_points(self):
        return self.health_points

    @combat_strength.setter
    def combat_strength(self, combat_strength):
        self._combat_strength = combat_strength

    @health_points.setter
    def health_points(self, health_points):
        self._health_points = health_points
