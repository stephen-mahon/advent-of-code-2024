def solve():
    with open("test_inputs/day01.txt") as f:
        data = [line.rstrip('\n') for line in f]
    
    # Solution logic    
    a_s = []
    b_s = []
    for line in data:
        a, b = map(int, line.split("   "))
        a_s.append(a)
        b_s.append(b)

    a_s.sort()
    b_s.sort()

    mapped_vals = dict()

    part1 = 0
    for i in range(len(b_s)):
        if b_s[i] in mapped_vals:
            mapped_vals[b_s[i]] += 1
        else:
            mapped_vals[b_s[i]] = 1
        part1 += abs(b_s[i] - a_s[i])
    
    part2 = 0

    for i in range(len(a_s)):
        if a_s[i] in mapped_vals:
            part2 += a_s[i] * mapped_vals[a_s[i]]

    return part1, part2