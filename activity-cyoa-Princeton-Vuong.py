# Choose Your own adventure
# Princeton Vuong
# 24 September

# Choose your own adventure story focusing on using
# variable and branching/conditionals

import sys

# Intro
greeting = "Welcome to the diddy dungeon"
print(greeting)

health = 0
inventory = []

name = input("What shall I call you traveller?")
print(f"Nice to meet you {name}!")

print("Please select a class from the following options.")
print("mage")
print("assassin")
print("warrior")
player_class = input("Which class would you like to select?")

if player_class.lower() == "mage":
    print(f"You chose {player_class}, a long distance class with exceptional power")
    health = 60
    inventory.append("staff")
elif player_class.lower() == "assassin":
    print(f"You chose {player_class}, a close distance class with exceptional speed")
    health = 75
    inventory.append("dagger")
elif player_class.lower() == "warrior":
    print(f"You chose {player_class}, a close distance class with exceptional defence")
    health = 100
    inventory.append("shield")

if health > 0:
    print(f"{name} the {player_class}, has {health} health points and a {inventory}.")

if health <= 0:
    print("GAME OVER!")

startgame = input("Do you wish to begin? Yes/No")

if startgame.lower() == "yes":
    print("Now the story begins.")
    print("With a Dragon who is terrorizing a small village")
    print("This Dragon resides in the great volcano far away.")
    print(
        "Your job,as the village's last hope,is to travel to the great volcano and slay this Dragon once and for all."
    )
    print("Your journey begins in the village tavern.")

else:
    print("restart the game dummy")
    sys.exit()
# Problem
print("To help you on your journey, we will give you one free potion of your choosing.")
print("speed")
print("health")
print("invis")
drink1 = input("select one of the options.")

if drink1.lower() == "speedpot":
    inventory.append("speedpot")
    print(f"You have picked up a {drink1}")

elif drink1.lower() == "healthpot":
    inventory.append("healthpot")
    print(f"You have picked up a {drink1}")

elif drink1.lower() == "invispot":
    inventory.append("invispot")
    print(f"You have picked up a {drink1}")

# Rising action
print("As you were about to leave the tavern, an ogre appears")
print("fight")
print("run")
print("hide")
choice1 = input("Do you wish to do?")
enemy_health = 50
if choice1 == "fight":
    print(f"You have encountered an ogre with {enemy_health} health")
    if player_class == "mage":


# Climax

# Resolution
