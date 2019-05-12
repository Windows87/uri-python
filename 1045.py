a, b, c = (raw_input()).split(' ')

a = float(a)
b = float(b)
c = float(c)

s = sorted([a, b, c])
a = s[2]
b = s[1]
c = s[0]

if a >= b+c:
    print("NAO FORMA TRIANGULO")
elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")
elif a**2 > b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")
elif a**2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")

if a == b and b == c:
    print("TRIANGULO EQUILATERO")
else:
    if a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")
