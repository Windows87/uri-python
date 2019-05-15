x = input()
y = input()
z = 0

if x > y:
    z = x
    x = y
    y = z

x += 1

while y > x:
    if x % 5 == 2 or x % 5 == 3:
        print x
    x += 1
