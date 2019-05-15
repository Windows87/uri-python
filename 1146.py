while True:
    x = input()

    if x == 0:
        break

    t = ""
    for i in range(x - 1):
        i += 1
        t += str(i) + " "

    t += str(x)

    print t
