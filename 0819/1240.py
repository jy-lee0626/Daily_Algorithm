import sys
from collections import deque

def BFS(start, end, result):
  global answer
  
  if start == end:
    return answer.append(result)

  lst = deque()
  
  for idx, dist in enumerate(my_arr[start]):
    if dist and not visited[idx]:
      if idx == end:
        lst.clear()
        lst.append(idx)
        break
      else:
        lst.append(idx)
  
  while lst:
    new_start = lst.popleft()
    visited[new_start] = 1
    distance = my_arr[start][new_start]
    BFS(new_start, end, result + distance)
    visited[new_start] = 0
    
  
  

n, m = map(int, sys.stdin.readline().rstrip().split())
my_arr = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(n - 1):
  x, y, distance = map(int, sys.stdin.readline().rstrip().split())
  my_arr[x][y] = distance
  my_arr[y][x] = distance
  
for i in range(m):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  answer = []
  BFS(x, y, 0)
  print(min(answer))