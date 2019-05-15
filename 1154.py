s = 0
p = 0.0

while True:
    x = input()
    if x < 0:
        break
    s += x
    p += 1

print('{:.2f}').format(s/p)
