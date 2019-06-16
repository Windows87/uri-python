import math

while True:
    try:
        x, y = raw_input().split(' ')
        print math.factorial(int(x)) + math.factorial(int(y))
    except EOFError:
        break