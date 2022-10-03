import sys

num = int(sys.stdin.readline().rstrip())
result = int(sys.stdin.readline().rstrip())

for i in range(num - 1):
  new_concent = int(sys.stdin.readline().rstrip())
  if new_concent > 1:
    result += new_concent - 1
print(result)