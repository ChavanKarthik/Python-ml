def countdown():
    i = 5
    while i > 0:
        yield i  # generators are created by yield statement
        i -= 1  # individual iterable is stored in yield


for i in countdown():
    print(i)


def infinite_7():
    while True:
        yield 7


for i in infinite_7():
    print(i)  # returns a infinite loop of 7


def nums(x):
    for x in range(x):
        if i % 2 == 0:
            yield i


print(list(nums(20)))
