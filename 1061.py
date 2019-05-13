d = int((input()).split(' ')[1])
y = (input()).split(' ')
h = int(y[0])
m = int(y[2])
sI = int(y[4])

sI += d*24*60*60+h*60*60+m*60

d = int((input()).split(' ')[1])
y = (input()).split(' ')
h = int(y[0])
m = int(y[2])
sF = int(y[4])

sF += d*24*60*60+h*60*60+m*60
sT = sF - sI

print(str(int(sT/86400)) + " dia(s)")
sT -= int(sT/86400) * 86400
print(str(int(sT/3600)) + " hora(s)")
sT -= int(sT/3600) * 3600
print(str(int(sT/60)) + " minuto(s)")
sT -= int(sT/60) * 60
print(str(sT) + " segundo(s)")
