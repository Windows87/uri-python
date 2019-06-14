n = input()

for nIndex in range(n):
    cod = raw_input()
    if cod[0] != 'R' or cod[1] != 'A':
        print "INVALID DATA"
    elif len(cod) != 20:
        print "INVALID DATA"
    else:
        print int(cod[2:len(cod)])