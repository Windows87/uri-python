i = 1
while True:
    x = input()

    if x == -1:
        break

    print "Experiment " + str(i) + ": " + str(x/2) + " full cycle(s)"
    i += 1