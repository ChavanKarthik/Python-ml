# You have a record of  students. Each record contains the student's name, and their percent marks in Maths,
# Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and
# marks for students. You are required to save the record in a dictionary data type. The user then enters a student's
# name. Output the average percentage marks obtained by that student, correct to two decimal places.


# n = int(input('number of students'))
# student_marks = {}
# for student in range(n):
#     name, *line = input('enter name and marks').split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input('student name for avg')
# marks = student_marks[query_name]
# total = 0.0
# for i in range(len(marks)):
#     total += marks[i]
# average = total / len(marks)
# print("{0:.2f}".format(average))


# A valid UID must follow the rules below:
#
# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits (0 - 9)
# It should only contain alphanumeric characters ( a-z , A - Z &  0-9 ).
# No character should repeat.
# There must be exactly 10 characters in a valid UID.

# for _ in range(int(input())):
#     u = ''.join(sorted(input()))
#     try:
#         assert re.search(r'[A-Z]{2}', u)
#         assert re.search(r'\d\d\d', u)
#         assert not re.search(r'[^a-zA-Z0-9]', u)
#         assert not re.search(r'(.)\1', u)
#         assert len(u) == 10
#     except:
#         print('Invalid')
#     else:
#         print('Valid')


def merge_the_tools(string, k):
    ind = [l for l in range(0, len(string) + 1, k)]
    unsetEl = ([string[ind[i]:ind[i + 1]] for i in range(0, len(ind) - 1)])
    setEl = []
    for j in unsetEl:
        setEl.append(set(j))
    for h in range(len(setEl)):
        print(''.join(setEl[h]))


# merge_the_tools('AABCAAADA', 3)

N = ([input('enter a number : ').split() for _ in range(2)])
print(N)
