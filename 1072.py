x = int(input())
n = 0

for i in range(x):
    y = int(input())
    if y >= 10 and y <= 20:
        n+=1

print(str(n) + " in")
print(str(x - n) + " out")
