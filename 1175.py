l = []
l2 = []

for i in range(20):
    l.insert(len(l), input())

c = len(l) - 1
while c >= 0:
    l2.insert(len(l2), l[c])
    c -= 1

for i in range(len(l2)):
    print ("N[" + str(i) + "] = " + str(l2[i]))
