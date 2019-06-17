a, b = raw_input().split(' ')
c = raw_input().split(' ')
t = int(a)

for i in c:
    t += int(i)

    if t < 0:
        t = 0

    if t > 100:
        t = 100

print t