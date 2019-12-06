import statistic_basic_functions as super_class

y = [370, 877, 575, 11, 895, 377, 574, 88, 800, 825, 222, 411, 396, 215, 87, 633]


# print(y)

def quartiles(y):
    y = sorted(y)
    bucket_1 = y[:len(y) // 4]
    quartile1 = super_class.median(bucket_1)
    bucket_2 = y[len(y) // 4:len(y) // 2]
    quartile2 = super_class.median(bucket_2)
    bucket_3 = y[len(y) // 2:(len(y) - len(y) // 4)]
    quartile3 = super_class.median(bucket_3)
    bucket_4 = y[(len(y) - len(y) // 4): len(y)]
    quartile4 = super_class.median(bucket_4)
    IQR = y[(len(y) - len(y) // 4) - len(y) // 4]
    return bucket_1, bucket_2, bucket_3, bucket_4, IQR, quartile1, quartile2, quartile3, quartile4


# print(quartiles(y))

print(sorted(y))


def variance(y):
    mean = int(super_class.average(y))
    s_diff = [abs(i - mean) * abs(i - mean) for i in y]
    v = (sum(s_diff) / len(y) - 1)
    return v


def standard_deviation(y):
    sd = round(variance(y) ** 0.5, 2)
    return sd


print(f'variance : {variance(y)}')
print(f'standard deviation : {standard_deviation(y)}')
