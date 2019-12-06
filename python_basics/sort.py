def bubble_sort(x):
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp


a = [5, 6, 8, 1, 3, 4]
print('unsorted list', a)
bubble_sort(a)
print('sorted list', a)


def selection_sort(y):
    for i in range(len(y) - 1):
        minpos = i

        for j in range(i, len(y)):

            if y[j] < y[minpos]:
                minpos = j

        temp = y[i]
        y[i] = y[minpos]
        y[minpos] = temp


b = [5, 6, 8, 3, 2, 3]
selection_sort(b)
print(b)


def eff_sort(z):
    for s in range(len(z) - 1):
        minimum_position = s

        for p in range(s, len(z)):

            if z[p] < z[minimum_position]:
                minimum_position = p

        temp1 = z[s]
        z[s] = z[minimum_position]
        z[minimum_position] = temp1


zee = [5, 1, 4, 6, 9, 10]
eff_sort(zee)
print(zee)
