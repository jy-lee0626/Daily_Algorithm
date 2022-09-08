import sys

n = int(sys.stdin.readline().rstrip())
a = ' '
b = '*'
for i in range(1, n + 1):
  print(a * (n - i) + b * i)