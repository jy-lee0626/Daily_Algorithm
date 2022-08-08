import sys
from collections import deque

sys.stdin = open('input.txt')

def BFS(a, b, t):
    if t:
        my_str = 'W'
    else:
        my_str = 'B'
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and my_arr[nx][ny] == my_str:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return cnt ** 2


n, m = map(int, sys.stdin.readline().rstrip().split())  # n : 가로  m : 세로
my_arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

white = 0
blue = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if my_arr[i][j] == 'W':
                white += BFS(i, j, 1)
            else:
                blue += BFS(i, j, 0)

print(white, blue)

