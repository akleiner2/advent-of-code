f = open("data/day_5.txt")

nice = 0

# properties for each string
double_letter = False
bad_string = False
vowel_count = 0

vowels = ["a", "e", "i", "o", "u"]

bad_strings = ["ab", "cd", "pq", "xy"]

for line in f:
    prev_char = ''
    for char in line:
        if char in vowels:
            vowel_count += 1
        if char == prev_char:
            double_letter = True

        s = char + prev_char
        if s in bad_strings:
            bad_string = True

        prev_char = char

    if vowel_count >= 3 and double_letter and not bad_string:
        nice += 1

    double_letter, bad_string, vowel_count = False, False, 0

print (nice)

# Part 2
f.seek(0, 0)

def mid_two(string):
    for i in range(len(string)-1):
        if string.count(string[i:i+2]) >= 2:
            return True
    return False

def no_overlap(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

nice = 0

for line in f:
    if mid_two(line) and no_overlap(line):
        nice+=1

print (nice)
