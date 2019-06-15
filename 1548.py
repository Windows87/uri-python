n = input()

for nIndex in range(n):
    nNotas = input()  

    n2 = 0 
    notas = raw_input().split(' ')

    for notasIndex in range(nNotas):
        notas[notasIndex] = int(notas[notasIndex])

    ordenado = sorted(notas, reverse = True)

    for notasIndex in range(nNotas):
        if notas[notasIndex] == ordenado[notasIndex]:
            n2 += 1

    print n2