while True:
    try:
        x, y = raw_input().split(' ')
        print abs(int(x) - int(y))
    except EOFError:
        break