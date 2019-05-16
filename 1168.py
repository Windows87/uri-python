n = input()
for i in range(n):
    x = raw_input()
    s = 0
    
    for y in x:
        if y == '1':
            s += 2
        elif y == '2':
            s += 5
        elif y == '3':
            s += 5
        elif y == '4':
            s += 4
        elif y == '5':
            s += 5
        elif y == '6':
            s += 6
        elif y == '7':
            s += 3
        elif y == '8':
            s += 7
        elif y == '9':
            s += 6
        else:
            s += 6

    print str(s) + " leds"
