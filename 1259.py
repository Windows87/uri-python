n = input()
p = []
im = []

for nIndex in range(n):
    x = input()
    if x % 2 == 0:
        p.insert(len(p), x)
    else:
        im.insert(len(im), x)

p = sorted(p)
im = sorted(im, reverse=True)

for ps in p:
    print ps

for imps in im:
    print imps