x = input()
n = x
s = 0

if x <= 2000:
    print "Isento"

if x >= 0:
  n -= 2000
  
if x >= 2000.01:
  if n > 1000:
    s += 80
  else:
    s += n / 100 * 8
  n -= 1000

if x >= 3000.01:
  if n > 1500:
    s += 15 / 1 * 18
  else:
    s += n / 100 * 18
  n -= 1500
  
if x > 4500:
  s += n / 100 * 28

print ("R$ {:.2f}").format(s)