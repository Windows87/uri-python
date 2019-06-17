t = raw_input().lower()

try:
    t.index('zelda')
    print "Link Bolado"
except ValueError:
    print "Link Tranquilo"