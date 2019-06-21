n = input()

for nIndex in range(n):
    nams = []
    vals = []
    total = 0.0

    n2 = input()
    for n2Index in range(n2):
        nam, val = raw_input().split(' ')
        nams.insert(len(nams), nam)
        vals.insert(len(vals), float(val))
    
    n2 = input()
    for n2Index in range(n2):
        nam, quant = raw_input().split(' ')
        total += vals[nams.index(nam)] * int(quant)
    
    print 'R$ {:.2f}'.format(total)