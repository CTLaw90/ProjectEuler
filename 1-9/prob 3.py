import math

num = 600851475143
sqrtnum = math.sqrt(num)
lpf = 1

def is_prime(x):
	for y in range(2, x-1):
		if x % y == 0:
			return False
	else:
		return True
			
		

for x in range(1,int(sqrtnum)):
	if num % x == 0:
		if is_prime(x):
			lpf = x
		
print lpf