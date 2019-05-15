x, y = (raw_input()).split(' ')
x = int(x)
y = int(y)
i3 = 1

for i in range(y):
    t = ""

    for i2 in range(x - 1):
        t += str(i3) + " "
        i3+=1

    t += str(i3)

    print t

    if i3 == y:
        break
    else:
        i3+=1
