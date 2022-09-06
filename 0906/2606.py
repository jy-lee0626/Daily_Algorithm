import sys
from collections import deque

def BFS(start):
    result = 0
    arr = deque([start])
    visited[start] = 1
    while arr:
        now_computer = arr.popleft()
        for idx, connec in enumerate(connect[now_computer]):
            if connec and not visited[idx]:
                arr.append(idx)
                visited[idx] = 1
                result += 1
    return result


computer = int(sys.stdin.readline().rstrip())
connect = [[0] * (computer + 1) for _ in range(computer + 1)]
visited = [0] * (computer + 1)
num = int(sys.stdin.readline().rstrip())


for _ in range(num):
    x, y = map(int, sys.stdin.readline().split())
    connect[x][y] = 1
    connect[y][x] = 1

print(BFS(1))