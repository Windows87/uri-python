n = input()
s = raw_input().split(' ')
a = 0.0

for e in s:
    if e == '0':
        a += 1.0

if a/n * 100 > 50.0:
    print 'Y'
else:
    print 'N'