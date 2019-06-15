n = input()

for nIndex in range(n):
    texto = raw_input()

    if texto[0] == texto[2]:
        print int(texto[0]) * int(texto[2])
    elif texto[1].islower():
        print int(texto[0]) + int(texto[2])
    else:
        print int(texto[2]) - int(texto[0])