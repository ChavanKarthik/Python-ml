# ss=open("/home/beehyv/Downloads/python/python_basics/file_operations.py") #To open a file
# ss=open("/home/beehyv/Downloads/python/python_basics/file_operations.py","r") #To open a file with read permission
# ss=open("/home/beehyv/Downloads/python/python_basics/file_operations.py","wb") #To open a file with binary write permission
# ss=open("/home/beehyv/Downloads/python/python_basics/file_operations.py","rb") #To open a file with binary read permission
# ss=open("/home/beehyv/Downloads/python/python_basics/file_operations.py","w") #To open a file with write permission
ss = open("/home/beehyv/Downloads/python/python_basics/readFile.txt", 'r')
fileContent = ss.read()  # returns whole file data
ss2 = ss.read(15)  # returns only first 15 chars
# print(fileContent)
for line in fileContent.split(' '):  # returns one character in one line
    print(line)
ss.close()
