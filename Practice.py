# 1 - Odd or Even

# Ask the user for a number. Depending upon the input, output whether the number is an odd or even number
# name = input('Hello, what is your name? ').capitalize()
# print(f'Nice to meet you {name}!')
# while True:
#     try:
#         number: int = int(input('Please pick a whole number. '))
#         break
#     except ValueError:
#         print(f'Oops sorry {name}, that isn\'t a whole number')

# 1.0 - Depending on whether the number is even or odd, print out an appropriate message to the user.
# if number % 2 == 0:
#     print(f'The number you chose, {number}, is an EVEN number!')
# else:
#     print(f'The number you chose, {number}, is an ODD number!')

# 1.1 - If the number is a multiple of 4, print out a different message.
# if number % 4 == 0:
#     print(f'The number you chose, {number}, is a multiple of 4')
# elif number % 2 == 0:
#     print(f'The number you chose, {number}, is an EVEN number')
# else:
#     print(f'The number you chose, {number}, is an ODD number')

# 1.2 - Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
# while True:
#     try:
#         check: int = int(input('Please choose a whole number to divide by.'))
#         break
#     except ValueError:
#         print(f'Sorry {name} that isn\'t a whole number')
#
# if number % check == 0:
#     print(f'The number {number}, is a multiple of {check}')
# else:
#     print(f'The number {number} is NOT a multiple of {check}')

"""------------------------------------------------------------------------------------------------------------------"""

# 2 - Write a program that prints all the elements of the list that are less than 5

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# alessthanx = []
# alessthan5 = []

# 2.0 - list the values less than 5 from the list a.
# for x in a:
#     if x < 5:
#         alessthan5.append(x)
#
# print(f'These are the numbers in the list less than 5: \n {alessthan5}')

# 2.1 - Ask the user for a number and return a list of the numbers less than their chosen number.
# while True:
#     try:
#         check: int = int(input('Pick a number to see which values are less than your choice. '))
#         break
#     except ValueError:
#         print('Sorry this isn\'t an integer value')
#
# for x in a:
#     if x < check:
#         alessthanx.append(x)
#
# print(f'These are the number in the list less than {check}: \n {alessthanx}')

"""------------------------------------------------------------------------------------------------------------------"""
# 3 - Divisors
# 3.0 - Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
divisors = []
while True:
    try:
        num = int(input('Pick a number to see its divisors. '))
        break
    except ValueError:
        print('Sorry that is not a valid whole number!')
x = range(1, 1000000000)

# Checks what the divisors of the chosen number are and append the list of divisors
for divisor in x:
    if num % divisor == 0:
        divisors.append(divisor)

# Tells the user if their choice was a prime number or not
if len(divisors) == 2:
    print(f'The number {num} is a prime number')
else:
    print(f'The number {num} is NOT a prime number')

# Tell the user what the divisors are
print(f'These are the divisors of {num}: \n {divisors}')
