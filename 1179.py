def printArray(n, a):
    for i in range(len(a)):
        print n + "[" + str(i) + "] = " + str(a[i])
 
p = []
im = []
for i in range(15):
    x = input()
    if x % 2 == 0:
        p.insert(len(p), x)
    else:
        im.insert(len(im), x)
        
    if len(p) == 5:
        printArray('par', p)
        p = []
    
    if len(im) == 5:
        printArray('impar', im)
        im = []

printArray('impar', im)
printArray('par', p)
