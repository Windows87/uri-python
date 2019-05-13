a = 7
for i in range(10):
    if i % 2 != 0:
        print("I="+str(i)+" J=" + str(a))
        print("I="+str(i)+" J=" + str(a-1))
        print("I="+str(i)+" J=" + str(a-2))
        a+=2