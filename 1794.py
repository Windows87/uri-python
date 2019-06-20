n = input()
LA, LB = raw_input().split(' ')
SA, SB = raw_input().split(' ')

if n >= int(LA) and n <= int(LB) and n >= int(SA) and n <= int(SB):
    print "possivel"
else:
    print "impossivel"