f = open("data/day_2.txt")

# Part 1

def surface_area(w, l, h):
    return 2*w*l + 2*w*h + 2*l*h

def min_area(w, l, h): 
    vals = [w, l, h]
    vals.sort()
    return vals[0] * vals[1]

area = 0
for line in f: 
    dims = [int(num) for num in line.split("x")]
    w, l, h = dims[0], dims[1], dims[2]
    area = area + surface_area(w, l, h) + min_area(w, l, h)

print (area)

# Part 2

f.seek(0, 0)

def min_perimeter(w, l, h): 
    vals = [w, l, h]
    vals.sort()
    return 2 * vals[0] + 2 * vals[1]

def volume(w, l, h):
    return w*l*h

rope = 0
for line in f: 
    dims = [int(num) for num in line.split("x")]
    w, l, h = dims[0], dims[1], dims[2]
    rope += min_perimeter(w, l, h) + volume(w, l, h)

print (rope)