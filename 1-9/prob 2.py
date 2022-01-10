sum = 0
x = 1
last_x = 1
last_x2 = 0
while (x < 4000000):
	if x % 2 == 0:
		sum += x
		x = last_x + last_x2
		last_x2 = last_x
		last_x = x
	else:
		x = last_x + last_x2
		last_x2 = last_x
		last_x = x
		
print sum