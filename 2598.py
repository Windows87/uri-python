import math
n = input()

for nIndex in range(n):
    n, m = raw_input().split(' ')

    if int(n) % int(m) == 0:
        print int(n) / int(m)
    else:
        print int(n) / int(m) + 1