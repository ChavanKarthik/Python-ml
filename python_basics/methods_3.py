x = [4, 6, 8]


def update_1(k):
    k.append('45')
    print(f'k = {k}')


# update_1(m)
# print(m)

def modify_1():
    global x
    x = [77, 88, 99]
    print(f'x = {x}')


modify_1()
print(x)


def update_content(x):
    x[0] = 77
    x[1] = 55
    x[2] = 22
    print(f'x = {x}')
# update_content(m)
# print(m)
