print("welcome to the adventure games!")
name = input("A game at bay")
print("Greetings, Marcus are you ready for the journey ahead?")
health = 100
has_flashlight = False
print(
    "Your boat makes it to land and your injured. There are two paths, to the left and right"
)
choice1 = input()
if choice1 == "left":
    print("Through your long walk in the dark your foot steps on a backpack.")
    choice2 = input("do you pick up and open the backpack? (yes/no):")
    if choice2 == "yes":
        print("you find a flashlight and water! This may be useful.")
        has_flashlight = True
    else:
        print("you leave the backpack alone and keep walking.")
    print("You find yourself face to face with a hidden hole in ground.")
    choice3 = input("Do you want to enter the whole? (yes/no): ").lower()
    if choice3 == "yes":
        if has_flashlight:
            print(
                "with your flashlight, you explore safley and find tressure and medical supplies."
            )
            health += 47
            print("Ending: You escape thhe hole healed and rich!")
        else:
            print(
                "It's pitch black... You stumble and fall. you lose 50 health making your pre-existing leg injury worse."
            )
            health -= 50
            print(f"your health is now {health}")
            if health <= 0:
                print("you coudlnt surrive the fall.")
                print("Ending: You barely surrived.")
    else:
        print("You aviod the hole and continue")
        print("Eventually, you find a flare gun and are rescued.")
        print("Ending: You are saved but the tressure remains.")
elif choice1 == "right":
    print("You take the right path and you end up walking the shoreline.")
    print("You find fruit you have never seen growing on the bush")
    choice2 = input("Do you eat the fruit (yes/no):")
    if choice2 == "yes":
        print("The fruit taste odd and you start to feel lightheaded")
        health -= 35
        print(f"your health os now {health}")
    else:
        print("you ignore the fruit and continue down the beach")
    print("You find a cave entrance ahead.")
    choice3 = input("Do you enter the cave? (yes/no): ").lower()
    if choice3 == "yes":
        if has_flashlight:
            print("You use your flashlight to explore the cave.")
            print("You find gold and an old map out of the forest.")
            print("ENDING: You become a legend among adventurers! ")
        else:
            print("It's dark inside. You trip and hurt yourself.")
            health -= 50
            print(f"Your health is now {health}.")
        if health <= 0:
            print("You succumb to your injuries in the cave.")
            print("ENDING: Darkness takes you.")
        else:
            print("You find your way out, bruised and tired.")
            print("ENDING: You barely survive your mistake.")
    else:
        print("You avoid the cave and follow the shoreline.")
        print("Eventually, a rescue boat sees you and picks you up.")
        print("ENDING: You’re saved, but empty-handed.")
else:
    print("You stay frozen in fear and never choose a path.")
    print("ENDING: You are never seen again.")
