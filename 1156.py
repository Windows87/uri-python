s = 0

for i in range(20):
    if i == 0:
        s += 1
    else:
        s += (1.0 + i * 2)/2 ** i

print ('{:.2f}').format(s)
