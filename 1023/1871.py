import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
  lst = list(map(str, sys.stdin.readline().rstrip().split('-')))
  a = ((ord(lst[0][0]) - 65) * 26 ** 2 + (ord(lst[0][1]) - 65) * 26 + ord(lst[0][2]) - 65)
  b = int(lst[1])

  if abs(a - b) <= 100:
    print('nice')
  else:
    print('not nice')