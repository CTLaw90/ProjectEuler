import time

start = time.clock()


fibs =[1, 1]
x = 1
while len(str(fibs[x])) < 1000:
    fibs.append(fibs[x] + fibs[x-1])
    x += 1
	
print x+1


end = time.clock()

print "Time : ", end - start, " seconds"
