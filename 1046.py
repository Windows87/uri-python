a, b = (raw_input()).split(' ')

a = int(a)
b = int(b)
h = 0

if a >= b:
    h = b + 24 - a
else:
    h = b - a

print("O JOGO DUROU " + str(h) + " HORA(S)")
