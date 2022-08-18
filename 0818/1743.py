import sys
from collections import deque

def BFS(x, y):
  trash = 0
  lst = deque([(x, y)])
  visited[x][y] = 1
  while lst:
    trash += 1
    x, y = lst.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and my_arr[nx][ny]:
        lst.append((nx, ny))
        visited[nx][ny] = 1
  return trash

n, m, k = map(int, sys.stdin.readline().rstrip().split())

my_arr = [[0] * m for _ in range(n)]
for _ in range(k):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  my_arr[x - 1][y - 1] = 1

visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
isBreak = False

for i in range(n):
  for j in range(m):
    if my_arr[i][j] and not visited[i][j]:
      value = BFS(i, j)
      if value > result:
        result = value
        if result == k:
          isBreak = True
          break
  if isBreak:
    break
  
print(result)