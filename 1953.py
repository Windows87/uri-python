while True:
    try:
        n = input()
        EPR = 0
        EHD = 0
        INTRUSOS = 0

        for nIndex in range(n):
            m, curso = raw_input().split(' ')

            if curso == 'EPR':
                EPR += 1
            elif curso == 'EHD':
                EHD += 1
            else:
                INTRUSOS += 1

        print "EPR: " + str(EPR)
        print "EHD: " + str(EHD)
        print "INTRUSOS: " + str(INTRUSOS) 
    except EOFError:
        break