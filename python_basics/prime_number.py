import math


def prime_check(x):
    if x % 2 == 0:
        print(f"{x} is a not prime number(even number)")
        return

    for i in range(3, math.floor(math.sqrt(x)), 2):  # loop all number from 2 to x-1
        if x % i == 0:
            print(f"{x} is a not prime number")
            return

    print(f"{x} is a prime number")


prime_check(22)


def factorial(y):
    for i in range(1, y):
        y = y * i
    print(f"factorial of given number is {y}")


factorial(5)

x = int(input('please the number to get the table \n'))


def multiplier(x):
    for i in range(1, 11):
        print(f'{x}X{i}={x * i}')


multiplier(x)
