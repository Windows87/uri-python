n = input()
mcs = []
lans = []

for nIndex in range(n):
    lan = raw_input()
    mc = raw_input()
    lans.insert(len(lans), lan)
    mcs.insert(len(mcs), mc)

n = input()

for nIndex in range(n):
    nam = raw_input()
    lan = raw_input()
    print nam
    print mcs[lans.index(lan)]
    print ''