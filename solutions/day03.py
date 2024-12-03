import re
from utils.utils import parse_input

def solve():
    data1 = parse_input("inputs/day03.txt")
    data2 = parse_input("inputs/day03.txt")
    return (part1(str(data1)), part2(str(data2)))


def part1(data):
    pattern = r"mul[\(](\d+),(\d+)[\)]"
    matches = re.findall(pattern, data)

    number_pairs = [(int(num1), int(num2)) for num1, num2 in matches]

    total = 0
    for pair in number_pairs:
        total += pair[0] * pair[1]

    return total

def part2(data):
    pattern = r"mul[\(]\d+,\d+[\)]|do\(\)|don't\(\)"
    matches = re.findall(pattern, data)

    mul_bool = True
    total = 0
    for match in matches:
        if match == "don't()":
            mul_bool = False
            continue
        if match == "do()":
            mul_bool = True
            continue
        if mul_bool:
            matches = re.findall(r"mul[\(](\d+),(\d+)[\)]", match)
            number_pairs = [(int(num1), int(num2)) for num1, num2 in matches]
            total += number_pairs[0][0] * number_pairs[0][1]
    
    return total