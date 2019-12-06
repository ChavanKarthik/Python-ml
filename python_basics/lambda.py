def square(y):
    return y ** 2


print(square(5))

s = lambda x, y: x ** 2 + y ** 2  # lambda is a default function name
print(s(4, 5))
xyz = lambda a, b, c: 2 * a + b ** 2 + c
print(xyz(1, 2, 3))

yxz = lambda d: d * 3
print(yxz(4))

nums = [11, 22, 33, 44]
print(list(map(lambda e: e + 4, nums)))  # to map give function and iterable variable
print(list(map(lambda e: e + 5, nums)))  # directly create a lambda and map
print(list(filter(lambda f: f % 2 == 0, nums)))  # create a lambda and filter output
