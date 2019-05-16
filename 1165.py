x = input()

for i in range(x):
    y = input()
    p = True

    for i in range(y):
        i+=1
        if y % i == 0 and i != 1 and i != y:
            p = False

    if p == True:
        print str(y) + " eh primo"
    else:
        print str(y) + " nao eh primo"
