def sum(a, b):
    c = a + b
    print(c)


sum(5, 10)


def sum1(*d):
    f = 0  # declaring initial value as zero
    for i in d:  # looping all the arguments(tuples) given in function
        f = f + i
    print(f)


sum1(1, 2, 3, 4, 6)

p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
q = [1, 2, 3]


def even_odd_counter(p):
    even = 0
    odd = 0
    for j in p:
        if j % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


even, odd = even_odd_counter(q)

print("Even : " + str(even))
print("Odd  : " + str(odd))
