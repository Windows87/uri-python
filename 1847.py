x, y, z = raw_input().split(' ')
x = int(x)
y = int(y)
z = int(z)

if x > y and z >= y:
    print ':)'
elif y > x and y >= z:
    print ':('
elif y > x and z > y and (z - y) < (y - x):
    print ':('
elif y > x and z > y and (z - y) >= (y - x):
    print ':)'
elif x > y and y > z and (y - z) < (x - y):
    print ':)'
elif y > x and y > z and (y - z) >= (y - z):
    print ':('
elif x == y and z > y:
    print ':)'
else:
    print ':('
