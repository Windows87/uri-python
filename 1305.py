while True:
    try:
        x = float(raw_input())
        y = float(raw_input())

        if(x - int(x) >= y):
            print int(x) + 1
        else:
            print int(x)
    except EOFError:
        break