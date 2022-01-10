#modified version of the incorrect algorithm. this works in reverse, bottom-up, and summates the lower rows into the higher by selecting the highest possible combination. if that makes sense.
#i.e.        3         ->             3
#          5   2       ->           7   11
#        1    2   9    ->        x     x     x

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
	
def find_greatest_child(Ctri, indx, indy):
	# given the current position in the triangle, find the greatest of the children
	# returns 0 for left leg, 1 for right leg
	# renamed for clarity
	if int(Ctri[indy+1][indx]) > int(Ctri[indy+1][indx+1]):
		return 0
	else:
		return 1

#inital variable dec			
cur_num = 0
sum = 0
child = 0
	
#open file to count lines	
current_file = open_file(input_file)
lines_in_file = lines(current_file)
print lines_in_file

#reopen file to build the triange because i have to :[
current_file = open_file(input_file)
tri = build_tri(lines_in_file, current_file)
print tri

#main loop
for y in xrange(lines_in_file - 2, - 1, -1):
	for x in xrange(len(tri[y])):
		cur_num = int(tri[y][x])
		child = find_greatest_child(tri, x, y)
		tri[y][x] = str(int(tri[y][x]) + int(tri[y+1][x+child]))
	tri[y+1] = ["x"] * len(tri[y+1])
	for lines in xrange(lines_in_file):
		print tri[lines]
	
print tri[0][0]