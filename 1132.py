x = input()
y = input()
z = 0

if x > y:
    z = x
    x = y
    y = z

s = 0

while y >= x:
    if x % 13 != 0:
        s += x
    x+=1
    
print s
