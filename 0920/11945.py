import sys

a, b = map(int, sys.stdin.readline().split())

for i in range(a):
  string = str(sys.stdin.readline().rstrip())
  result = ''
  for j in range(b - 1, -1, -1):
    result += string[j]
  print(result)