ss = ("one", "two", "Three")  # Tuples are immutable and use ()
ss1 = {"1": "One", "2": "Two", "3": "Three"}  # Dictionaries use {}
ss2 = ["One", "Two", "Three"]  # Lists are mutable and use []

ss3 = (1, 2, (3, 4), (5, (6, 7), 8, 9))
print(ss3[3][1])  # Indexing for calling is same as list
ss4 = (range(0, 12, 1))  # start range from '0' till '11' with 1 number difference
print(ss4[2:5])  # start from 3rd parameter till 5th
print(ss4[2:-1])  # start from 3rd till last but one
print(ss4[7:5:-1])  # start from 6th and 7th

assert 2 + 5 == 7  # returns Boolean
print("2+5=7")
temperature = 10
assert (temperature >= 0)
print("greater than zero")
