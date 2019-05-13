pa = 0
im = 0
po = 0
ne = 0

for i in range(5):
    x = int(input())
    if x % 2 == 0:
        pa += 1
    else:
        im += 1

    if x > 0:
        po += 1
    else:
        if x != 0:
            ne += 1

print(str(pa) + " valor(es) par(es)")
print(str(im) + " valor(es) impar(es)")
print(str(po) + " valor(es) positivo(s)")
print(str(ne) + " valor(es) negativo(s)")
