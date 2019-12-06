# from factorial import fact

# k = 5

# print(fact(k))


# def sum():
#     print("sum function is called")


# if __name__ == "__sum__":
#     sum()

# sum()


def angle(x):
    for z in range(x):
        for y in range(z):
            if y != 1:
                print(' *', end="")
                print('__', end="")
            else:
                print(' &')
                print('==')


# angle(5)

def angle(p):
    for q in range(p + 1):
        for s in range(p - q):
            print("  ", end="")
        for r in range(q):
            if r == (q - 1):
                print(' ^')
            else:
                print(' ^', end="")


angle(6)
