ok = True
while True:
    if ok == True:
        x = 0
        s = 0.0

        while x != 2:
            y = float(input())
            if y > 10 or y < 0:
                print("nota invalida")
            else:
                x+=1
                s+=y
        print("media = {:.2f}").format(s/2)

    ok = False
    print ("novo calculo (1-sim 2-nao)")
    y = input()

    if y == 1:
        ok = True
    elif y == 2:
        break
