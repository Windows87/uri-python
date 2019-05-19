s = 0
n = 0
while n != 3:
    x = raw_input()
    
    if x == "caw caw":
        print s
        s = 0
        n += 1
    else:
        s += int(x.replace('-', '0').replace('*', '1'), 2)
