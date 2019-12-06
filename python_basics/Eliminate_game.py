# starting_number = int(input("please enter Starting number :"))
ending_number = int(input("please enter Ending number :"))
list1 = [x for x in (range(0, ending_number + 1))]


def eliminate_Numbers(list2, skip=True):
    new_list = []  # get the iterated list
    if len(list2) == 1:  # stop when single stop is left
        print(list2[0])
    else:
        for i in list2:
            if not skip:  # skip value is false
                new_list.append(i)  # take the number
            skip = not skip  # alter the skip value

        eliminate_Numbers(new_list, skip)  # recursion

# eliminate_Numbers(list1)
