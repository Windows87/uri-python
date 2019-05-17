n = 12
m = []
st = n - 1
s = 0
v = 0

t = raw_input()

for i in range(n):
    l = []
    for i2 in range(n):
        l.insert(len(l), input())
    m.insert(len(m), l)

for i in range(n):
    for i2 in range(n):
        if i2 > st: 
            s += m[i][i2]
            v += 1
    st -= 1

if t == "S":
    print ('{:.1f}').format(s)
else:
    print ('{:.1f}').format(s/v)
