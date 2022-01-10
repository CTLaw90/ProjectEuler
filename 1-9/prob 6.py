sumsq = 0
sqsum = 0

for i in range(1, 101):
	sumsq += i**2
	
for i in range(1, 101):
	sqsum += i
	
sqsum = sqsum ** 2 

print sqsum - sumsq