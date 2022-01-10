#project euler prob 39
#integer right triangles

from math import sqrt

p = 1000

pSquares = [x**2 for x in xrange(0, p+2)]

triCount = [0 for x in xrange(p+1)]

for i in xrange(1, p):
	for j in xrange(i+1, p+1):
		k = pSquares[i] + pSquares[j]
		if k in pSquares:
			if (i + j + int(sqrt(k))) <= p:
				# print i,j, sqrt(k)
				# print pSquares[i], pSquares[j], k
				# print "-----------------"
				triCount[i + j + int(sqrt(k))] += 1
			
maxCount = max(triCount)
# print triCount
print [i for i, j in enumerate(triCount) if j == maxCount]