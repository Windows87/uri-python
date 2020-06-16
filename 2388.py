n = int(input())
t = 0

for i in range(n):
    T, v = raw_input().split(' ')
    t += int(T) * int(v)

print(t)