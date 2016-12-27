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

        # Part 1
        rank = sorted([-letters[c],c] for c in letters.keys())
        rankstr = ''.join(rank[x][1] for x in xrange(min(5,len(rank))))

        if rankstr == checksum:
            rooms.append(room)

        # Part 2
        a = ord("a")
        msg = ""
        name = " ".join(parts[:-1])
        for c in name:
            if c != " ":
                msg += chr((ord(c)-a+room)%26 + a)

        if msg == "northpoleobjectstorage":
            print (room)

    print (sum(rooms))
