file = open("sample_csv.csv")
file_content = file.read()
print(file_content)
file.close()


def csv_cleaner(a):
    word_array = []
    for word in a.split(','):
        word = word.strip()
        if word is not '':
            word_array.append(word)
    return word_array


print(csv_cleaner(file_content))
