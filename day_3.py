f = open("data/day_3.txt", "r")

# Part 1

start = (0, 0)
visited = {}

directions = f.readline() 

for direction in directions: 
    if start not in visited: 
        visited[start] = 1

    if direction == ">":
        start = (start[0] + 1, start[1])
    elif direction == "v":
        start = (start[0], start[1] - 1)
    elif direction == "<":
        start = (start[0] - 1, start[1])
    elif direction == "^":
        start = (start[0], start[1] + 1)

# Check the last possible value
if start not in visited: 
    visited[start] = 1

#print len(visited)


# Part 2
f.seek(0, 0)

santa = (0, 0)
robo = (0, 0)
temp = (0, 0)
visited = {}

for i, direction in enumerate(directions):
    if i%2 == 0: 
        temp = santa
    else: 
        temp = robo

    if temp not in visited: 
        visited[temp] = 1 
    
    if direction == ">":
        temp = (temp[0] + 1, temp[1])
    elif direction == "v":
        temp = (temp[0], temp[1] - 1)
    elif direction == "<":
        temp = (temp[0] - 1, temp[1])
    elif direction == "^":
        temp = (temp[0], temp[1] + 1)

    if i%2 == 0: 
        santa = temp
    else: 
        robo = temp

if santa or robo not in seek: 
    visited[santa] = 1
    visited[robo] = 1

print len(visited)
