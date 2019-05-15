while True:
    a, b = (raw_input()).split(' ')
    o = sorted([int(a), int(b)])
    a = o[1]
    b = o[0]

    if a <= 0 or b <= 0:
        break

    s = 0
    t = ""

    while a >= b:
        t += str(b) + " "
        s += b
        b += 1

    print(t + "Sum=" + str(s))
