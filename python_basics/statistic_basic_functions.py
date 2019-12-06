# list of random numbers
# x = random.sample(range(1, 1000), 15)
x = [370, 877, 575, 11, 895, 377, 574, 88, 800, 825, 222, 411, 396, 885, 857, 633]


# print(x)


# to find the sum
def total(x):
    summ = 0
    for i in x:
        summ = i + summ
    return summ


# print(total(x))

# to find mean (average)
def average(x):
    y = 0
    y = total(x) / len(x)
    return y


# print(average(x))

# To find median
def median(x):
    x = sorted(x)
    if len(x) % 2 != 0:
        medean = x[(len(x)) // 2]
    else:
        m = int(((len(x)) / 2) + 0.5)
        n = int(((len(x)) / 2) - 0.5)
        medean = (x[m] + x[n]) / 2
    return medean


# print(median(x))

# to find range of a list
def range1(x):
    x = sorted(x)
    range1 = x[-1] - x[0]
    return range1

# print(range1(x))
