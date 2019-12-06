a = [6, 4, 2, 1, -2, -5, -8]
c = 0
for b in a:
    c += b
print(c)

total = 0
j = 0
while j <= 6:
    total += j
    j += 1
print(total)

a = [6, 4, 2, 1, -2, -5, -8]
s = 0
t = 0
while a[t] >= 0:
    s += a[t]
    t += 1
print('sum of number up to ', t, 'is ', s)

list_1 = [1, 2, 3, 4, 5]
x = y = 0
while list_1[y] < 6:
    x += list_1[y]
    list_1[y] += 1
print('sum of x is', x)
