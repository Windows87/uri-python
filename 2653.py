d = []
v = 0

while True:
    try:
        x = raw_input()
        try:
            d.index(x)
        except ValueError:
            v += 1
            d.insert(len(d), x)
    except EOFError:
        break

print v 