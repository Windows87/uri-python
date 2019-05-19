x = input()
y = raw_input().split(' ')
l = int(y[0])
q = 0

for i in range(x - 1):
    i += 1
    if l > int(y[i]):
        q = i + 1
        break
        
    l = int(y[i])

print q
