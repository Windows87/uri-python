l = []
for i in range(100):
    l.insert(len(l), input())

for i in range(len(l)):
    if l[i] <= 10:
        print ("A[" + str(i) + "] = {:.1f}").format(l[i])
