import sys

def BFS(x, y, time):
    time += 1

    if not my_arr[x][y] or visited[x][y] or time >= result:
        return

    if x == n and y == m:
        if time < result :
            result = time

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            

sys.stdin = open('input.txt')

x, y = map(int, sys.stdin.readline().split())
my_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(x)]
visited = [[0] * y for _ in range(x)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = x - 1
m = y - 1

result = 1000000
BFS(0, 0, 0)
print(result)

