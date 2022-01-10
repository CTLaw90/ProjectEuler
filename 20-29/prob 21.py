def sum_of_div(x):
	sumdiv = 0
	for i in xrange(1, x):
		if x % i == 0:
			sumdiv += i
			
	return sumdiv
		
sum_of_am = 0

for i in xrange(1, 10000):
	if (i == sum_of_div(sum_of_div(i))) and ( i != sum_of_div(i)):
		sum_of_am += i
		
print sum_of_am
