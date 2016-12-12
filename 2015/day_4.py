from hashlib import md5

# Part 1
i = 0
while not md5('bgvyzdsv{}'.format(i)).hexdigest().startswith('00000'):
    i += 1     

print i

# Part 2
i = 0
while not md5('bgvyzdsv{}'.format(i)).hexdigest().startswith('000000'):
    i += 1 

print i