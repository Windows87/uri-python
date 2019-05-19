c = 1

while True:
    try:
        x = raw_input()
        y = raw_input()
        n = len(y.split(x)) - 1

        print "Caso #" + str(c) + ":"

        if n != 0:
            print "Qtd.Subsequencias: " + str(n)
            print "Pos: " + str(y.rindex(x) + 1)
        else:
            print "Nao existe subsequencia"
        print ""
        c += 1
    except EOFError:
        break
