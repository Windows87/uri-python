x = input()

for i in range(x):
    a, b, c = raw_input().split(' ')

    if len(a) == 1:
        a = "0" + a

    if len(b) == 1:
        b = "0" + b

    if c == "1":
        print a + ":" + b + " - A porta abriu!"
    else:
        print a + ":" + b + " - A porta fechou!"
