n = 0.0
t = 0

while True:
    try:
        na = raw_input()
        n += 1
        t += input()
    except EOFError:
        break

print('{:.1f}').format(t/n) 