def parse_input(file_path):
    with open(file_path, "r") as f:
        return f.readlines()

def strip_new_lines(arr):
    new_arr = []
    for line in arr:
        new_arr.append(line.strip("\n"))
    
    return new_arr