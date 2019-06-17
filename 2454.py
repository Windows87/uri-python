x, y = raw_input().split(' ')
x = int(x)
y = int(y)

if x and not y:
    print "B"
elif x and y:
    print "A"
else:
    print "C"