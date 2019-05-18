x = input()
x = (raw_input()).split()

m2 = 0
m3 = 0
m4 = 0
m5 = 0

for y in x:
    y = int(y)
    if y % 2 == 0:
        m2 += 1
    if y % 3 == 0:
        m3 += 1
    if y % 4 == 0:
        m4 += 1
    if y % 5 == 0:
        m5 += 1

print str(m2) + " Multiplo(s) de 2"
print str(m3) + " Multiplo(s) de 3"
print str(m4) + " Multiplo(s) de 4"
print str(m5) + " Multiplo(s) de 5"
