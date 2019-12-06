a = ['aaa', 'bbb', 'ccc']
print(a)
a.append('ddd')
print(a)
a.pop()
print(a)
print(a[0])
a[0] = 'AAA'
print(a)
a[0] = 'aaa'
temp = a[0]
a[0] = a[2]
a[2] = temp
print(a)
