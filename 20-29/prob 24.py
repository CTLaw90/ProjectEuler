import time

max = 10

i = range(max)
perms = []
obuff = []
go = True

def rec(buff):
	global perms
	global go
	if go:
		for x in i:
			if x not in buff:
				buff.append(x)
				if len(buff) < max+1:
					rec(buff)
					if len(buff) == max:
						perms.append(str(buff))
						if len(perms) == 1000000:
							go = False
				buff.pop()


			
def main():
	rec(obuff)
	print perms.pop()
        
start = time.clock()
main()
end = time.clock()
print "Time :" , end - start , "seconds"
