# Work - McDoBot
# Author: Princeton Vuong
# 6 October

# Write a McDonald's bot that asks if you want fries with your meal.
# Call it work-mcdobot.py .
# It should accept Yes/yes or No/no as inputs, and reply
# appropriately depending on the answer.
# If the user inputs anything else, it should repeat back their answer
# and say that it does not understand.
fries = input("Would you like fries with your meal?")
if fries.lower() == "yes":
    print("Here is your meal with fries.")
elif fries.lower() == "no":
    print("Here is your meal without fries.")
else:
    print(f"I dont understand {fries}")
