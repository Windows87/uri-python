m = input()
n = input()

a = []

for nIndex in range(n):
    x = input()

    try:
        a.index(x)
    except ValueError:
        a.insert(len(a), x)
        m -= 1

print m