while True:
    try:
        x = input()
        print x - 1
    except EOFError:
        break
