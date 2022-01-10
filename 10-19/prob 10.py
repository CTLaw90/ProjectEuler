#runs in O(n**2) time. dont use this lol

def is_prime(x):
	for y in range(2, x-1):
		if x % y == 0:
			return False
	else:
		return True
		
sum = 0

for i in range(2, 2000000):
	if i % 10000 == 0:
		print "i: " + str(i)
		print "sum: " + str(sum)
	if is_prime(i) == True:
		sum += i
		
print sum