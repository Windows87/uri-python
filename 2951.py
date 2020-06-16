n, g = raw_input().split(' ')

n = int(n)
g = int(g)

runs = {}

for i in range(n):
    x, y = raw_input().split(' ')

    runs[x] = int(y)

X = input()

R = raw_input().split(' ')
t = 0

for i in R:
    t += runs[i]

print(t)

if t >= g:
    print('You shall pass!')
else:
    print('My precioooous')