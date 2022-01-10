ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
tens = ["","","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["", "onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred", "sevenhundred", "eighthundred", "ninehundred"]
thousand = ["" , "onethousand"]
ands = "and"

def assign_name(num):
	#method to change numeric characters into words
	bufferstring = ""
	
	i1 = int(num[3])
	i2 = int(num[2])
	i3 = int(num[1])
	i4 = int(num[0])
	
	i12 = int(num[2]) * 10 + int(num[3])
	
	if int(i2) < 2:
		bufferstring = thousand[i4] + hundreds[i3] + ones[i12]
	else:
		bufferstring = thousand[i4] + hundreds[i3] + tens[i2] + ones[i1]
	if (i2 > 0 or i1 > 0) and (i3 > 0 or i4 > 0):
		bufferstring = bufferstring + ands
	
	return bufferstring

sum = 0
word = ""

for i in range(1, 1001):

	stringnum = str(i)

	#get the string in a readable form, i.e. "0116"
	while len(stringnum) < 4:
		stringnum = "0" + stringnum
	
	word = assign_name(stringnum)
	#print i, word
	sum += len(word)
	
print sum
	
