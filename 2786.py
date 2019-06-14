x = input()
y = input()

print x*y + (x - 1)*(y - 1)
if x % 2 != 0:
    print (x - 1)*(y - 1) + (x - 1) * 2
else:
    print x*(y - 1) + (x - 1) * 2