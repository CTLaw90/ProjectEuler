n = 100
fac = 1
str_fac = ""
sum = 0

for i in xrange(n, 1, -1):
	fac = fac * i
	
str_fac = str(fac)

for char in str_fac:
	sum += int(char)
	
print sum
