file = open("/home/beehyv/Downloads/python/writeFile.txt", "w")  # creates new file
file.write("Add text to a file. ")  # writes text to file
file.write("Second write function")
file = open("/home/beehyv/Downloads/python/writeFile.txt", "r")
print(file.read())
file.close()
