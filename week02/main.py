import random

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]

print("Elements:", elements)

#git add . && git commit -m "add elemnts array" && git push

def func_name():
    return True

def say_greeting(name, message):
    print(f"{message}, {name}")
    
say_greeting("Maziar", "hello")

def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("error: please enter the integer")
            continue


try:
    elements_selected = get_valid_int_input("Enter the index of the element you like: ")
    
    #roll dice
    elementRoll = random.randint(1, 6)
    totalNum = elements_selected+elementRoll
    
    #print the result based on the totalNum
    if elementRoll <=2:
        print("You rolled a weak element, friend.")
    elif elementRoll <=4:
        print("Your element is moderate")
    else:
        print("Nice element.")
except IndexError:
    print("Error: invalid element index!")   
except Exception as e:
    print(f"An unexpected error occured: {e}")