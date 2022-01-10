def is_even(n):
	return (n/2)

def is_odd(n):
	return (3*n+1)
	
big = 0
bigcount = 0
for i in range(1, 1000000):
	count = 1
	x = i
	while x != 1:
		count += 1
		if x % 2 == 0:
			x = is_even(x)
		else:
			x = is_odd(x)
	if count > bigcount:
		big = i
		bigcount = count
	
print big, bigcount