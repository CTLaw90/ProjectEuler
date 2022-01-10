
def coinify(n, coins, a):
	if coins == []:
		print "empty coins"
		return 0
	elif n == 0:
		print "n == 0"
		return 1
	for x in [coin for coin in coins if coin <= n]:
		if x in coins:
			coins.remove(x)
			for y in [i for i in xrange(1,n) if n%i == 0]:
				print "for coin: ", x
				print "for multi: ", y
				a = coinify(n-(x*y), coins, a)
				print a
			coins.append(x)
	return a
		
			
def main():
	coins = [200,100,50,20,10,5,2,1]
	amount = 5
	
	print coinify(amount, coins, 0)
	
	
main()
