# Problem 1
user_age = int(input("What is your age?"))
print(f"Your age in 2049 will be {user_age + 31} years old")

# Problem 2
total_score = 0


for _ in range(5):
    score = float(input("What is your rating from 1 to 10: "))

    if score > 10:
        score = 10

    total_score += score

average_score = total_score / 5

print(f"Your olympic score is {average_score} / 10")

# Problem 3

total_cost = 0

burger = input("Do you want a burger for $5? (yes/no)").lower()
if burger == "yes":
    total_cost += 5
fries = input("Do you want a fries for $3? (yes/no)").lower()
if fries == "yes":
    total_cost += 3

total_cost = total_cost * 1.14

print(f"your total is ${total_cost}")
