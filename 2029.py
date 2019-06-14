while True:
    try:
        V = float(input())
        D = float(input())
        r = D/2
        h = V/(3.14*r**2)
        a = 3.14 * r**2

        print("ALTURA = {:.2f}").format(h)
        print("AREA = {:.2f}").format(a)
    except EOFError:
        break