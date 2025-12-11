# Maths
# Author: Princeton Vuong
# November 12


# Machines are good at crunching numbers -
# faster and more accurately than most humans!
# Create a small program that calculates something useful to you (making you smile is useful).
# It should take user input,
# at use at least one of the number operators we saw in class: + / * -.
# You may modify one of your previous exercises to include calculations, if you wish.


NUM_PEOPLE = 5


def pet_counter():
    """Ask how many dogs and cats people own and print totals."""
    total_dogs = 0
    total_cats = 0

    for _ in range(NUM_PEOPLE):
        print("How many dogs and cats do you own?")
        dogs = int(input("Dogs: ").strip("!.?,"))
        cats = int(input("Cats: ").strip("!.?,"))

        total_dogs = total_dogs + dogs
        total_cats = total_cats + cats

    print("Total dogs owned:", total_dogs)
    print("Total cats owned:", total_cats)

    average_dogs = total_dogs / NUM_PEOPLE
    average_cats = total_cats / NUM_PEOPLE

    print("Average dogs per person:", average_dogs)
    print("Average cats per person:", average_cats)


def main():
    pet_counter()


if __name__ == "__main__":
    main()
