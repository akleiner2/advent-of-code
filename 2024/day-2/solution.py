def strictly_increasing(list):
    return all(list[i] < list[i + 1] for i in range(len(list) - 1))

def strictly_decreasing(list):
    return all(list[i] > list[i + 1] for i in range(len(list) - 1))

def each_report_within_range(list):
    return all(abs(list[i] - list[i + 1]) >= 1 and abs(list[i] - list[i + 1]) <= 3 for i in range(len(list) - 1))

def is_valid(list):
    return (strictly_increasing(list) or strictly_decreasing(list)) and each_report_within_range(list)

def can_remove_element_to_be_valid(list):
    for i in range(len(list)):
        list_without_i = list[:i] + list[i+1:]
        if is_valid(list_without_i):
            return True
    return False

with open("input.txt", "r") as f:
    lines = [list(map(int, line.split())) for line in f.readlines()]

# part 1
print(len(list(filter(lambda r: is_valid(r), lines))))

# part 2
print(len(list(filter(lambda r: is_valid(r) or can_remove_element_to_be_valid(r), lines))))
