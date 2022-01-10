
def coinify(n, coins, known_values):
	breaker = 0
	for x in [coin for coin in coins if (coin <= n)]: #for loop which iterates through all coins >= incoming amount
		print "Entering for loop with n =", n, ", with coin =", x, ", and known values:\n", known_values
		if n - x == 0:
			known_values[n] += 1
		elif known_values[n-x] > 0:
			known_values[n] += known_values[n-x]
		else:
			known_values = coinify(n-x, coins, known_values)
			known_values[n] += 1						#looks good
	return known_values
	
	
	
def main():
	coins = [1,2,5,10,20,50,100,200]
	amount = 7
	known_values = [0] * (amount+1)
	known_values[1] = 1
	known_values = coinify(amount, coins, known_values)
	print "For the amount", amount, "there are",known_values[amount], "possible means of constructing with the coin values of:", coins
	
main()
