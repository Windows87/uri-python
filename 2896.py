n = int(input())

for i in range(n):
    x, y = raw_input().split(' ')
    
    x = int(x)
    y = int(y)

    g = int(x/y) 

    t = x%y + g

    print(t)