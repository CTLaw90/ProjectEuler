def is_div(x,y):
	if x%y == 0:
		return True
	else:
		return False
		
		
loop = True
z= 20
while loop:
	for i in range(1,21):
		if is_div(z,i) == False:
			z = z + 20
			break
		elif is_div(z,i) and i == 20:
			print "sup"
			loop = False
			break
	
print z