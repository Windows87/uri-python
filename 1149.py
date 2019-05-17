t = (raw_input()).split(' ')
x = int(t[0])
y = -1
i = 1
s = 0

while y == -1:
    v = int(t[i])
    
    if v > 0:
        y = v
    
    i += 1

for i in range(y):
    s += x + i

print s
