class Student:

    def sum(self, a, b):
        try:
            s = int(input('enter first number ')) / int(input('enter second number '))
            print('sum of given numbers is ', s)
        except ZeroDivisionError as e:
            print(e)
        except ValueError:
            print('invalid input')
        except Exception:
            print('Something went wrong')
        finally:
            print('sum method ended')


obj = Student()
obj.sum(1, 1)
