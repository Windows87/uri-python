n = input()

s = 0
b = 0
a = 0

st = 0
bt = 0
at = 0

for nIndex in range(n):
    name = raw_input()
    sg, bg, ag = raw_input().split(' ')

    s += float(sg) 
    b += float(bg) 
    a += float(ag)

    sg, bg, ag = raw_input().split(' ')

    st += float(sg) 
    bt += float(bg) 
    at += float(ag)

sr = 100/s*st
br = 100/b*bt
ar = 100/a*at

print 'Pontos de Saque: {:.2f} %.'.format(sr)
print 'Pontos de Bloqueio: {:.2f} %.'.format(br)
print 'Pontos de Ataque: {:.2f} %.'.format(ar)