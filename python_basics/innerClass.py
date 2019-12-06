class Student:
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap = self.Laptop()

    def show(self):
        print(s1.name, s1.rollNo)
        self.lap.show()

    def dontShow(self):
        print('Student details are confidential')
        print('''Please don't mind''')

    class Laptop:
        def __init__(self):
            self.brand = 'Dell'
            self.processor = 'i5'
            self.ram = '16 GB'
            self.harddisk = '1 TB'

        def show(self):
            print(self.brand, self.processor, self.ram, self.harddisk)


s1 = Student('Naveen', 123)
s1.show()
