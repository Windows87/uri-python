N, D = raw_input().split(' ')

N = int(N)
D = int(D)

l = {}

for i in range(N):
    x = raw_input().lower().replace(' ', '')
    firstCarac = x[0]
    if firstCarac in l:
        if(len(l[firstCarac]) < len(x)):
            l[firstCarac] = x
    else:
        l[firstCarac] = x

l2 = []
t = 0

for c in l:
    l2.append(len(l[c]))

l2.sort()
l2.reverse()

if len(l2) < D:
    D = len(l2)

for i in range(D):
    t += l2[i]

print(t)