import re 
import functools

with open("input.txt", "r") as f:
    instructions = f.read()
    matches = [list(map(int, match)) for match in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", instructions)]
    print(functools.reduce(lambda acc, x: acc + x[0] * x[1], matches, 0))

def process_matches(matches):
    result = []
    enabled = True 
    for match in matches: 
        if match == "don't()":
            enabled = False 
        elif match == "do()":
            enabled = True 
        else:
            if enabled:
                result.append(match)
    return result

def execute_instruction(instruction):
    numbers = re.findall(r"(\d+)", instruction)
    if len(numbers) == 2:
        return int(numbers[0]) * int(numbers[1])
    return 0

with open("input.txt", "r") as f:
    instructions = f.read()
    matches = re.findall(r"(?:mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", instructions)
    print(functools.reduce(lambda acc, x: acc + execute_instruction(x), process_matches(matches), 0))
