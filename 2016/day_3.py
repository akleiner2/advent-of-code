def is_valid(x, y, z):
    return (x+y) > z and (y+z) > x and (x+z) > y

with open("data/day3.txt", "r") as f:
    num_valid = 0
    for vals in f:
        vals = map(int, vals.split())
        if is_valid(vals[0], vals[1], vals[2]):
            num_valid += 1

    print ("Part 1: %d") % (num_valid)

with open("data/day3.txt", "r") as f:
    num_valid = 0
    vals = []
    for nums in f:
        nums = map(int, nums.split())
        vals.append(nums)

    for i in range(0, len(vals)-2, 3):
        first = vals[i]
        second = vals[i+1]
        third = vals[i+2]

        for j in range(3):
            if is_valid(first[j], second[j], third[j]):
                num_valid += 1

    print ("Part 2: %d") % num_valid
