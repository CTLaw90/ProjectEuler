import time

def main():
	nums = []
	for x in xrange(2, 101):
		for y in xrange(2, 101):
			n = x**y
			if n not in nums:
				nums.append(n)
				
				
	print len(nums)
	
	
start = time.clock()
main()
end = time.clock()
print "Time :" , end - start , "seconds"