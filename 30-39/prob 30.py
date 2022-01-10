import time

def main():
	tot_sum = 0
	char_str = ""
	
	for x in xrange(2,300000):
		char_str = str(x)
		char_sum = 0
		for char in xrange(len(char_str)):
			char_sum += (int(char_str[char]))**5
		if char_sum == x:
			tot_sum += x
			
	print tot_sum


start = time.clock()
main()
end = time.clock()
print "Time :" , end - start , "seconds"
