def get_diags(n):
	if n == 1:
		return 1
	else:
		return (2*((2*((2*n - 1)**2)) - (6*(n-1))))
		
def main():
	sum = 0
	n = 1
	while ((2*n - 1)**2) <= (1001*1001):
		sum += get_diags(n)
		# print n, sum
		n += 1
	print sum
		
main()