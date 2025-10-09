# Methods
# Author: Princeton Vuong
# Date: 6 October

weather = input("What's the weather like right now?")
if weather.lower().strip("!") == "rainy":
    print("You should bring an umbrella")
elif weather.lower() == "sunny":
    print("You should bring suncreen")

else:
    print("I see...")

fries_reply = input("Do you want fries?")
# "yes!"

if "yes" in fries_reply.lower():
    print("Here are your fries")
else:
    print("Here are no fries")
