def binary(n):
    b = bin(n)
    b = b[2:len(b)]
    return b

def invert(b):
    return b[::-1]

def best(bestn, bestt, y, t):
    for i in range(bestn):
        i+=1
        
        if t == '+ ':
            nb = binary(y + i)

        if t == '- ':
            nb = binary(y - i)

        if t == 'x ':
            nb = binary(y * i)

        if t == '/ ':
            nb = binary(y / i)
        
        ninv = invert(nb)

        if nb == ninv:
            if(bestn > i):
                bestn = i
                bestt = t            
            break
    return [bestn, bestt]

x = input()

for i in range(x):
    y = input()
    b = binary(y)
    inv = invert(b)
    bestt = ""
    bestn = 100

    if inv == b:
        print('*')
        continue

    for i in range(50):
        i+=1
        nb = binary(y + i)
        ninv = invert(nb)
        
        if nb == ninv:
            if(bestn > i):
                bestn = i
                bestt = '+ '
            break

    bestn, bestt = best(bestn, bestt, y, '+ ')
    bestn, bestt = best(bestn, bestt, y, '- ')
    bestn, bestt = best(bestn, bestt, y, 'x ')
    bestn, bestt = best(bestn, bestt, y, '/ ')

    print(bestt + str(bestn))
