import sys
from collections import deque

sys.stdin = open('input.txt')

def BFS(start):
    cnt = 0
    queue = deque()
    visited = [0] * (n + 1)
    visited[start] = 1
    queue.append(start)
    while queue:
        computer = queue.popleft()
        for i in my_arr[computer]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = 1
    return cnt


n, m = map(int, sys.stdin.readline().rstrip().split())
my_arr = [[] for _ in range(n + 1)]

for i in range(m):
    y, x = map(int, sys.stdin.readline().rstrip().split())
    my_arr[x].append(y)

hacked = 0
result = []

for i in range(1, n + 1):
    count = BFS(i)
    if count > hacked:
        result.clear()
        hacked = count
        result.append(i)
    elif count == hacked:
        result.append(i)


print(*result)