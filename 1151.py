x = input()
a = 1
b = 1
r = 1
t = ""

for i in range(x):
    if i == 0:
        t += "0 "
    elif i == 1:
        t += "1 "
    else:
        t += str(r) + " "
        r = a + b
        a = b
        b = r

t = t[0:len(t) - 1]
print t
       
