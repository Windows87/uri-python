x = int(input())
y = int(input())
s = 0

i = x - 1

while i > y:
    if i % 2 != 0:
        s += i
    i-=1

print(s)
