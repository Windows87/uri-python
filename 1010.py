a, b, c = (raw_input()).split(' ')
a = int(a)
b = int(b)
c = float(c)

d, e, f = (raw_input()).split(' ')
d = int(d)
e = int(e)
f = float(f)

print("VALOR A PAGAR: R$ {:.2f}").format(b*c + e*f)
