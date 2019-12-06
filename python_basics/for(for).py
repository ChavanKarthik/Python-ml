aaa = {1, 2.5, 3, 4, 10, 101, 105}
for x in aaa:
    if x == 105:
        print('found ' + str(x))
for z in list(range(5, 100)):
    if z == 98:
        print('found ' + str(z))

ccc = [55, 56, [15, 16, 17, 18, [25, 26, 27, 28], 19, 20], 57]
for y in ccc:
    if isinstance(y, list):
        for s in y:
            if isinstance(s, list):
                for p in s:
                    if p == 25:
                        print('found ' + str(p))

ddd = [55, 56, 58, 59, [15, 16, 17, 18, 25, 26, 27, 28, 19, 20], 57]
for t in ddd:
    if isinstance(t, int):
        if t == 59:
            print('found t = ' + str(t))
    elif isinstance(t, list):
        for p in t:
            if p == 59:
                print('found p = ' + str(p))
