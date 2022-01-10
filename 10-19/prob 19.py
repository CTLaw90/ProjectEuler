days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
day_of_week = [0, 1, 2, 3, 4, 5, 6] #0 is sunday

day = 2 #jan 1, 1901 was a tuesday

tot = 0 #number of 1sts of the month that are sundays

for year in xrange(1901, 2001):
	if year % 4 == 0:
		days_in_month[1] = 29
	else:
		days_in_month[1] = 28
	for month in days_in_month:
		if day % 7 == 0:
			tot += 1
		day += month
		
print tot
