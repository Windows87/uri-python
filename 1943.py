x = input()

if x == 1:
    print "Top 1"
elif x <= 3:
    print "Top 3"
elif x <= 5:
    print "Top 5"
elif x <= 10:
    print "Top 10"
elif x <= 25:
    print "Top 25"
elif x <= 50:
    print "Top 50"
else:
    print "Top 100"