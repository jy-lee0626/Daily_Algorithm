import sys
from collections import deque

def BFS(x, y):
  arr = deque([(x, y)])
  visited[x][y] = 1
  
  while arr:
    x, y = arr.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] > high and not visited[nx][ny]:
        arr.append((nx, ny))
        visited[nx][ny] = 1
        
result = 1
maps = []
N = int(sys.stdin.readline().rstrip())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
  lst = list(map(int, sys.stdin.readline().split()))
  maps.append(lst)
    
for high in range(1, 101):
  visited = [[0] * N for _ in range(N)]
  cnt = 0
  for i in range(N):
    for j in range(N):
      if maps[i][j] > high and not visited[i][j]:
        BFS(i, j)
        cnt += 1 
  if cnt > result:
    result = cnt

print(result)