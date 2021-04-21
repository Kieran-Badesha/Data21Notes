from typing import Set

hi = "Hello World!"
print(hi)

name = input("What is your name? ")
age = input(f"Hello {name}! How old are you? ")
Height = input("What is your height in cm? ")
Date = input("What is the date today? ")

print(f"Pleased to meet you {name}. You are {age} years old and {Height}cm tall. Today's date is {Date}")

# Python Slicing -----------------------------------------------------------------

print(hi[8:5:-1])

print(hi.upper())
print(hi.casefold())
print(hi.count("l"))

# concatenations -----------------------------------------------------------------

a = 40
b = input("number")

print(a + int(b))
print(str(a) + b)

# Booleans ----------------------------------------------------------------------
a = True
b = False

print(a == b)

print(hi.isalpha())
print(hi.isalnum())
print(hi.islower())
print(hi.lower().islower())

z = None

print(bool(None))
print(bool(z == None))
print(bool(z == False))

# Lists & Tuples --------------------------------------------------------------------------
    #Lists
        #Can have mixed data types in lists, can be changed.
shopping_list = ["eggs", "milk", "bread"]

print(shopping_list)
print(shopping_list[0:2])

shopping_list[0] = "5"
    #Tupples
        #Cannot be changed, is immutable.
shopping_tup = ("bread", "milk", "eggs")
print(shopping_tup)
shopping_tup[0] = "chocolate"

# Dictionary ------------------------------------------------------------------------------
student_1 = {
    "name": "Kieran",
    "stream": "data",
    "list": ["value1", "value2", "value3"]
}

print(student_1["list"][1])

student_1["name"] = "bob"

print(student_1)

student_1["list"].remove("value3")

# Sets ------------------------------------------------------------------------------------
car_parts: set[str] = {"wheels", "doors", "windows"}

print(car_parts)
print(type(car_parts))

car_parts.add("headlights")

# Control Flow ----------------------------------------------------------------------------
age = 90

if age > 18:
    print("You are older than 18!")
if age > 50:
    print("you are older than 50!")
else:
    print("You are not older than 18!")

# Loops -----------------------------------------------------------------------------------
list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
em_list = [[1, 2, 3], [2, 3, 4]]

for data in list_data:
    print(data)

for data in em_list:
    print(data)
    for num in data:
        print(num)

x = 0
while x < 10:
    print("this is True")
    print(x)
    if x == 4:
        break
    x += 1

user_prompt = True

while user_prompt:
    age = int(input("What is your age?"))
    if age:
        user_promt = False
    else:
        print("Please provide your answer as a digit")

print(len(set("bob")))
print(len("bob"))
print(len(set("bob")) == len("bob"))