# Meares, William
# Computer Programming, period 4
# Assignment: Homework 4
# 10/7/2026

alien_color = "green"
if alien_color == "green":
    print("+5 points")
elif alien_color == "yellow":
    print("+10 points")
else:
    print("+15 points")


alien_color = "yellow"
if alien_color == "green":
    print("+5 points")
elif alien_color == "yellow":
    print("+10 points")
else:
    print("+15 points")


alien_color = "red"
if alien_color == "green":
    print("+5 points")
elif alien_color == "yellow":
    print("+10 points")
else:
    print("+15 points")

test_ages = [1, 3.9, 10, 13, 19, 20, 21, 65]

for age in test_ages:
    if age < 2:
        print("thats a baby")
    elif age >= 2 and age < 4:
        print("thats a toddler")
    elif age >= 4 and age < 13:
        print("thats a kid")
    elif age >= 13 and age < 20:
        print("thats a teenager")
    elif age >= 20 and age < 65:
        print("thats an adult")
    else:
        print("behold the elder")

usernames = ["george", "walter11", "crazycat", "admin", "player53"]
for name in usernames:
    if name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for loggin in again")

usernames = []
for name in usernames:
    if name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for loggin in again")

# I wasnt really sure how to fix this secton of the homework

    current_users = ["bob", "hank", "nick", "mark", "dodo"]
    new_users = ["falcon", "bobcat", "bob", "finn", "dodo"]
    for user in new_users:
        if user == current_users:
            print("enter a new username")
        else:
            print("proceed")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")