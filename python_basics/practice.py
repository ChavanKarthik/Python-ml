list1 = ['asdf', 'sd', 's', 'd', 'df', 'r', 'h', 'u', '6', 'w', 'qw', 'r', 'h', 'u', '6', 'w', 'qw']

list2 = [x * x for x in range(10)]
print(sum(list2[5:-2]))


def sel_sum(list1):
    total = 0
    for i in range(5, len(list1) - 2):
        total = total + list1[i]
    return total


def single_digit(list1):
    new_list = []
    for i in range(len(list1)):
        if len(list1[i]) == 1:
            new_list.append(list1[i])
    return new_list


# print(list1[5:-8:])
print(sel_sum(list2))
