import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  for i in range(b):
    print('X' * a)
  print()