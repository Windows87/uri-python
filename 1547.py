n = input()

for nIndex in range(n):
    n2, numR = raw_input().split(' ')
    nums = raw_input().split(' ')
    
    numR = int(numR)
    difR = 200
    pos = 0
    index = 0

    for num in nums:
        dif = numR - int(num)
        if dif < 0:
            dif = -(dif)
        
        if difR > dif:
            pos = index
            difR = dif

        index += 1

    print pos + 1