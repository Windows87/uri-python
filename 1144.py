x = input()

for i in range(x):
    i+=1
    for i2 in range(2):
        print(str(i) + " " + str(i**2 + i2) + " " + str(i**3 + i2))
