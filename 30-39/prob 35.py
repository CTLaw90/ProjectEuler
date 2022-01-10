#prob 35
#circular primes


#This was built on a missunderstanding of circular primes. I had assumed circular primes meant
#all permutations of numbers in a prime had to create a prime number, instead of the original
#number just being rotated. I used recursion in build_circ() to create a list of all the possible
#assemblies of digits in any given number.

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
	
	
primes = sieve(10000)
primes_list = []

for i in primes:
	primes_list.append(i)
		
print primes_list

#Function to find all permutations of characters in a number string
def find_circ(num):
	list_char = []
	
	for char in str(num):
		list_char.append(int(char))
	
	circ_list = build_circ([], list_char)
	
	# print circ_list

	for circ in circ_list:
		if circ not in primes_list:
			# print '\n', circ, 'not in!', '\n'
			return False
		
	return True
	
def build_circ(cur, remaining):
	new_list = []

	if len(remaining) == 1:
		new_circ = []
		cur.append(remaining[0])
		new_circ.append(int(''.join(map(str, cur))))
		return new_circ
		
	else:
		for char in remaining:
			new_cur = copy(cur)
			new_cur.append(char)
			new_rem = copy(remaining)
			new_rem.pop(new_rem.index(char))
			new_num = build_circ(new_cur, new_rem)
			
			# print remaining, char, new_num, new_list

				
			for item in new_num:
				new_list.append(item)
				
		return new_list
			
	
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