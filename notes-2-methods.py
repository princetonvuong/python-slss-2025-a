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
