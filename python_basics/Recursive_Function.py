aaa = [1, 2, 3, 4, [5, 6, [7, 8], 9, 10]]
for x in aaa:
    if isinstance(x, int):
        if x == 11:
            print('found x = ' + str(x))
    elif isinstance(x, list):
        for y in x:
            if isinstance(y, int):
                if y == 11:
                    print('found y = ' + str(y))
            elif isinstance(y, list):
                for z in y:
                    if z == 11:
                        print('found z = ' + str(z))
                    else:
                        print('not found')


def recursive(s, validate):
    if isinstance(s, int):
        if s == validate:
            print('found ' + str(s))
    else:
        for p in s:
            if recursive(p, validate):
                return


# recursive(aaa, 8)

# try:
#     print(list(range(0, 101, 5)))
# except ZeroDivisionError:
#     print('divided by zero')
# finally:
#     print('this will run')

# if 10 in aaa:
#     print('found n = 10')
# else:
#     print('10 not found')


def sum_to(x):
    for e in range(x + 1):
        if e == 5:
            print("found 5")
            return x + 5
        else:
            print("not found")

# sum_to(10)
