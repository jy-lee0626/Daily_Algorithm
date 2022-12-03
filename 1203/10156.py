import sys

k, n, m = map(int, sys.stdin.readline().split())
total = k * n

if total > m:
  print(total - m)
else:
  print(0)