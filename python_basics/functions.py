# function is a collection of instructions or code.
def test1():  # defining a function
    print("Test function is executed")
    print("Passed")


test1()  # calling a function


def test2(x):  # With argument
    return x + 10  # output of function


a = test2(5)
print(a)


def test3(x, y):
    return x ** 2 + y ** 2 + 2 * x * y


b = test3(2, 5)
print(b)


def bmicalculator(name, height, weight):
    bmi = round(weight / (height ** 2))
    if bmi >= 25.0:
        return name + ' is over weight'
    elif bmi < 18.5:
        return name + " is Under weight"
    else:
        return name + " is Normal weight"


print(bmicalculator('manohar', 1.8, 75))
