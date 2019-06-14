n = input()

for nIndex in range(n):
    n2 = input()
    some = True
    first = ""

    for n2Index in range(n2):
        if not first:
            first = raw_input()
        else:
            if first != raw_input():
                some = False
    
    if some:
        print first
    else:
        print "ingles"