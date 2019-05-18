import math
n = input()
a1 = math.pow((1+math.sqrt(5))/2.0, n)
a2 = math.pow((1-math.sqrt(5))/2.0, n)
print '{:.1f}'.format((a1 - a2) / math.sqrt(5))
