while True:
    try:
        x, y = raw_input().split(' ')
        x = int(x)
        g = 0

        for i in range(x):
            z = raw_input().split(' ')
            if z[0] == y and z[1] == "0":
                g += 1

        print g
    except EOFError:
        break
