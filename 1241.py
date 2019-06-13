n = input()

for nIndex in range(n):
    n1, n2 = raw_input().split(' ')

    if n1[len(n1) - len(n2) : len(n1)]  == n2:
        print "encaixa"
    else:
        print "nao encaixa"