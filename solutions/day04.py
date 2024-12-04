from utils.utils import parse_input, strip_new_lines

def solve():
    arr = parse_input("test_inputs/day04.txt")
    data = strip_new_lines(arr)
    part1 = word_search(data, "XMAS")
    part2 = x_mas_search(data)
    return (part1, part2)

def word_search(grid, check):
    total = 0

    row = len(grid)
    col = len(grid[0])
    offset = len(check)

    # Horizontals
    for line in grid:
        for i in range(0, len(line) - offset + 1):
            word = line[i:i + offset]
            if word == check or word[::-1] == check:
                total += 1
    
    # Verticals
    for j in range(col):
        line = ""
        for i in range(row):
            line += grid[i][j]
        for i in range(0, len(line) - offset + 1):
            word = line[i:i + offset]
            if word == check or word[::-1] == check:
                total += 1

    # Diagonal-Right
    for i in range(0, row - offset + 1, 1):
        for j in range(0, col - offset + 1, 1):
                word = ""
                for k in range(offset):
                    word += grid[i+k][j+k]
                if word == check or word[::-1] == check:
                    total +=1

    # Diagonal-Left
    for i in range(0, row - offset + 1, 1):
        for j in range(offset-1, col, 1):
                word = ""
                for k in range(offset):
                    word += grid[i+k][j-k]
                if word == check or word[::-1] == check:
                    total += 1
    
    return total

def x_mas_search(grid):
    total = 0

    row = len(grid)
    col = len(grid[0])

    for i in range(1, row-1):
        for j in range(1, col-1):
            if grid[i][j] == 'A':
                if diagonal_check(grid, i, j):
                    total+=1

    return total

def diagonal_check(grid, x, y):
    # a  .  b
    # . x,y .
    # d  .  c
    # possible combinations clockwise from top-left
    # M M S S, S M M S, S S M M, S A A S
    a = grid[x-1][y-1]
    b = grid[x+1][y-1]
    c = grid[x+1][y+1]
    d = grid[x-1][y+1]
    
    if a == "M" and b == "M" and c == "S" and d == "S":
        return True
    
    if a == "S" and b == "M" and c == "M" and d == "S":
        return True
    
    if a == "S" and b == "S" and c == "M" and d == "M":
        return True
    
    if a == "M" and b == "S" and c == "S" and d == "M":
        return True
    
    return False