#did this just as a project to work on recursion. the previous solution not only works but is pretty efficent
#could probably get this to work if i increase the max recursion depth but its already for less efficent then the other solution, so i dont see a point


import time
import math

start = time.clock()


def fib(a, b):
	#a = fibs[x-2], b = fibs[x-1], c = fibs[x]
	c = a + b
	a = b
	b = c
	size = int(math.log10(c))+1
	if size == 1000:
		print c
	else:
		fib(b, c)

fib(1,1)
	
end = time.clock()

print "Time : ", end - start, " seconds"
