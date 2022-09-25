import sys

h, m = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline())

m = time + m

if m >= 60:
  h += m // 60
  m = m % 60

if h > 23:
  h = h - 24
  
print(h, m)