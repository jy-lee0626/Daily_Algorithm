import sys
result = ['D', 'C', 'B', 'A', 'E']

for i in range(3):
  lst = list(map(int, sys.stdin.readline().split()))
  cnt = lst.count(1)
  print(result[cnt])