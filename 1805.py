x, y = raw_input().split(' ')
x = int(x)
y = int(y)
t = 0

while y >= x:
    t += x
    x += 1

print t