a = 1
b = 1
r = 1
f = []

for i in range(61):
    if i == 0:
        f.insert(len(f), 0)
    elif i == 1:
        f.insert(len(f), 1)
    else:
        f.insert(len(f), r)
        r = a + b
        a = b
        b = r

x = input()

for i in range(x):
    y = input()
    print "Fib(" + str(y) + ") = " + str(f[y])
