def decor(x):  # takes x as print_text from line 10
    def wrap():
        print("123")
        x()  # calls args in line 1
        print("456")

    return wrap


def print_text():
    print("Hey Hi!")


decorated = decor(print_text)  # calls line 8
decorated()  # calls decor(print_text) in line 10


def print_text1():
    print("Hello world!")


print_text1 = decor(print_text1)
print(print_text1())
