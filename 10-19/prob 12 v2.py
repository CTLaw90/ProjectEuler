import math
# codes pretty sloppy. for example with triangle number = 15 it reports only two div.
# this is because the int(math.sqrt(x)) rounds down, then the for loop doesnt actually 
# count that number. so for t = 15 it doesnt add two to divs for 3 and 5. when numbers
# get big this isnt a problem.

def get_next_tri():
	tri = 0
	n = 1
	while n:
		tri += n
		print tri
		yield tri
		n += 1
		
def get_div(n):
	divs = 2
	if n == 1:
		return 1
	if n == 2:
		return divs
	if n > 2:
		for i in range(2, int(math.sqrt(n))):
			if n % i == 0:
				divs += 2
	return divs

div = 0
cyc = 1

for i in get_next_tri():
	div = get_div(i)
	if div > 500:
		break
	cyc += 1