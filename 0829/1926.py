import sys
from collections import deque

def DFS(x, y):
    global result
    ans = 0

    my_lst = deque([(x, y)])
    visited[x][y] = 1

    while my_lst:
        x, y = my_lst.popleft()
        ans += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                my_lst.append((nx, ny))

    if ans > result:
        result = ans




n, m = map(int, sys.stdin.readline().split())
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    arr.append(lst)

visited = [[0] * m for _ in range(n)]
cnt = 0
result = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            cnt += 1
            DFS(i, j)

print(cnt)
print(result)