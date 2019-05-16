x = input()
x2 = x
y = 0
n = 1

while True:
    y = input()
    if y > x:
        break

while y > x:
    x += x2 + n
    n += 1

print n
