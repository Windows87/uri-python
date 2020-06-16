n = int(input())

for i in range(n):
    x = int(input())
    t = 0

    for j in range(x):
        t += 2**j
    
    print(t)