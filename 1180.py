x = input()
y = (raw_input()).split(' ')
m = 0
p = 0

for i in range(x):
    y[i] = int(y[i])
    if y[i] < m:
        m = y[i]
        p = i

print "Menor valor: " + str(m)
print "Posicao: " + str(p)
