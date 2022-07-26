import sys
from collections import deque

def BFS(start):
    time = 0
    queue = deque()
    queue.append((start, time))
    while queue:
        start, time = queue.popleft()
        if not visited[start]:
            if start == k:
                return time
            
            visited[start] = True
            time += 1
            
            if (start + 1) < 100001:
                queue.append((start + 1, time))
            if (start * 2) < 100001:
                queue.append((start * 2, time))
            if (start - 1) >= 0:
                queue.append((start - 1, time))
    return
    

n, k = map(int, sys.stdin.readline().split())   # n: 현재 k:도착
visited = [False] * 100001
print(BFS(n))