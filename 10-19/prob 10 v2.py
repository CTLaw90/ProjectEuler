#second attempt using Sieve of Eratosthenes to test for primality

def sieve(x):
	a = [True] * x
	a[0] = False
	a[1] = False
	
	for (i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in range(i*i, x, i):
				a[n] = False
	
	
test_this = sieve(2000000)
sum = 0
for i in test_this:
	sum += i
		
print sum