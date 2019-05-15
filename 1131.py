g = 0
v1 = 0
v2 = 0
e = 0

while True:
    a, b = (raw_input()).split(' ')
    a = int(a)
    b = int(b)
    g+=1

    if(a > b):
        v1 += 1
    elif a == b:
        e += 1
    else:
        v2 += 1

    print "Novo grenal (1-sim 2-nao)"
    y = input()

    if y == 2:
        break

print(str(g) + " grenais")
print("Inter:" + str(v1))
print("Gremio:" + str(v2))
print("Empates:" + str(e))

if v1 > v2:
    print("Inter venceu mais")
elif v1 == v2:
    print("Nao houve vencedor")
else:
    print("Gremio venceu mais")
