def longest_pal_sub_string(input_str):
    pals = []
    length = len(input_str)
    if length > 1000000:
        print('invalid input')
        return
    else:
        for i in range(length):
            for j in range(length):
                if i - j % 2 == 0:
                    if i > j:
                        if input_str[i:j] % 2 == 0:
                            if input_str[i:j].reverse():
                                pals.append(input_str[i:j])

    return max(pals, key=len)


if __name__ == '__main__':
    input_str = str(input('please the input to find strongest palindrome'))
    longest_pal_sub_string(input_str)
