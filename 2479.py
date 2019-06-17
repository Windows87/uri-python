n = input()
c = 0
nc = 0
nams = []

for nIndex in range(n):
    t, nam = raw_input().split(' ')
    
    nams.insert(len(nams), nam)

    if t == '+':
        c += 1
    else:
        nc += 1

nams = sorted(nams)

for nam in nams:
    print nam

print 'Se comportaram: ' + str(c) + ' | Nao se comportaram: ' + str(nc)
