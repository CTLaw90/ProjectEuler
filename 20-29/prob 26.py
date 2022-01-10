#Euler prob 26
#Reciprocal cycles

import time
from decimal import *

start_time = time.time()

getcontext().prec = 3000

longest = [0, 0] #[x, cycle]

def find_cycle(float_string, x):
	for i in xrange(1, len(float_string)):
		for j in xrange(len(float_string)+1):
			if (i+j+i) < (len(float_string)+1):
				# print 'comparing ', float_string[j:i+j], float_string[j+i:i+j+i]
				if float_string[j:i+j] == float_string[j+i:i+j+i]:
					cycle = int(float_string[j:i+j])
					# print 'MATCH FOUND', cycle
					if cycle > longest[1]:
						longest[0] = x
						longest[1] = cycle
					if 	float_string[j:i+j] == float_string[j+i+i:i+j+i+i] == float_string[j+3*i:i+j+3*i]:	#to get rid of single repeating digits and not double digits part of a larger cycle.... not the best solution.
						return
	return


			
for x in xrange(1, 1000):
	y = Decimal(1) / Decimal(x)
	
	recip_string = str(y)
	recip_string = recip_string.strip('0.')
	
	
	find_cycle(recip_string, x)



print longest

print("--- %s seconds ---" % (time.time() - start_time))