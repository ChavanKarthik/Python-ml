# finding Factorial using for loop
n = 5


def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


# finding Factorial using recursion

if __name__ == "__fact__":
    fact()
print(fact(5))

k = 5


def facto(k):
    if k == 0:
        return 1
    return k * facto(k - 1)


result = facto(5)

if __name__ == "__facto__":
    facto()
print("factorial : " + str(result))

print(__name__)
