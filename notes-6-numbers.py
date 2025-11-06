# Numbers and operations
# Author : Princeotn VUong
# November 5


# work with numbers amd operations

# Create an algorithm to gather data to find the most popular bubble tea place around us

# Version 1
def vote_listed_choices():
    """display all choices
    5 Users votes for their choice
    Results will be printed"""
    CHOICES = [
        "A. Blenz",
        "B. Bubble Queen",
        "C. Sun Tea",
        "D. heytea",
        "E. CoCo",
        "F. Fresh T",
    ]
    # show all the choices
    print("Vote for your favourite from the list:")
    print("Give the letter of your choice")
    for choice in CHOICES:
        print(choice)

    # Keep track of a talley
    # Data analysis
    # Give the raw scores
    # Give scores as a percentage


# Version 2
# Ask the user to give their favoutite bubble tea place
# keep track of a tally
# Data analysis
# Give the raw percentage score
# Give scores as a percentage


def main():
    vote_listed_choices()


if __name__ == "__main__":
    main()
