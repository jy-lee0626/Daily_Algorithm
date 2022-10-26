import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
  a = str(sys.stdin.readline().rstrip())
  print('{}. {}'.format(i, a))