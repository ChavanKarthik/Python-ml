max_value = 100


def find_state(pos):
    pos[0] = 0
    pos[1] = 0
    pos[2] = 1
    pos[3] = 1
    pos[4] = 1
    pos[5] = 1
    pos[6] = 1

    # find winner for other positions
    for i in range(7, max_value + 1):
        # if not (pos[i - 2] or (pos[i - 3]) or pos[i - 5]):
        if not (pos[i - 2]) or not (pos[i - 3]) or not (pos[i - 5]):
            pos[i] = 1
        else:
            pos[i] = 0


# driver function
N = int(input("Pls enter number of stones : "))
pos = [0] * (max_value + 1)

find_state(pos)

if pos[N] == 1:
    print("Alice is winner")
else:
    print("Bob is winner")
