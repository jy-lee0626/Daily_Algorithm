import sys

result = 0
now = 0

for _ in range(10):
  down, up = map(int, sys.stdin.readline().split())
  now -= down
  now += up
  if now > result:
    result = now
print(result)