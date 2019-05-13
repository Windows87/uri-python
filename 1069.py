x = int(input())

for i in range(x):
    y = input()
    y = y.replace('.', '')
    d = 0
    for i2 in range(50):
        o = len(y)
        y = y.replace('<>', '')
        n = len(y)
        d += (o - n) / 2
    print(int(d))
    
