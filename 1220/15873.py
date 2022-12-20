import sys

result = 0
a = str(sys.stdin.readline().rstrip())

for i in a:
  if not int(i):
    result += 9
  else:
    result += int(i)
print(result)