import sys
from collections import deque

def BFS(x, y):
  global result
  lst = deque([(x, y, 1)])
  visited[x][y] = 1
  
  while lst:
    x, y, cnt = lst.popleft()    
    if x == n - 1 and y == m - 1 and cnt < result:
      result = cnt
      
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and my_arr[nx][ny] and not visited[nx][ny]:
        lst.append((nx, ny, cnt + 1))
        visited[nx][ny] = 1
    
    
n, m = map(int, sys.stdin.readline().rstrip().split())
my_arr = []
for i in range(n):
  num = str(sys.stdin.readline().rstrip())
  new_arr = []
  for j in num:
    new_arr.append(int(j))
  my_arr.append(new_arr)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0] * m for _ in range(n)]
result = 999999999999999

BFS(0, 0)
print(result)