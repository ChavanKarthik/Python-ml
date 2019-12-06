a = list(range(100, 102))
for x in a:
    print(x)

for y in list(range(100, 102)):
    print(y)

aaa = [[1, 2.5], [3, 4, 10], [101, 105]]
for z in aaa:
    if isinstance(z, list):
        for w in z:
            if w == 10:
                print('Found 10')
                break

aaa = [1, 2, 5, [3, [9, [10, 10], 10], 4, 10], 101, 105]


def recursiveElementCheck(a, compare):
    if isinstance(a, int):
        if a == compare:
            print("Found ", compare)
            exit()
    else:
        for z in a:
            if recursiveElementCheck(z, compare):
                return


recursiveElementCheck(aaa, 10)
