import sys

result = 0
while True:
  n = int(sys.stdin.readline().rstrip())
  if n == -1:
    break
  result += n

print(result)