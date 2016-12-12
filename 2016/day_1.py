# Tuple of (cur_direction, turn) => next_direction
next_direction = {
    ("N", "L"): "W",
    ("N", "R"): "E",
    ("S", "L"): "E",
    ("S", "R"): "W",
    ("E", "L"): "N",
    ("E", "R"): "S",
    ("W", "L"): "S",
    ("W", "R"): "N"
}

found = False

with open("data/day1.txt", "r") as f:
    x = 0
    y = 0
    direction = "N"
    my_input = f.readline()
    my_input = map(lambda x: (x.strip()[0], int(x.strip()[1:])), my_input.split(","))
    visited = {}

    for instruction in my_input:
        turn = instruction[0]
        amt = instruction[1]
        direction = next_direction[(direction, turn)]

        if direction == "W" or direction == "S":
            amt *= -1

        if direction == "N" or direction == "S":
            for val in range(y, y+amt+1, amt):
                if (x, val) in visited:
                    found = True
                else:
                    visited[(x, val)] = 1
            y += amt

        if direction == "E" or direction == "W":
            for val in range(x, x+amt+1, amt):
                if (val, y) in visited:
                    found = True
                else:
                    visited[(val, y)] = 1
            x += amt
