with open("data/day2.txt") as f:
    # Part 1
    num = 5
    code = ""

    left = [1, 4, 7]
    up = [1, 2, 3]
    right = [3, 6, 9]
    down = [7, 8, 9]

    for line in f:
        for char in line:
            if num in left and char == "L" or \
                num in right and char == "R" or \
                num in up and char == "U" or \
                num in down and char == "D":
                pass
            else:
                if char == "U":
                    num -= 3
                elif char == "D":
                    num += 3
                elif char == "L":
                    num -= 1
                elif char == "R":
                    num += 1

        code += str(num)

    print ("Part 1 code: %s") % code

with open("data/day2.txt") as f:
    # Part 2
    code = ""
    num = 5

    left = [5, 2, 1, 10, 13]
    up = [5, 2, 1, 4, 9]
    right = [1, 4, 9, 12, 13]
    down = [5, 10, 13, 12, 9]

    smaller_step = [3, 10]

    letter_map = {v:v for v in range(1, 10)}
    letter_map[10] = "A"
    letter_map[11] = "B"
    letter_map[12] = "C"
    letter_map[13] = "D"

    for line in f:
        for char in line:
            if num in left and char == "L" or \
                num in right and char == "R" or \
                num in up and char == "U" or \
                num in down and char == "D":
                pass
            else:
                if char == "U":
                    num = num - 4 if num is not 3 else (num - 2)
                elif char == "D":
                    num = num + 4 if num is not 11 else (num + 2)
                elif char == "L":
                    num -= 1
                elif char == "R":
                    num += 1

        code += str(letter_map[num])

    print ("Part 2 code: %s") % code
