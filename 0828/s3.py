import sys
from collections import deque
from copy import deepcopy

sys.stdin = open('input.txt')

def DFS(cnt):
    global result
    global core, arr

    if not core:
        if cnt < result:
            result = cnt
        return

    x, y = core.popleft()

    if arr[x - 1][y] == 1 and arr[x + 1][y] == 1 and arr[x][y - 1] == 1 and arr[x][y + 1] == 1:
        DFS(cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        lst = arr[:]
        number = cnt
        while True:
            if nx == -1 or nx == N or ny == -1 or ny == N:
                DFS(cnt)
                arr = lst[:]

            if not arr[nx][ny]:
                arr[nx][ny] = 2
                cnt += 1
            elif arr[nx][ny] and 0 <= nx < N and 0 <= ny < N:
                arr = lst
                cnt = number
                break

            nx += dx[i]
            ny += dy[i]

T = int(input())


for tc in range(1, T+1):
    arr = []
    core = deque()
    N = int(input())
    result = 999999999999
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for _ in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)

    for i in range(1, N):
        for j in range(1, N):
            if arr[i][j]:
                core.append([i, j])

    DFS(0)

    print('#{} '.format(tc, ))

