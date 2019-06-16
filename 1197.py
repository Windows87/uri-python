while True:
    try:
        x, y = raw_input().split(' ')
        print int(x)*2 * int(y)
    except EOFError:
        break