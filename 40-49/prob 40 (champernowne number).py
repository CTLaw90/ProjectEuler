#project euler 40

numString = ""
i = 1

while len(numString) < 1000000:
	numString += str(i)
	i += 1
	
numSum = int(numString[1 - 1]) * int(numString[10 - 1]) * int(numString[100 - 1]) * int(numString[1000 - 1]) * int(numString[10000 - 1]) * int(numString[100000 - 1]) * int(numString[1000000 - 1])
print numSum