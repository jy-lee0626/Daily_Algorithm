import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
  num = int(sys.stdin.readline().rstrip())
  result = sum(map(int, sys.stdin.readline().split()))
  print(result)