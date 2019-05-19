m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31,30, 31]

while True:
    try:
        x, y = raw_input().split(' ')
        x = int(x)
        y = int(y)
        s = 0

        for i in range(x - 1):
            s += m[i]

        s += y

        if s == 359:
            print "E vespera de natal!"
        elif s == 360:
            print "E natal!"
        elif s < 360:
            print "Faltam " + str(360 - s) + " dias para o natal!"
        elif s > 360:
            print "Ja passou!"
    except EOFError:
        break
