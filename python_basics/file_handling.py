f = open('writeFile.txt', 'r')  # Opening a file with read access
print(f.readline(150), end="")  # read first line
print(f.readline(12), end="")  # read first 10 characters
print(f.read(), end="")  # read everything in file

f1 = open('writeFile1.txt', 'w')  # Write access
f1.write('Want to test write function ')

f2 = open('writeFile1.txt', 'a')  # Append
f2.write(' here append function is been executed ')
f1.close()
f2.close()

f3 = open('writeFile1.txt')
print(f3.read())

f.close()
