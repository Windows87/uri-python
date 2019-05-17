x = input()

for i in range(x):
    y = (raw_input()).split(' ')
    n1 = y[0]
    t1 = y[1]
    n2 = y[2]
    t2 = y[3]

    y, z = (raw_input()).split(' ')
    s = int(y) + int(z)

    if s % 2 == 0:
        if t1 == "PAR":
            print n1
        else:
            print n2
    else:
        if t1 == "IMPAR":
            print n1
        else:
            print n2
