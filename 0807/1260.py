import sys
from collections import deque

sys.stdin = open('input.txt')

def dfs(start):
    visited[start] = 1
    print(start, end=' ')
    for i in range(1, n + 1):
        if nodes[start][i] and not visited[i]:
            dfs(i)

def bfs(start):
    bfs_visited = [0] * (n + 1)
    stack = deque()
    stack.append(start)
    while stack:
        node = stack.popleft()
        if not bfs_visited[node]:
            print(node, end=' ')
        bfs_visited[node] = 1

        for i in range(1, n + 1):
            if nodes[node][i] and not bfs_visited[i]:
                stack.append(i)

n, m, v = map(int, sys.stdin.readline().rstrip().split())
nodes = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    nodes[x][y] = nodes[y][x] = 1

dfs(v)
print()
bfs(v)