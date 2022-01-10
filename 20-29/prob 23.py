import time


def sumdiv(x):
	divs =  [i for i in xrange(1, x/2 + 1) if x % i == 0]
	sum = 0
	for i in divs:
		sum += i
		
	return sum

def get_next_prop(max):
	y = 12
	while y < max:
		if sumdiv(y) > y:
			yield y
		y += 1
	
def main():	
	n = 28123
	table = [True]*(n+1)
	props = []
	sum = 0

	for next_prop in get_next_prop(n):
		props.append(next_prop)
		for i in props:
			if i + next_prop < n + 1:
				table[i + next_prop] = False

	for j in xrange(n+1):
		if table[j]:
			sum += j
			
	#for k in range(len(table)):
		#print k, table[k]
		
	print sum
	
start = time.clock()
main()
end = time.clock()
print "Time :" , end - start , "seconds"