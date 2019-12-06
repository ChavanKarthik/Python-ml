file = open("sample_csv.csv", "r")  # Open a file
a = file.read()  # Get all data to 'a'
file.close()
print(a)


def data_cleaner(a):
    word_array = []

    for word in a.split(','):
        word = word.strip()
        if word is not '':
            word_array.append(word)
    return word_array


v = data_cleaner(a)
print(v)
# print (", ".join(v))

# for i in range(7,9):
# for j in range(1,11):
# print(f"{i}*{j}={i*j}")
