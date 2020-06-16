x, y = raw_input().split(' ')

v = []
d = []

for i in range(int(x)):
    l = raw_input().split(' ')

    for it in l:
        t = it[1]

        if(t == 'V'):
            v.append(int(it[0]))
        else:
            d.append(int(it[0]))

v.sort()
d.sort()

v.reverse()
d.reverse()

for a in v:
    print(str(a) + 'V')

for a in d:
    print(str(a) + 'D')