x = '0101010'

for y in x:
    if int(y) == 0 or int(y) == 1:
        v = True
    else:
        v = False
        print("Not a binary number")
        break
if v:
    print("binary number")

test_string = "geekforgeeks"
# test_string = [1, 2, 3]
# print("The original string : " + str(test_string))
res = ''.join(sorted(test_string))


# print("String after sorting : " + str(res))

def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
# list3 = extendList('a')
print(list1)
