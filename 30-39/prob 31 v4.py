import time
start_time = time.time()

coins = [1, 2, 5, 10, 20, 50, 100, 200]
solutions = 0

def coinify(amount, last_coin):
	global solutions
	new_coins = [x for x in coins if x <= (target - amount) and x >= last_coin]
	
	for coin in new_coins:
		# print 'target', target, 'amount', amount, 'coin', coin, 'coins', new_coins
		amount += coin
		if (target - amount) == 0:
			solutions += 1
		elif (target - amount) > 0:
			last_coin = coin
			coinify(amount, last_coin)
		amount -= coin


target = int(raw_input('enter an amount> '))

coinify(0, 0)		
			
print "number of solutions: ", solutions
print("--- %s seconds ---" % (time.time() - start_time))