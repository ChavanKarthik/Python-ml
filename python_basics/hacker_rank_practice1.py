# to check whether a given series of string is present in a string
def count_substring(string, sub_string):
    return sum([1 for i in range(0, len(string) - len(sub_string) + 1)
                if (string[i:(len(sub_string) + i)] == sub_string)])


# print(count_substring('abcdcdc', 'cdc'))

# To check whether a given string has only alphabatical or both
s = 'aQ3'


# print((any(c.isalnum() for c in s)), '\n', (any(c.isalpha() for c in s)))

# Designer Door mat puzzle
# n, m = map(int,input("please enter two odd nums with space in b/w").split())  # example of args 5 15
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

# Print  lines where each line  (in the range ) contains the
# respective decimal, octal, capitalized hexadecimal, and binary values of .
# Each printed value must be formatted to the width of the binary value of .


def print_formatted(n):
    # your code goes here
    width = len("{0:b}".format(n))
    for i in range(1, n + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=width))


# print_formatted(15)


# Different sizes of alphabet rangoli
import string

alpha = string.ascii_lowercase

# n = int(input("Please enter a number : "))
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
# print('\n'.join(L[:0:-1] + L))

# print second largest number in a list

# arr = map(int, input('Enter set of numbers').split())
# arr = sorted(set(arr))
# print(arr[-2])


mark_sheet = []
for _ in range(0, int(input('no of students'))):
    mark_sheet.append([input('S_name'), float(input('Marks'))])

second_highest = sorted(list(set([marks for name, marks in mark_sheet])))[1]
print('\n'.join([a for a, b in sorted(mark_sheet) if b == second_highest]))
