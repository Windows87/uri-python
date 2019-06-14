n = input()

for nIndex in range(n):
    x, y = raw_input().split(' ')
    x = int(x)
    y = int(y)

    b = 2*(x**2) + (5*y)**2
    c = -100*x + y**3
    r = (3*x)**2 + y**2

    if b > c and b > r:
        print "Beto ganhou"
    elif c > b and c > r:
        print "Carlos ganhou"
    else:
        print "Rafael ganhou"