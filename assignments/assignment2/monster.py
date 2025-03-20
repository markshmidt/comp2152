import random
from character import Character
class Monster:
    def __init__(self):
        super().__init__()
        self.combat_strength = random.randint(1, 6)
        self.health_points = random.randint(1, 20)

    def attacks(self, hero):
        ascii_image2 = """                                                                 
               @@@@ @                           
          (     @*&@  ,                         
        @               %                       
         &#(@(@%@@@@@*   /                      
          @@@@@.                                
                   @       /                    
                    %         @                 
                ,(@(*/           %              
                   @ (  .@#                 @   
                              @           .@@. @
                       @         ,              
                          @       @ .@          
                                 @              
                              *(*  *      
                 """
        print(ascii_image2)
        print(f"    |    Monster's Claw ({self.combat_strength}) ---> Player ({hero.health_points})")

        if self.combat_strength >= hero.health_points:
            hero.health_points = 0
            print("    |    Player is dead")
        else:
            hero.health_points -= self.combat_strength
            print(f"    |    The monster has reduced Player's health to: {hero.health_points}")

        return hero.health_points

def __del__(self):
        print('The Monster object is being destroyed by the garbage collector')
        super().__del__()