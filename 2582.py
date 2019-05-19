x = input()
l = ["PROXYCITY", "P.Y.N.G.", "DNSUEY!", "SERVERS",
     "HOST!", "CRIPTONIZE", "OFFLINE DAY", "SALT",
     "ANSWER!", "RAR?", "WIFI ANTENNAS"]

for i in range(x):
    y = (raw_input()).split(' ')
    a = int(y[0])
    b = int(y[1])
    print(l[a + b])
