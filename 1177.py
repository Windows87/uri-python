x = input()
a = 0

for i in range(1000):
    print "N[" + str(i) + "] = " + str(a)
    a += 1
    if a == x:
        a = 0
