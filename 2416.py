x, y = raw_input().split(' ')
x = int(x)
y = int(y)

if x > y:
    print x % y
else:
    print y % x