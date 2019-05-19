while True:
    x, y = raw_input().split(' ')
    x = int(x)
    y = int(y)

    if x == 0 and y == 0:
        break

    print y * x
