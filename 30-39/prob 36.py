#prob 36
#double-base palindromes


#one liner to convert base 10 to base x
def Base10toBaseN(num,n):
   return ((num == 0) and  "0" ) or ( Base10toBaseN(num // n, n).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[:n][num % n])

def is_pal(num):
		n = str(num)
		rev_n = ''
		
		for char in xrange(len(n) - 1, -1, -1):
			rev_n = rev_n + n[char]
			
		if rev_n == n:
			return True
		else:
			return False

sum_of_pal = 0
			
for i in xrange(1000000):
	j = Base10toBaseN(i, 2)
	if is_pal(i) and is_pal(j):
		print i, " and ", j, " are palindromes!"
		sum_of_pal += i
		
print sum_of_pal

