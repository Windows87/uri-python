x = input()
t = 0

for i in range(x):
  y, z = (raw_input()).split(' ')
  if y == '1001':
      t += 1.5 * int(z)
  elif y == '1002':
      t += 2.5 * int(z)
  elif y == '1003':
      t += 3.5 * int(z)
  elif y == '1004':
      t += 4.5 * int(z)
  else:
      t += 5.5 * int(z)

print ('{:.2f}').format(t)
