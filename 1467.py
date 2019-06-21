while True:
    try:
        a, b, c = raw_input().split(' ')
        if a == b and a == c and b == c:
            print '*'
        elif a != b and a != c:
            print 'A'
        elif b != a and b != c:
            print 'B'
        else:
            print 'C'
    except EOFError:
        break