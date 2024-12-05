from utils.utils import parse_input, strip_new_lines

def solve():
    arr = parse_input("test_inputs/day05.txt")
    data = strip_new_lines(arr)

    page_ordering_rules = []
    updates = []

    new_line = False
    for line in data:
        if line == "":
            new_line = True
            continue 

        if (new_line):
            updates.append(line)
        else:
            page_ordering_rules.append(line)
    
    for i in range(len(page_ordering_rules)):
        page_ordering_rules[i] = page_ordering_rules[i].split("|")
    
    for i in range(len(updates)):
        updates[i] = updates[i].split(",")
    
    ans1 = part1(page_ordering_rules, updates)
    ans2 = part2(page_ordering_rules, updates)

    return ans1, ans2


def part1(rules, updates):
    correct_updates = []
    for update in updates:
        if right_order(rules, update):
            correct_updates.append(update)
    
    total = 0
    for update in correct_updates:
        total += middle_value(update)

    return total


def right_order(rules, update):
    for i in range(len(update)):
        for pair in rules:
            if str(update[i]) == pair[0] and pair[1] in update[:i]:
                return False

    return True


def part2(rules, updates):
    incorrect_updates = []
    for update in updates:
        if not right_order(rules, update):
            incorrect_updates.append(update)

    total = 0
    for update in incorrect_updates:
        update = corrected_order(rules, update)
        total += middle_value(update)

    return total


def corrected_order(rules, update):
    for i in range(len(update)):
        for pair in rules:
            if str(update[i]) == pair[0] and pair[1] in update[:i]:
                update = swap_index(i, update.index(pair[1]), update)
                corrected_order(rules, update)

    return update


def swap_index(i, j, arr):
    first = arr[i]
    second = arr[j]
    arr[i] = second
    arr[j] = first

    return arr


def middle_value(arr):
    middle_index = int(len(arr)/2)

    return int(arr[middle_index])