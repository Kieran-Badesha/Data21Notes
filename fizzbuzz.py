"""def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(int(i))


n = 10
print(fizzbuzz(n))
"""


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Fizzbuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


n = 12
print("\n".join(fizzbuzz(n) for n in range(1, 15)))
