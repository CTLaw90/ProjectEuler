#was in the middle of changing some things and decided i needed to rewrite
#the entire program. wanted to use generator function instead of recaluclating
#the triangle number each time. ended up WAY faster

import math

def get_tri(num):
	tri = 0
	while tri < num:
		yield tri
		tri += i
	
def get_div(num):
	numdiv = 2
	for i in range(2, num):
		if num % i == 0:
			numdiv += 1
	return numdiv

x = 10000	
y = 0
while y <= 500:
	y = get_div(get_tri(x))
	print x, y
	x += 1

print y