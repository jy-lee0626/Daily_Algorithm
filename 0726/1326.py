import sys
from collections import deque

def BFS(start, end):
    visited = [-1] * (n + 1)
    queue = deque()
    queue.append(start)
    visited[start] = 0
    while queue:
        now = queue.popleft()
        for i in range(now, n + 1, my_arr[now]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[now] + 1
                if i == end:
                    return visited[i]
        for i in range(now, 0, -my_arr[now]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[now] + 1
                if i == end:
                    return visited[i]
    return -1

n = int(sys.stdin.readline())
my_arr = [0] + list(map(int, sys.stdin.readline().split()))
start, end = map(int, sys.stdin.readline().split())
    
print(BFS(start, end))
