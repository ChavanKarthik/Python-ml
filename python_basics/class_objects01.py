class Computer:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        print("Name   : {}\nAge    : {}\nHeight : {}".format(self.name, self.age, self.height))


obj1 = Computer('sai', 25, 5)
obj2 = Computer('ram', 65, 6)


# obj1.display()
# obj2.display2()

class Car:

    def __init__(self):
        self.brand = 'Skoda'
        self.model = 'Laura'

    def update(self):
        self.model = 'Laura Elegance'


c1 = Car()
c2 = Car()

c2.name = 'Rapid'
c2.model = 'High_End'

c1.update()
c2.update()


# print(c1.brand, c1.model)
# print(c2.brand, c2.model)

class School:
    def __init__(self):
        self.marks = 540
        self.rank = 'First_rank'


sch1 = School()
sch2 = School()

# print(sch1.marks,sch1.rank)
