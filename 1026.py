def binary(n, mlen):
    bina = bin(n)
    bina = bina[2:len(bina)]

    mbina = bin(mlen)
    mbina = mbina[2:len(mbina)]
    ret = ""

    for nIndex in range(len(mbina) - len(bina)):
        ret += "0"

    return ret + bina

while True:
    try:
        x, y = raw_input().split(' ')
        mlen = 0

        if int(x) > int(y):
            mlen = int(x)
        else:
            mlen = int(y)

        x = binary(int(x), mlen)
        y = binary(int(y), mlen)
        r = ""

        for nIndex in range(len(x)):
            if x[nIndex] == y[nIndex]:
                if x[nIndex] == '1':
                    r += '0'
                else:
                    r += x[nIndex]
            else:
                r += '1'
        
        print int(r, 2)
    except EOFError:
        break