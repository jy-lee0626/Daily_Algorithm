import sys

a, b = map(int, sys.stdin.readline().split())
x1, y1 = a//4, a%4
x2, y2 = b//4, b%4

if not y1:
  y1 = 4
  x1 -= 1
  
if not y2:
  y2 = 4
  x2 -= 1
  
print(abs(x2 - x1) + abs(y2 - y1))