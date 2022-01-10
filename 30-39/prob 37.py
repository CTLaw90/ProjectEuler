#prob 37
#truncatable primes

import time
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

def is_l_trunc(num):
	num_str = str(num)
	
	new_num = ''
	
	for i in xrange(1, len(num_str)):
		new_num = num_str[i:]
		if int(new_num) in primes_list:
			continue
		else:
			return False
			
	return True
		
def is_r_trunc(num):
	num_str = str(num)
	
	new_num = ''
	
	for i in xrange(len(num_str)-1, 0, -1):
		new_num = num_str[:i]
		if int(new_num) in primes_list:
			continue
		else:
			return False
			
	return True
		
		
sum = 0

for x in primes_list:
	if x < 10:
		continue
		
	if is_l_trunc(x) and is_r_trunc(x):
		print x, " is a truncatable prime!"
		sum += x
		
print sum

print '---',start_time - time.time(), ' seconds!---'