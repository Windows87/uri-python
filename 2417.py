cV, cE, cS, fV, fE, fS = raw_input().split(' ')
cP = int(cV) * 3 + int(cE)
fP = int(fV) * 3 + int(fE)

if(cP > fP):
    print 'C'
elif fP > cP:
    print 'F'
elif int(cS) > int(fS):
    print 'C'
elif int(fS) > int(cS):
    print 'F'
else:
    print '='