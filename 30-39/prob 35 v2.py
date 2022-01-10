#prob 35 v2
#circular primes

import time
from copy import copy
start_time = time.time()

#Using sieve of Eratosthenes algorithm to find primes

def sieve(x):
	a = [True] * x
	a[0] = False
	a[1] = False
	
	for (i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in range(i*i, x, i):
				a[n] = False
	
	
primes = sieve(1000000)
primes_list = []

for i in primes:
	primes_list.append(i)
		
# print primes_list

#Function to find all permutations of characters in a number string
def find_circ(num):

	circ_list = build_circ(str(num))
	
	# print circ_list

	for circ in circ_list:
		if circ not in primes_list:
			# print '\n', circ, 'not in!', '\n'
			return False
		
	return True
	
def build_circ(circ_str):
	
	rot_list = []
	
	for i in xrange(len(circ_str), 0, -1):
		new_rot = []
		for j in xrange(len(circ_str)):
			new_rot.append(circ_str[j-i])
		
		rot_list.append(int(''.join(new_rot)))

				
	return rot_list
			
	
circ_primes = []

for x in primes_list:
	if len(str(x)) == 1:
		circ_primes.append(x)
	else:
		if find_circ(x):
			circ_primes.append(x)

print circ_primes
print len(circ_primes)


print("--- %s seconds ---" % (time.time() - start_time))