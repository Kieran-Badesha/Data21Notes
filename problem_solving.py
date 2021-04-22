# Question 1
# list_of_multiples = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
# print(sum(list_of_multiples))
# Ans = 233168
#
#
# Question 2
# n1, n2 = 1, 2
# count = 0
# while n1 <= 4000000:
#     if n1 % 2 == 0:
#         count += n1
#     n1, n2 = n2, n1+n2
# print(count)
# Ans = 4613732
#
#
# Question 3
# Create empty list
# list = []
# Creates list of numbers we want to find the lowest common multiple of and append to list.
# for i in range(2, 21):
#     list.append(i)
# for i in range(0, len(list)):
#     for j in range(1, i+1):
#         if list[i] % list[i-j] == 0:
#             list[i] = int(list[i] / list[i-j])
# answer = 1
# for i in range(0, len(list)):
#     answer = answer * list[i]
# print(answer)

# Create list of numbers we want to find lcm of
# import math
# Returns the lcm of first n numbers
# def lcm(n):
#     ans = 1

    # for i in range(1, n + 1):
    #     ans = int((ans * i)/math.gcd(ans, i))
    # return ans
# main
# n = 20
# print (lcm(n))


# Question 4
# Create empty list
# prime_numbers = []
# for num in range(2, 2000001):
#     prime = True
#     for i in range(2, num, 2):
#         if num % i == 0:
#             prime = False
#     if prime is True:
#         prime_numbers.append(num)
#
#
# print(sum(prime_numbers))

# Question 4 using MATH module
# import math
# prime_numbers = [2]
# for num in range(3, 2000001, 2):
#     if all(num % i != 0 for i in range(3, int(math.sqrt(num))+1, 2)):
#         prime_numbers.append(num)
# print(sum(prime_numbers))
# ANS = 142913828922


# Problem 5:
# from num2words import num2words
#
# list_of_nums = []
# for number in range(1, 1001):
#     num = num2words(number).replace("-", "").replace(" ", "")
#     list_of_nums.append(num)
# print("\n".join(list_of_nums))
#
# print(sum(len(i) for i in list_of_nums))

# ANS = 21124

# Problem 6

# ways = []
# target = [200]
# coins = [1, 2, 5, 10, 20, 50, 100, 200]
# coins_top = [200, 100, 50, 20, 10, 5, 2, 1]
# for i in coins:
#     if target % i == 0:
#         ways.append()
