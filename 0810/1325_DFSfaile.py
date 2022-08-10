import sys
from collections import deque

sys.stdin = open('input.txt')

def DFS(start, computer_number, cnt):
  global result, hacked
  
  visited[computer_number] = 1
  lst = my_arr[computer_number]
  queue = deque()

  for idx, i in enumerate(lst):
      if i and not visited[idx]:
        cnt += 1
        queue.append(idx)
      
  while queue:
      new_computer = queue.pop()
      DFS(start, new_computer, cnt)
  if cnt > hacked:
      hacked = cnt
      result = set()
      result.add(start)
  elif cnt == hacked:
      result.add(start)

n, m = map(int, sys.stdin.readline().rstrip().split())
my_arr = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    y, x = map(int, sys.stdin.readline().rstrip().split())
    my_arr[x][y] = 1
  
hacked = 0
result = set()

for i in range(1, n):
    visited = [0] * (n + 1)
    cnt = 0
    DFS(i, i, cnt)
  
result = list(result)

for i in result:
    print(i, end=" ")