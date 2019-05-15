x = input()

for i in range(x):
    a, b = (raw_input()).split(' ')
    a = float(a)
    b = float(b)
    if b == 0:
        print "divisao impossivel"
    else:
        print("{:.1f}").format(a/b)
