c = 0
r = 0
s = 0

x = input()
for i in range(x):
    y = (raw_input()).split(' ')
    if y[1] == 'C':
        c += int(y[0])
    elif y[1] == 'R':
        r += int(y[0])
    elif y[1] == 'S':
        s += int(y[0])

t = c + r + s
pc = 100.0/t * c
pr = 100.0/t * r
ps = 100.0/t * s

print("Total: " + str(t) + " cobaias")
print("Total de coelhos: " + str(c))
print("Total de ratos: " + str(r))
print("Total de sapos: " + str(s))
print("Percentual de coelhos: {:.2f} %").format(pc)
print("Percentual de ratos: {:.2f} %").format(pr)
print("Percentual de sapos: {:.2f} %").format(ps)
