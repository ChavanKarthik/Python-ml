def finder(x):
    answer = 0
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if int(str(i) + str(i)) + int(str(j) + str(j)) + int(str(k) + str(k)) == int(str(i) + str(j) + str(k)):
                    answer = int(str(i) + str(j) + str(k))
                    print(answer)


finder(1)
