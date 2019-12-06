# Types of Methods : 
class Cars:
    company = 'BMW'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # Instance method
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getBrand(cls):  # Class method
        return cls.company

    @staticmethod
    def catogory():  # Static method
        print('This is a Automobiles company')


s1 = Cars(55, 66, 77)  # creating objects
s2 = Cars(22, 33, 44)

print(s1.avg())
print(Cars.getBrand())
Cars.catogory()
