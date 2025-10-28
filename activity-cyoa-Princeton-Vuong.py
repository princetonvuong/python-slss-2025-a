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

name = input("What shall I call you traveller? ")
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
        action1 = input("Do you want to attack or use a potion?")

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

print("After defeating the ogre, you reach a fork in the road.")
print("Path A: A dark forest.")
print("Path B: A rocky mountain trail.")
path = input("Which path do you choose?")

if path.lower() == "a":
    print("You enter the dark forest. It's eerily quiet...")
    print("A Goblin King ambushes you!")
    enemy2 = "Goblin King"
    enemy_health = 40
elif path.lower() == "b":
    print("You climb the mountain path. Rocks tumble as you go.")
    print("A Goblin King leaps out from behind a boulder!")
    enemy2 = "Goblin King"
    enemy_health = 40

# --- MINI BOSS: GOBLIN KING ---
while health > 0 and enemy_health > 0:
    action2 = input("Do you want to attack or use a potion?\n")

    if "attack" in action2.lower():
        if player_class == "mage":
            player_damage = random.randint(12, 22)
        elif player_class == "assassin":
            player_damage = random.randint(10, 26)
        elif player_class == "warrior":
            player_damage = random.randint(9, 20)

        player_damage += strength_boost
        strength_boost = 0
        enemy_health -= player_damage
        print(
            f"You strike the {enemy2} for {player_damage} damage! ({enemy_health} HP left)"
        )

    elif "potion" in action2.lower():
        print("Inventory:", inventory)
        potion2 = input("Which potion do you want to use?").lower()

        if potion2 == "healthpot" and "healthpot" in inventory:
            health += 20
            inventory.remove("healthpot")
            print("You used a health potion and restored 20 HP!")
        elif potion2 == "strengthpot" and "strengthpot" in inventory:
            strength_boost = 10
            inventory.remove("strengthpot")
            print("You feel a surge of power! +10 damage on your next attack.")
        else:
            print("You don't have that potion!")

    else:
        print("Invalid action — the Goblin King attacks first!")

    if enemy_health > 0:
        enemy_damage = random.randint(8, 18)
        health -= enemy_damage
        print(f"The {enemy2} slashes you for {enemy_damage} damage! ({health} HP left)")

if health <= 0:
    print("You were defeated by the Goblin King...")
    sys.exit()

print(
    f"You have defeated the {enemy2}! You loot his chest and find another health potion."
)
inventory.append("healthpot")

# --- FINAL BOSS: DRAGON ---
print("\nYou finally reach the mouth of the volcano.")
print("The Dragon roars from within — this is it.")
enemy3 = "Dragon"
enemy_health = 75

while health > 0 and enemy_health > 0:
    action3 = input("Do you want to attack or use a potion?")

    if "attack" in action3.lower():
        if player_class == "mage":
            player_damage = random.randint(18, 25)
        elif player_class == "assassin":
            player_damage = random.randint(15, 30)
        elif player_class == "warrior":
            player_damage = random.randint(12, 22)

        player_damage += strength_boost
        strength_boost = 0
        enemy_health -= player_damage
        print(
            f"You strike the {enemy3} for {player_damage} damage! ({enemy_health} HP left)"
        )

    elif "potion" in action3.lower():
        print("Inventory:", inventory)
        potion3 = input("Which potion do you want to use?").lower()

        if potion3 == "healthpot" and "healthpot" in inventory:
            health += 25
            inventory.remove("healthpot")
            print("You used a health potion and restored 25 HP!")
        elif potion3 == "strengthpot" and "strengthpot" in inventory:
            strength_boost = 15
            inventory.remove("strengthpot")
            print("You feel an immense surge of power! +15 damage next attack.")
        else:
            print("You don't have that potion!")

    else:
        print("You hesitate — the Dragon strikes first!")

    if enemy_health > 0:
        enemy_damage = random.randint(12, 25)
        health -= enemy_damage
        print(
            f"The {enemy3} breathes fire, dealing {enemy_damage} damage! ({health} HP left)"
        )

if health <= 0:
    print("You were burned to ashes by the Dragon... GAME OVER.")
    sys.exit()

print("With one final blow, the Dragon collapses.")
print("The volcano rumbles... but you stand victorious.")
print(f"Congratulations, {name} the {player_class}! You have saved the village!")

# Climax

# Resolution
