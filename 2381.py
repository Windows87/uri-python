n, x = raw_input().split(' ')
l = []

for nIndex in range(int(n)):
    l.insert(len(l), raw_input())

l = sorted(l)

print l[int(x) - 1]