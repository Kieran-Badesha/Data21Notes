# def addition(num1, num2):
#     return num1 + num2
#
#
# add = lambda num1, num2: num1 + num2
# print(add(2, 3))
#
# print(addition(2, 3))

savings = [234, 555, 674, 78]
bonus = []


def b_func():
    for x in savings:
        increase = x * 1.10
        print(increase)
b_func()

savings_lam = [234, 555, 674, 78]
bonus_lam = list(map(lambda x: x * 1.1, savings))

print(bonus)

# in oop can get too complicated 