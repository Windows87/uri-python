for i in range(11):
    for i2 in range(3):
        i2+=1
        r = i*0.2
        r2 = i2+i*0.2
        if r == int(r):
            r = int(r)
        if r2 == int(r2):
            r2 = int(r2)
        print("I="+str(r)+" J="+str(r2))
