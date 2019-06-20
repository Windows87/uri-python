renas = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']
nums = raw_input().split(' ')
som = 0

for num in nums:
    som += int(num)

i = 0
for i2 in range(som):
    if i == 8:
        i = 0
    else:
        i += 1

print renas[i - 1]