while True:
    try:
        x = input()
        a = 0
        f = 0
        tf = 0
        i = False

        for c in x:
            if c == '(':
                a += 1
                tf += 1

            if c == ')':
                if tf == 0:
                    i = True
                tf -= 1
                f += 1

        if a == f and i == False:
            print('correct')
        else:
            print('incorrect')
    except EOFError:
        break
