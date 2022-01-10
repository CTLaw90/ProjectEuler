def rev_num(x):
	rev = ""
	for i in range(len(str(x)), 0, -1):
		rev = rev + str(x)[i-1]
	return int(rev)
	
hold = 1
current = 1	
	
for x in range(999,900,-1):
	for y in range(999,900,-1):
		hold = x * y
		if hold == rev_num(hold):
			if hold > current:
				current = hold
				
print current