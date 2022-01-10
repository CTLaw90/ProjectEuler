import math
import time

def is_prime(x):
	for i in range(2,(int(math.sqrt(x)))+1):
		if x % i == 0:
			return False		
			
	return True
	
def get_n(n, a, b):
	num = n**2 + a*n + b
	if num > 0:
		if is_prime(num):
			return get_n(n+1, a, b)
		else:
			return n
	else:
		return n
		
def main():
	max_n = 0
	max_a = 0
	max_b = 0
	for a in xrange(-1000,1000):
		for b in xrange(-1000, 1000):
			n = get_n(0, a, b)
			if n > max_n:
				max_n = n
				max_a = a
				max_b = b
				
	print max_a, max_b, max_n, max_a*max_b
	
start = time.clock()
main()
end = time.clock()
print "Time :" , end - start , "seconds"