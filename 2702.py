a, b, c = raw_input().split(' ')
d, e, f = raw_input().split(' ')
r = 0

if int(a) < int(d):
    r += int(d) - int(a)

if int(b) < int(e):
    r += int(e) - int(b)

if int(c) < int(f):
    r += int(f) - int(c)

print r      