import sys

k, d, a = map(int, sys.stdin.readline().split('/'))
if k + a < d or not d:
  print('hasu')
else:
  print('gosu')