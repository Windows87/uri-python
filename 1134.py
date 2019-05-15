a = 0
g = 0
d = 0

while True:
    x = input()

    if x == 4:
        break

    if x == 1:
        a += 1
    elif x == 2:
        g += 1
    elif x == 3:
        d += 1

print "MUITO OBRIGADO"
print "Alcool: " + str(a)
print "Gasolina: " + str(g)
print "Diesel: " + str(d)
