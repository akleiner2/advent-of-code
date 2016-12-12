"""
Helper functions for getting info and performing actions
"""
def extract_info(line):
	action = ""
	lower_bound = (0, 0)
	upper_bound = (999, 999)
	parts = line.split("through")

	lower_index = 2	
	# Determine the action. This can all really be consolodated tbh. 
	if "toggle" in parts[0]:
		action = "toggle"
		lower_index = 1
	elif "turn on" in parts[0]:
		action = "on"
	else:
		action = "off"

	# Determine the limits of the lights. This would be so much easier if I used RegEx.
	upper_lower, upper_upper = tuple(int(x) for x in parts[1].split(","))
	lower_lower, lower_upper = tuple(int(x) for x in parts[0].split()[lower_index].split(","))

	upper_bound = (upper_lower, upper_upper)
	lower_bound = (lower_lower, lower_upper)

	return action, lower_bound, upper_bound

def do_lights(grid, action, lower, upper):
	for i in range(lower[0], upper[0]+1): 
		for j in range (lower[1], upper[1]+1):
			if action == "off":
				grid[i][j] = 0
			elif action == "on":
				grid[i][j] = 1
			elif action == "toggle":
				if grid[i][j] == 0:
					grid[i][j] = 1
				else: 
					grid[i][j] = 0

def do_lights_2(grid, action, lower, upper): 
	for i in range(lower[0], upper[0]+1): 
		for j in range (lower[1], upper[1]+1):
			if action == "off":
				grid[i][j] = max(grid[i][j]-1, 0)
			elif action == "on":
				grid[i][j] += 1
			elif action == "toggle":
				grid[i][j] += 2

def count_lights(grid):
	count = 0 
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				count += 1 
	return count

def count_lights_2(grid):
	count = 0 
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			count += grid[i][j]
	return count

f = open("./data/day_6.txt", "r")
# Part 1
grid = [[0 for col in range(1000)] for row in range(1000)]

for line in f: 
	action, lower, upper = extract_info(line)
	do_lights(grid, action, lower, upper)

print (count_lights(grid))

# Part 2
f.seek(0, 0)
grid = [[0 for col in range(1000)] for row in range(1000)]

for line in f: 
	action, lower, upper = extract_info(line)
	do_lights_2(grid, action, lower, upper)

print (count_lights_2(grid))
