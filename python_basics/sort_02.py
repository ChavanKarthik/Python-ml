def sorting(x):
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp


a = [5, 6, 8, 2, 6, 4]
print('unsorted list', a)
sorting(a)
print('sorted list', a)


def sort1(y):
    for i in range(len(y) - 1):
        minimum_position = i
        for j in range(i, len(y)):
            if y[j] < y[minimum_position]:
                minimum_position = j

        temp = y[i]
        y[i] = y[minimum_position]
        y[minimum_position] = temp


b = [5, 6, 8, 2, 1, 1, 6, 8, 10, 42]
print('unsorted list', b)
sort1(b)
print('sorted list', b)
