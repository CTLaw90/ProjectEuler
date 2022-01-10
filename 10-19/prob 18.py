#unfortunatley missunderstood the problem. this algoritm moves top-down and chooses the highest child element

input_file = 'prob_18_num.txt'

def open_file(file):
	return open(file, 'r')

def lines(file):
	#counts lines in the file
	with file as f:
		for i, l in enumerate(f):
			pass
	return i + 1
	
def build_tri(lines, file):
	#builds and populates the triangle
	Btri = []
	str_buff = ""
	for i in range(lines):
		Btri.append(["00"])
	
	for j in range(lines):
		str_buff = file.readline()
		Btri[j] = str_buff.split()
		
	return Btri
	
def find_next_num(Ctri, indx, indy):
	#given the current position in the triangle, find the greatest of the children
	#returns 0 for left leg, 1 for right leg
	if int(Ctri[indy+1][indx]) > int(Ctri[indy+1][indx+1]):
		return 0
	else:
		return 1

#inital variable dec		
x = 0	
cur_num = 0
sum = 0
	
#open file to count lines	
current_file = open_file(input_file)
lines_in_file = lines(current_file)
print lines_in_file

#reopen file to build the triange because i have to :[
current_file = open_file(input_file)
tri = build_tri(lines_in_file, current_file)
print tri

#main loop
for y in xrange(lines_in_file):
	cur_num = int(tri[y][x])
	sum += cur_num
	print y, tri[y], cur_num
	if y < lines_in_file-1:
		x += find_next_num(tri, x, y)
	
	
print sum