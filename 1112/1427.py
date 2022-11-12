import sys

Num = list(str(sys.stdin.readline().rstrip()))
result = sorted(Num, reverse=True)

for i in result:
  print(i, end='')