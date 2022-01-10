input_file = open('prob_13_num.txt', 'r')


buffer = ""
sum = 0
for i in range(0,100):
	buffer = input_file.readline()
	sum += int(buffer)
		
print sum