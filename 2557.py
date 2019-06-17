while True:
    try:
        x, t = raw_input().split('+')
        y = t.split('=')[0]
        z = t.split('=')[1]

        if not x.isdigit():
            print int(z) - int(y)
        elif not y.isdigit():
            print int(z) - int(x)
        else:
            print int(x) + int(y)
    except EOFError:
        break