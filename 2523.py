while True:
    try:
        x = raw_input()
        y = input()
        z = raw_input().split(' ')
        t = ""

        for e in z:
            t += x[int(e) - 1]

        print t
    except EOFError:
        break
