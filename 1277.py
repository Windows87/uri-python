n = input()

for nIndex in range(n):
    n2 = input()
    names = raw_input().split(' ')
    ps = raw_input().split(' ')
    i = 0
    txt = ""

    for name in names:
        p2 = ps[i] 

        pre = 0
        t = 0.0

        for p in p2:
            if p != 'M':
                t += 1
                if p == 'P':
                    pre += 1
        
        if pre / t * 100 < 75:
            txt += name + " "
        
        i += 1

    print txt[0:len(txt) - 1]