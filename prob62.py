#projeuler problem 62
#cubic permutations

perms = {}

x = 10
while x < 10000:
    tmp = x*x*x
    tmpStr = list(str(tmp))
    tmpStr.sort()
    tmpStr = ''.join(tmpStr)
    if tmpStr in perms:
        perms[tmpStr].append([tmp, x])
        if len(perms[tmpStr]) == 5:
            print("Found!")
            print(perms[tmpStr])
            quit()
    else:
        perms[tmpStr] = ([[tmp, x]])
    x+=1

print("Not Found")   
