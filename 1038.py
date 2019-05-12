x, y = (raw_input()).split(' ')
x = int(x)
y = int(y)
t = 0

if x == 1:
    t = y * 4
elif x == 2:
    t = y * 4.5
elif x == 3:
    t = y * 5
elif x == 4:
    t = y * 2
else:
    t = y * 1.5

print("Total: R$ {:.2f}").format(t)
