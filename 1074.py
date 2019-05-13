x = input()

for i in range(x):
    y = input()
    t = ""

    if y == 0:
        print("NULL")
    else:
        if y % 2 == 0:
            t += "EVEN "
        else:
            t += "ODD "

        if y > 0:
            t += "POSITIVE"
        else:
            t += "NEGATIVE"
        print(t)
        

        
