import random
try:
    combatStrength = int(input("Enter your combat Strength: "))
except TypeError as e:
    print("Combat strength must be an integer")
    
    
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

weaponRoll= random.randint(1,6)
print(f"Your weapon roll is {weaponRoll}")
print()
combatStrength+=weaponRoll

while True:
    try:
        weapon = weapons[weaponRoll]
        print(f"Your weapon is {weapon}.")
        if weaponRoll<=2:
            print("You rolled a weak weapon, friend")
        elif weaponRoll<=4:
            print("Your weapon is meh")
        else:
            print("Nice weapon, friend!")
        if weapon!="Fist":
            print("Thank goodness you didn't roll the Fist...")
        break
    except IndexError as e:
        print("Index out of range", e)
        continue