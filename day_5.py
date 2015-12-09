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
