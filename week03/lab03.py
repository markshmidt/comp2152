import random

# Dice options using list() and range()
diceOptions = list(range(1, 7))

# Weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']
print("Available Weapons:", ', '.join(weapons))

# Inputs combat strength hero
combatStrength = int(input("Enter your combat Strength (1-6): "))
if combatStrength<1 or combatStrength>6:
    print("Invalid input, combatStrength should be between 1 and 6. ")
    combatStrength=1 #default value

# Inputs combat strength hero
mCombatStrength = int(input("Enter monsters combat Strength (1-6): "))
if mCombatStrength<1 or mCombatStrength>6:
    print("Invalid input, monsters combatStrength should be between 1 and 6. ")
    mCombatStrength=1 #default value

#combatStrength = max(1, min(6, int(input("Hero strength (1-6): "))))
#mCombatStrength = max(1, min(6, int(input("Monster strength (1-6): "))))

# Battle
for j in range(1, 21, 2):#simulation od 20 rounds stepping by 2
    #dice rolls for hero and monster
    heroRoll, monsterRoll = random.choice(diceOptions), random.choice(diceOptions)
    
    # calculate the weapon
    heroWeapon, monsterWeapon = weapons[heroRoll - 1], weapons[monsterRoll - 1]
    
    # Calculate the total score
    heroTotal, monsterTotal = combatStrength+heroRoll, mCombatStrength+monsterRoll
    
    print(f"Round {j}: Hero rolled {heroRoll}, Monster rolled {monsterRoll}).", 
          f"Hero selected: {heroWeapon}, Monster Selected: {monsterWeapon}.",
          f"Hero total strength: {heroTotal}, Monster total strength: {monsterTotal}",
          "Hero wins!" if heroTotal > monsterTotal else "Monster wins!" if heroTotal < monsterTotal else "Tie!")
    if j == 11:
        print("Battle Truce declared in Round 11. Game Over!")
        break