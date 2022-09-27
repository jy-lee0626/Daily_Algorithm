import sys

num = int(sys.stdin.readline())

a = 1
star = 1
vacumm = num - 1
while a < num * 2:
  print(' ' * vacumm + '*' * star)
  if a > num - 1:
    star -= 2
    vacumm += 1
  else:
    star += 2
    vacumm -= 1
  a += 1
  