# William Meares
# Computer Programming, period 4
# Assignment: Homework 3
# 9/15/2026

hobbies = ["drone flying", "rubik's cube", "gaming", "cooking", "baking"]
print(hobbies)
print(len(hobbies))
print(hobbies[2])
print(hobbies[0])

hello = ["hello! " * 100]
print(hello)

list1 = ["pumpkin", "halloween", "jack-o-lantern", "spooky"]
list2 = ["christmas", "new year", "holiday", "santa"]
list3 = list1+list2
print(list3)

fav_foods = ["pasta", "hamburger", "pancakes", "ice cream", "pizza"]
print(len(fav_foods))
print(fav_foods[2])
print(fav_foods[-4])
fav_foods.append("William")
fav_foods.insert(2, 16)
fav_foods.pop(0)
print(fav_foods)

numbers = list(range(1, 21))
for number in numbers:
    print(number)

odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

animals = ["squirrel", "bear", "capybara"]
for animal in animals:
    print(f"A {animal} would make a decent pet")
print("All of these animals have fur")

guest_list = ["Grandpa Bill", "Alexander the Great", "Thor"]
for people in guest_list:
    print(f"{people} you are invited to dinner!")
print("Thor cant make it to dinner")
guest_list[2] = "Albert Einstein"
for people in guest_list:
    print(f"{people} you are in vited to dinner")