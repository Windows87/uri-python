import math

a, b, c = (raw_input()).split(' ')
a = float(a)
b = float(b)
c = float(c)

if a == 0:
    print("Impossivel calcular")
else:
    d = b**2 - 4*a*c

    if d < 0:
        print("Impossivel calcular")
    else:
        r1 = (-b-math.sqrt(d))/(2*a)
        r2 = (-b+math.sqrt(d))/(2*a)

        print("R1 = {:.5f}").format(r2)
        print("R2 = {:.5f}").format(r1)
