import random
import time


# Text based boxing game by f1nesse13:

while True: # Asks for players name and checks if valid.
    player =  input("Please enter your boxer's name: ")
    if (player.isalpha()):
        print("Ok " + player + " let's see who your coming up against tonight...")
        break
    elif (player.isalpha() and player.isspace() for i in player):
        print("Ok " + player + " let's see who your coming up against tonight...")
        break
    else:
         print('Invalid name! No numbers or symbols please.')
# Picks a opponent
opponent_list = ["Monty \'The Python \' Williams", "Joe \'The Schmoe\' Mcdoughan", "Jay \'The Kay\' Joking", "Rob \'LMAO U LOSE\' Johnson", "Donald \'MAGA\' Trump", "FooBar Reynolds" ]

opponent = random.choice(opponent_list)

print(str("Ok " + player + " your opponent tonight will be " + opponent))
time.sleep(3)

print("RING RING RING".center(75,":"))
print("RING RING RING".center(75,":"))
time.sleep(3)

# Setting up parameters for health and damage.. damage will be random
# Also added different punches to make more interesting

damage = 0
player_health = 100
oppo_health = 100
counter = 0
punch = ["Uppercut", "Right Hook", "Left Hook", "Overhand Right", "Low Blow", "Haymaker"]
while True:

    def boxer_damage(damage):
        damage = random.randint(1,20)
        return damage
    def boxer_health(health):
        health - boxer_damage(damage)
        return health

# Fight loop will randomize and calculate damage and health
# Will end once someone hits 0 health


    if player_health <= 0:
        print("Sorry I guess " + opponent + " was too much for you.")
        break
    if oppo_health <= 0:
        print("Wow! Great job " + player + " you knocked " + opponent + " out cold.")
        break
    if player_health >= 0 and oppo_health >= 0:
        if counter == 0:
            time.sleep(1)
            damage = boxer_damage(damage)
            print("Ok " + player + " your moving in on him...")
            choice = random.choice(punch)
            print(str("You hit him with a " + choice + " for " + str(damage) + " damage."))
            if choice == "Low Blow":
                print("You better watch those punches.. you don't want to get disqualified....")
            elif damage < 5:
                print("Man you whiffed with that " + choice + "...")
            elif damage > 15:
                print("Nice " + choice + "!!! I\'m suprised he didn\'t go down!")
            oppo_health -= damage
            print(opponent + " has " + str(oppo_health) + " health left.")
            print(player + " has " + str(player_health) + " health left.")
            print(input("Press enter to continue:"))
            counter += 1
        elif counter == 1:
            time.sleep(1)
            damage = boxer_damage(damage)
            choice = random.choice(punch)
            print(opponent + " hit you with a " + choice + " for " + str(damage) + " damage.")
            if damage > 15:
                print("Wow " + player + " are you alright?")
            elif damage < 5:
                print("Keep moving " + player + " looks like hes having a hard time hittin\' you")
            elif choice == "Low Blow":
                print("C'MON REF! Pay attention!!")
            player_health -= damage
            print(opponent + " has " + str(oppo_health) + " health left.")
            print(player + " has " + str(player_health) + " health left.")
            print(input("Press enter to continue:"))
            counter -= 1
    
            
        

    


        
        

    
    

