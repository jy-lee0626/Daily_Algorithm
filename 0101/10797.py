import sys

result = 0
num = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))

for i in lst:
  if num == i:
    result += 1

print(result)
