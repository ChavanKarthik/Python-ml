print("{0} {1} {0}".format("Hi", "Hello"))  # format replaces with {} params
print(" ,".join(["Hi", "How", "Ru?"]))  # joins params with ','
print("Hello Me".replace("Me", "World!"))  # replaces 'Me' param with 'World!'
print("This is Me!".startswith("This"))  # returns a boolean
print("This is Me!".endswith("Me!"))  # returns a boolean
print("This is Me!".upper())  # returns whole string in uppercase
print("This is Me!".lower())  # returns whole string in lower
print("This. is. Me!".split(". "))  # splits where '. ' is there
ss = tuple(range(0, 10))  # (0,1,2,3,4,5,6,7,8,9)
print(min(ss))  # (0)
print(max(ss))  # (9)
print(abs(-55))  # returns only int
print(sum(range(5)))  # returns sum of (0,1,2,3,4)

ss1 = [5, 6, 7, 8, 9, 10]
if any([i > 8 for i in ss1]):  # if any of the i is greater returns true
    print("one of the param  > 5")
if all([i > 4 for i in ss1]):  # if all of the i is greater returns true
    print("All of the param are > 5")
for v in enumerate(ss1):  # Returns indexes with value
    print(v)
