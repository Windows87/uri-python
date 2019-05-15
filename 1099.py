x = input()

for i in range(x):
    a, b = (raw_input()).split(' ')
    o = sorted([int(a), int(b)])
    a = o[1]
    b = o[0] + 1
    s = 0

    while a > b:
        if b % 2 != 0:
            s += b
        b+=1

    print s
