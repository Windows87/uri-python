a, b, c = (raw_input()).split(' ')
a = int(a)
b = int(b)
c = int(c)
m = (a+b+abs(a-b))/2
m = (m+c+abs(m-c))/2

print(str(m) + " eh o maior")
