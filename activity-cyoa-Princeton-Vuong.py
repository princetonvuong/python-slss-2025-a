# Choose Your own adventure
# Princeton Vuong
# 24 September

# Choose your own adventure story focusing on using
# variable and branching/conditionals

import sys
import random

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
print("health")
print("strength")
drink1 = input("select one of the options.")

if drink1.lower() == "strength":
    inventory.append("strengthpot")
    print(f"You have picked up a {drink1}")

elif drink1.lower() == "health":
    inventory.append("healthpot")
    print(f"You have picked up a {drink1}")

# Rising action
print("As you were about to leave the tavern, an ogre appears")
print("fight")
print("run")
print("hide")
choice1 = input("Do you wish to do?")

strength_boost = 0

enemy_health = 20
enemy1 = "ogre"

if choice1 == "fight":
    while health > 0 and enemy_health > 0:
        action1 = input("Do you want to attack or use a potion? ")

        if "attack" in action1.lower():
            print(f"You have encountered an ogre with {enemy_health} health")

            if player_class == "mage":
                player_damage = random.randint(15, 20)
                print(
                    f"You used your staff and cast a powerful spell at the {enemy1} for {player_damage} damage!"
                )

            elif player_class == "assassin":
                player_damage = random.randint(10, 25)
                print(
                    f"You swiftly stab the {enemy1} with your dagger for {player_damage} damage!"
                )

            elif player_class == "warrior":
                player_damage = random.randint(8, 18)
                print(
                    f"You swing your sword at the {enemy1} for {player_damage} damage!"
                )

            player_damage += strength_boost
            enemy_health -= player_damage

            print(f"The {enemy1} now has {enemy_health} health remaining!")

        elif "potion" in action1.lower():
            print("Inventory:", inventory)
            potion1 = input("Which potion do you want to use? ").lower()

            if potion1 == "healthpot" and "healthpot" in inventory:
                health += 20
                inventory.remove("healthpot")
                print("You used a health potion and restored 20 HP!")
                print(f"You now have {health} HP.")

            elif potion1 == "strengthpot" and "strengthpot" in inventory:
                strength_boost = 10
                inventory.remove("strengthpot")
                print(
                    "You feel a surge of power! Your next attack will deal +10 damage."
                )

            else:
                print("You don't have that potion!")

        else:
            print("Invalid action — you lose your turn!")

        if enemy_health > 0:
            enemy_damage = random.randint(5, 15)
            health -= enemy_damage
            print(f"The {enemy1} attacks you for {enemy_damage} damage!")
            print(f"You now have {health} HP.")


if enemy_health <= 0:
    print(f"You have defeated the {enemy1}")
    if strength_boost > 0:
        strength_boost = 0

elif health <= 0:
    print("GAME OVER")
    sys.exit()


# Climax

# Resolution
