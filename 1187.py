n = 12
m = []
st1 = 1
st2 = n - 2
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
        if i2 >= st1 and i2 <= st2: 
            s += m[i][i2]
            v += 1
    st1 += 1
    st2 -= 1

if t == "S":
    print ('{:.1f}').format(s)
else:
    print ('{:.1f}').format(s/v)
