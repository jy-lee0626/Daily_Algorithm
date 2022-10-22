import sys

n = int(sys.stdin.readline().rstrip())
user = list(map(int, sys.stdin.readline().split()))
lst = []
result = 0

for i in user:
  if i in lst:
    result += 1
  else:
    lst.append(i)
    
print(result)