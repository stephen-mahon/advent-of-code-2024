from utils.utils import parse_input


def solve():
    with open("test_inputs/day02.txt") as f:
        data = [line.rstrip('\n') for line in f]

    part1 = 0
    part2 = 0
    for line in data:
        if check_safety_level(line.split()):
            part1 += 1
        if problem_dampener(line.split()):
            part2 += 1

    return (part1, part2)


def cast_int_array(line):
    # cast as int
    arr = []
    for i in line:
        arr.append(int(i))
    
    return arr


def problem_dampener(line):
    # cast as int
    arr = cast_int_array(line)

    # if the array is fine, return true
    if check_safety_level(line):
        return True
    
    # iterate through the array removing an element
    for i in range(len(arr)):
        # test again
        new_arr = arr[:i] + arr[i+1:]
        if check_safety_level(new_arr):
            return True

    return False


def check_safety_level(line):
    # cast the array of strings to an array of ints
    arr = cast_int_array(line)
    
    # check to see if the array is strickly assending or strickly desending
    if not(arr == sorted(arr) or arr == sorted(arr, reverse=True)):
        return False

    for i in range(1, len(arr)):
        delta = abs(int(arr[i-1]) - int(arr[i]))
        # Any two adjacent levels differ by at least one and at most three
        if delta == 0 or delta > 3:
            return False

    return True