# Functions
# Author: Princeton
# 8 October

# function to print "hello"
def say_hello():
    print("hello")


say_hello()


# function to print a personaliized hello
def say_hello_nicely(name: str):
    print(f"hello {name}!")


def normalized_input():
    """Takes user input and cleans it up."""
    output = input().lower().strip(",.! ")
    return output


def normalize_input(user_input: str):
    """Takes user input and cleans it up."""
    output = user_input.lower().strip(",.?! ")
    return output


# ask the user what the weather is
weather_reply = normalized_input()
