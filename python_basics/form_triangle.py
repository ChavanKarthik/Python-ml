w = 10

for x in range(w):  # To initiate a
    for z in range(w - x):  # To print *'s' in Ascending order
        print(' ', end="")  # To print White spaces
    for y in range(x):
        print('* ', end="")
    print()

# for i in range(4):
#     for j in range(4):
#         if i < 3:
#             print('^ ', end=" ")
#         else:
#             print('^ ')
#             break
