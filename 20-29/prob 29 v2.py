#was playing around with list comprehension, incomplete solution

import time

def main():
	nums = [x for x in xrange(2, 101)]
	print len(nums)
	print nums
	
	
start = time.clock()
main()
end = time.clock()
print "Time :" , end - start , "seconds"