x = ['20931', 'DHARARI KUND', '417', 'GANGOLIHAT', '605', 'PITHORAGARH', '33', 'Uttarakhand']


def dictionary_maker(x):
    dicter = {}
    for index, item in enumerate(x):
        if len(x) % 2 == 0:
            if index % 2 == 0:
                dicter[item] = 0
            else:
                dicter[x[index - 1]] = item
        else:
            print('Number of elements is not correct')
            break

    return dicter


def dictionary_maker3(x):
    dicter = {}
    index = 0
    for item in x:
        if index % 2 == 0:
            dicter[item] = 0
        else:
            dicter[x[index - 1]] = item
        index += 1

    return dicter


def dictionary_maker2(x):
    dicter = {}
    keys = []
    values = []
    for index, item in enumerate(x):
        if index % 2 == 0:
            keys.append(item)
        else:
            values.append(item)

    for i in range(0, len(keys)):
        dicter[keys[i]] = values[i]

    return dicter


print(dictionary_maker(x))
# print(dictionary_maker3(x))
# print(dictionary_maker2(x))
