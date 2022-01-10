#prob 34 v2
#digit factorials

# no strings attached!!

import time
start_time = time.time()

num_factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
tot_sum = 0


for x in xrange(10, 41000):
	num = x
	fac_sum = 0
	while num > 0:
		n = num % 10
		num = num / 10
		fac_sum += num_factorials[n]
	if fac_sum == x:
		print x
		tot_sum += x

		
print tot_sum




print("--- %s seconds ---" % (time.time() - start_time))