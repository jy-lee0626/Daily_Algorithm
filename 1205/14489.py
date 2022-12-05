import sys

a, b = map(int, sys.stdin.readline().split())
chicken = int(sys.stdin.readline().rstrip())

if (a + b) >= 2 * chicken:
  print((a + b) - 2 * chicken)
else:
  print(a + b)