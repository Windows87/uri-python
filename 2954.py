n = input()

for i in range(n):
    r = raw_input().lower()
    f = ''

    for c in r:
        if not c in ['.', ',']:
            f += c

    t = [0]

    f = f.split(' ')

    for p in f:
        if p == 'jogo':
            t[len(t) - 1] += 4
            t.append(0)
        elif p == 'perdi':
            t[len(t) - 1] += 5
            t.append(0)
        else:
            t[len(t) - 1] += len(p)
    
    t.sort()
    t.reverse()

    print(t[0])
