a, b, c= (raw_input()).split(' ')
a = int(a)
b = int(b)
c = int(c)

s = sorted([a, b, c])

for i in range(3):
    print(s[i])

print("")

print(a)
print(b)
print(c)
