c = 1

while True:
    try:
        x = input()
        t = ""

        for i in range(x + 1):
            if  i == 0:
                t += "0 "
            else:
                for i2 in range(i):
                    t += str(i) + " "

        t = t[0: len(t) - 1]
        n = len(t.split(' '))
        if len(t.split(' ')) == 1:
            print "Caso " + str(c) + ": " + str(n) + " numero"
        else:
            print "Caso " + str(c) + ": " + str(n) + " numeros"
        print t
        print ""

        c += 1
    except EOFError:
        break
