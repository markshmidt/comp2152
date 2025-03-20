import random
from character import Character
from monster import Monster
class Hero:
    def __init__(self):
        super().__init__()
        self.combat_strength = random.randint(1, 6)
        self.health_points = random.randint(1, 20)

    def attacks(self, monster):
        def hero_attacks(combat_strength, m_health_points):
            ascii_image = """
                                        @@   @@ 
                                        @    @  
                                        @   @   
                       @@@@@@          @@  @    
                    @@       @@        @ @@     
                   @%         @     @@@ @       
                    @        @@     @@@@@     
                       @@@@@        @@       
                       @    @@@@                
                  @@@ @@                        
               @@     @                         
           @@*       @                          
           @        @@                          
                   @@                                                    
                 @   @@@@@@@                    
                @            @                  
              @              @                  

          """
            print(ascii_image)
            print(f"    |    Hero's attack ({self.combat_strength}) ---> Monster ({monster.health_points})")

            if self.combat_strength >= monster.health_points:
                monster.health_points = 0
                print("    |    You have killed the monster")
            else:
                monster.health_points -= self.combat_strength
                print(f"    |    You have reduced the monster's health to: {monster.health_points}")

            return monster.health_points

def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
