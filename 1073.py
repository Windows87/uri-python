x = int(input()) + 1

for i in range(x):
    if i % 2 == 0 and i != 0:
        print(str(i) + "^2 = " + str(i**2))
