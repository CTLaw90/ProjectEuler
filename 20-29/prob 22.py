input_file = open('names.txt')
name_list =  input_file.read()
name_list = name_list.replace('"', '')
name_list = name_list.split(",")
name_list.sort()

def char_val(name):
	vals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	sum = 0
	char = ""
	for i in range(len(name)):
		char = name[i]
		sum += (vals.find(char) + 1)
		
	return sum
	
total = 0

for i in range(len(name_list)):
	total += (i+1) * char_val(name_list[i])
	
print total