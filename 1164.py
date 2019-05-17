t = input()
for i2 in range(t):
    x = input()
    s = 0
    for i in range(x - 1):
        i += 1
        if x % i == 0:
            s += i
        
    if s == x:
        print str(x) + " eh perfeito"
    else:
        print str(x) + " nao eh perfeito"