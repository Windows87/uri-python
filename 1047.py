a, b, c, d = (raw_input()).split(' ')

a = int(a)
b = int(b)
c = int(c)
d = int(d)
mi = a*60+b
mf = c*60+d
m = 0

if mi >= mf:
    m = mf + 24*60 - mi
else:
    m = mf - mi

print("O JOGO DUROU " + str(m/60) + " HORA(S) E " + str(m - m/60 * 60) + " MINUTO(S)")
