#prob 33
#digit cancelling fractions

import time
from decimal import *
from fractions import Fraction

start_time = time.time()

fracs = []
new_fracs = []
frac_prod = 1

def check_cancel(numer, denom):
	n = str(numer)
	d = str(denom)
	
	if len(n) == 1:
		n = '0'+n
		
	if len(d) == 1:
		d = '0'+d
	
	n1 = Decimal(n[0])
	n2 = Decimal(n[1])
	d1 = Decimal(d[0])
	d2 = Decimal(d[1])
	
	p = Decimal(numer)/Decimal(denom)
	# print numer, denom
	# print p
	# print n1, n2, d1, d2
	
	if numer == denom:
		return False
	elif n2 == d2 == 0:
		return False
	
	if (n1 > 0) and (d1 > 0) and n2 == d2 and ((n1/d1) == p):
		return True
	elif (n2 > 0) and (d1 > 0) and n1 == d2 and ((n2/d1) == p):
		return True
	elif (n1 > 0) and (d2 > 0) and n2 == d1 and ((n1/d2) == p):
		return True
	elif (n2 > 0) and (d2 > 0) and n1 == d1  and ((n2/d2) == p):
		return True
	else:
		return False

for numerator in xrange(10, 100):
	for denominator in xrange(numerator + 1, 100):
		if check_cancel(numerator, denominator):
			# print numerator, denominator
			fracs.append([numerator, denominator])
			
for f in fracs:
	frac_prod = frac_prod * (Decimal(f[0])/ Decimal(f[1]))
	
print Fraction(frac_prod)
	
print("--- %s seconds ---" % (time.time() - start_time))