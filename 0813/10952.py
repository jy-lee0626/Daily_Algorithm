import sys

while True:
  a, b = map(int, sys.stdin.readline().rstrip().split())
  if a and b:
    print(a + b)
  else:
    break