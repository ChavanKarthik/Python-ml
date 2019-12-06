# None is often used to represent 'absence of value(Null)'
print(None == None)


def asdf():
    print('Hi!')


var = asdf()
print(var)  # None is printed because of null argument

# Dictionaries are data structures used to map arbitrary keys to values
ss = {"ram": 24, "sham": 28, "ravi": 12, "don": 45}  # keys are immutable
print(ss["ram"])
ss1 = {"Hindi": "Oh mere Humsafar", "English": "Oneday I'm gonna fly away"}
print(ss1["English"])
print("English" in ss1)  # Returns boolean
# print(ss1["urdu"]) KeyError is returned as there is no urdu key word
print(ss.get("ramesh", "not in dictionary"))  # get is same as indexing but can set default vaule instead
ss2 = {1: 1, 2: 1, 3: 2, 4: 3}
print(ss2.get(7, 10) + ss2.get(4, 5))  # as 7 is not there it takes 10 as default

cubes = [i ** 3 for i in range(5)]
print(cubes)

evens = [k ** 2 for k in range(10) if k ** 2 % 2 == 0]
print(evens)
