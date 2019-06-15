n = input()

for nIndex in range(n):
    con, dig = raw_input().split(' ')
    con = int(con)
    dig = int(dig)

    if con and dig:
        print 26**con * 10**dig
    elif con:
        print 26**con
    elif dig:
        print 10**dig
    else:
        print 0