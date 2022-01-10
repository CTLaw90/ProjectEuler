def is_prime(x):
	for y in range(2, x-1):
		if x % y == 0:
			return False
	else:
		return True

i = 0
j = 1
target = 10001
loop = True
while (i < target):
	while loop == True:
		j = j + 1
		if is_prime(j):
			break	
	
	i = i + 1
	
print i
print j