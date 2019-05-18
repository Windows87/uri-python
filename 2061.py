x, y = (raw_input()).split(' ')
x = int(x)
y = int(y)

for i in range(y):
    z = raw_input()
    if z == 'fechou':
        x += 1
    else:
        x -= 1

print x
