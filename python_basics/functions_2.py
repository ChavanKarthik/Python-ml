def apply_twice(func, arg):
    return func(func(arg))  # iterates two times in same func with 1st func result as 2nd args


def add_five(x):
    return x + 5


print(apply_twice(add_five, 10))  # based on apply_twice func args should be given


def pure_func(x, y):
    temp = x + 2 * y
    return temp / (2 * x + y)


print(pure_func(float(5), float(20)))
some_list = [5, 8, 9]


def impure(arg):
    some_list.append(arg)


print(impure(6))
