# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).

l = []
for i in range(2000, 2051):
    if (i % 7 == 0) and (i % 5 != 0):
        l.append(str(i))
print(','.join(l))


# Write a program which can compute the factorial of a given numbers.
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


print(fact(8))

"""With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is 
an integral number between 1 and n (both included). and then the program should print the dictionary."""

n = 8
d = dict()
for i in range(1, n + 1):
    d[i] = i * i

print(d)

"""Write a program which accepts a sequence of comma-separated numbers 
from console and generate a list and a tuple which contains every number."""

values = "5,6,7,8,9,10"
l = values.split(",")
t = tuple(l)
print(l)
print(t)
