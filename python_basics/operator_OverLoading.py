class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3


s1 = Student(5, 6)
s2 = Student(10, 11)

s3 = s1 + s2

print(s3.m1, s3.m2)


class Badminton:
    def tactics(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        return m1, m2

    def __add__(self, other):
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        r3 = Badminton(r1, r2)
        return r3


# s1 = Badminton()
# s2 = Badminton()
# s3 = Badminton()
# obj1 = s1.tactics(45,55)
# obj2 = s2.tactics(25,35)
# onj3 = s3.__add__(obj1+obj2)
# print(obj1, obj2)
# print(s3)

class Teacher:
    def __init__(self, a1, a2, ):
        self.a1 = a1
        self.a2 = a2

    def __add__(self, other1, other2):
        b1 = self.a1 + other1.a1 + other2.a1
        b2 = self.a2 + other1.a2 + other2.a2
        b3 = Teacher(b1, b2)
        return b3


p1 = Teacher(1, 1)
p2 = Teacher(9, 9)
p3 = Teacher(8, 8)

p4 = p1 + p2
print(p4.m1)
