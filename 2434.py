n, inicio = raw_input().split(' ')
inicio = int(inicio)
m = inicio

for nIndex in range(int(n)):
    inicio += input()
    if inicio < m:
        m = inicio

print m