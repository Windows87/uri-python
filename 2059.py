a, b, c, d, e = (raw_input()).split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

if e == 1 and d == 1:
      print "Jogador 2 ganha!"
elif d == 1:
    print "Jogador 1 ganha!"
else:
    if (b + c) % 2 == 0:
        if a == 1:
            print "Jogador 1 ganha!"
        else:
            print "Jogador 2 ganha!"
    else:
        if a == 0:
            print "Jogador 1 ganha!"
        else:
            print "Jogador 2 ganha!"        
