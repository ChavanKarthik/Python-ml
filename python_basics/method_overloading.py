class Student:
    # def __init__(self,m1,m2):
    # 	self.m1=m1
    # 	self.m2=m2

    def addition(self, a=0, b=0, c=0):
        s = 0
        s = a + b + c
        return s


s1 = Student()  # (11,22)
print(s1.addition(12, 14))
