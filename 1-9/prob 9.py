import math

zsq = 1
z = 1 
nips = 1
for x in range(-500, 500):
	for y in range(x+1, 501):
		zsq = (x**2) + (y**2)
		z = math.sqrt(zsq)
		if z % 1 == 0:
			print "x: " + str(x) + " y: " + str(y) + " z: " + str(z)
		if (x + y + z) == 1000:
			nips = x*y*z
			print "#############################################################"
			break
			
print nips