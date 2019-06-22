while True:
    n = input()
    if not n:
        break
    s = raw_input().split(' ')
    sc = []

    for e in s:
        sc.insert(len(sc), int(e))

    so = sorted(sc)

    print sc.index(so[len(so) - 2]) + 1