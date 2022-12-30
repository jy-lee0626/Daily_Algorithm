import sys

lst = []
for i in range(7):
  num = int(sys.stdin.readline().rstrip())
  if num % 2:
    lst.append(num)

if lst:
  print(sum(lst), min(lst), sep='\n')
else:
  print(-1)
