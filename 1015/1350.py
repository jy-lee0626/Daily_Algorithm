import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
cluster = int(sys.stdin.readline().rstrip())
result = 0

for i in lst:
  a = i // cluster
  b = i % cluster
  if b:
    a += 1
  result += a * cluster

print(result)