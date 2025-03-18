import random
from character import Character
class Monster:
    def __init__(self):
        super().__init__()

    def monster_attacks(self, hero):
        print("Monster attacks Hero!")
        hero.health_points -= self.combat_strength
        print(f"Hero's health reduced to {hero.health_points}")

    def __del__(self):
        print('The Monster object is being destroyed by the garbage collector')