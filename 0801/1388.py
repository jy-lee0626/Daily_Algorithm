import sys

def DFS(x, y):
    visited[x][y] = True
    
    if my_arr[x][y] == '-':
        if y + 1 < m and my_arr[x][y + 1] == '-':
            DFS(x, y + 1)
    elif my_arr[x][y] == '|':
        if x + 1 < n and my_arr[x + 1][y] == '|':
            DFS(x + 1, y)
            

n, m = map(int, sys.stdin.readline().split())

my_arr = [list(str(sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            result += 1
            DFS(i, j)
            
print(result)