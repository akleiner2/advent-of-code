import operator

with open("data/day4.txt") as f:
    rooms = []
    for room in f:
        parts = room.rstrip().split("-")
        num_and_check = parts[len(parts)-1]

        name = ''.join(parts[:-1])

        index = num_and_check.index("[")
        room = int(num_and_check[:index])
        checksum = num_and_check[index+1:-1]

        letters = {}
        for letter in name:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1

        letters = sorted(letters.items(), key=operator.itemgetter(1), reverse=True)
        for i in range(len(checksum)):
            check = checksum[i]
            if letters[i][0] == check:
                rooms.append(room)

    print (sum(rooms))
