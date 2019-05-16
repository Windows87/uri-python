x = input()
y = raw_input()
m = []
n = 12
s = 0

for i in range(n):
    l = []
    for i2 in range(n):
        l.insert(len(l), input())
    m.insert(len(m), l)

for i in range(n):
    s += m[x][i]

if y == 'S':
    print ('{:.1f}').format(s)
else:
    print ('{:.1f}').format(s/n)
