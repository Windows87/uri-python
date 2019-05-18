x, y = (raw_input()).split(' ')
x = float(x)
y = float(y)

p = 100/x*y-100
print('{:.2f}%').format(p)
