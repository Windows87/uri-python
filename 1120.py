while True:
    x, y = (raw_input()).split(' ')
    x = int(x)
    y = int(y)

    if x == 0 and y == 0:
        break

    y = str(y).replace(str(x), '')
    if y == '':
        y = 0
    else:
        y = int(y)
        
    print y
