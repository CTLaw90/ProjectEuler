#prob 32
#pandigital products

import time

start_time = time.time()

prod_sum = 0
pan_digits = []


def read_string(string):
	num_dict = {}
	for char in string:
		if char in num_dict:
			return False
		
		else:
			num_dict[char] = 1
	
	if '0' in num_dict:
		return False
	
	for x in xrange(1, 10):
		if str(x) not in num_dict:
			return False
			
	
	return True
	
	
for multiplicand in xrange(190):
	for multiplier in xrange(multiplicand, 7800):
		product = multiplicand * multiplier
		num_string = ''.join([str(multiplicand), str(multiplier), str(product)])
		if read_string(num_string):
			if (product) not in pan_digits:
				prod_sum += product
				pan_digits.append(product)

			
print prod_sum
print pan_digits

print("--- %s seconds ---" % (time.time() - start_time))