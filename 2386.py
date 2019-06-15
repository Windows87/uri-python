x = input()
n = input()
cont = 0

for nIndex in range(n):
    fot = input()
    if fot * x >= 40000000:
        cont += 1

print cont