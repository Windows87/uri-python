m = 0
p = 0

for i in range(100):
    y = int(input())
    if y > m:
        m = y
        p = i + 1

print(m)
print(p)
