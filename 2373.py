n = input()
caiu = 0

for nIndex in range(n):
    latas, copos = raw_input().split(' ')
    if int(latas) > int(copos):
        caiu += int(copos)

print caiu