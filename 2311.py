n = input()
nams = []
valos = []

for nIndex in range(n):
    nams.insert(len(nams), raw_input())
    multi = float(input())
    
    valores = raw_input().split(' ')
    valores = sorted(valores)
    valores = valores[1:len(valores) - 1]
    val = 0.0

    for valor in valores:
        val += float(valor)
    
    valos.insert(len(valos), val * multi)

for i in range(n):
    print nams[i] + ' {:.2f}'.format(valos[i])