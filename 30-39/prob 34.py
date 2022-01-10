#prob 34
#digit factorials

import time
start_time = time.time()

num_factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
tot_sum = 0

def factorialize_digits(n):
	num_string = str(n)
	fac_sum = 0
	for char in num_string:
		fac_sum += num_factorials[int(char)]
	
	if fac_sum == n:
		return True
		
	else:
		return False

for x in xrange(10, 10000000):
	if factorialize_digits(x):
		print x
		tot_sum += x
		
print tot_sum




print("--- %s seconds ---" % (time.time() - start_time))