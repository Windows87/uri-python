p = 0
m = 0

for i in range(6):
    x = input()
    if x > 0:
        p += 1
        m += x

m = m/p
print(str(p) + " valores positivos")
print('{:.1f}').format(m)
