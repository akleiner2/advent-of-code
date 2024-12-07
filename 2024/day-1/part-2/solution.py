def build_frequency(items): 
    frequency = {}
    for item in items:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

with open("input.txt", "r") as f:
    lines = [list(map(int, line.split())) for line in f.readlines()]
    left = [line[0] for line in lines]
    right = build_frequency([line[1] for line in lines])

similarity_score = 0
for item in left: 
    similarity_score += item * right.get(item, 0)

print(similarity_score)
