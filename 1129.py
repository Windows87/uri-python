while True:
    n = input()
    if not n:
        break

    for nIndex in range(n):
        A, B, C, D, E = raw_input().split(' ')
        m = []

        if int(A) <= 127:
            m.insert(len(m), 'A')

        if int(B) <= 127:
            m.insert(len(m), 'B')

        if int(C) <= 127:
            m.insert(len(m), 'C')

        if int(D) <= 127:
            m.insert(len(m), 'D')

        if int(E) <= 127:
            m.insert(len(m), 'E')

        if len(m) == 0 or len(m) > 1:
            print '*'
        else:
            print m[0]     