import sys
sys.stdin = open('input.txt')

T = int(input())                        # test case number
def BFS(x, y, value, cnt):
    global result
    value += arr[x][y]
    cnt += 1

    if cnt == 4:
        if value > result:
            result = value
        return

    if y % 2:                               # 홀수면
        for i in range(6):
            nx = x + dx_h[i]
            ny = y + dy_h[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                visited[nx][ny] = 1
                BFS(nx, ny, value, cnt)
                visited[nx][ny] = 0
    else:                                   # 짝수면
        for i in range(6):
            nx = x + dx_j[i]
            ny = y + dy_j[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                visited[nx][ny] = 1
                BFS(nx, ny, value, cnt)
                visited[nx][ny] = 0

for test in range(1, T+1):
    w, h = map(int, input().split())        # w: y, h: x
    arr = []
    visited = [[0] * w for _ in range(h)]
    result = 0
    dx_j = [-1, 1, 0, 0, -1, -1]            # 짝수 일 때
    dy_j = [0, 0, 1, -1, 1, -1]
    dx_h = [-1, 1, 0, 0, 1, 1]              # 홀수 일 때
    dy_h = [0, 0, 1, -1, 1, -1]
    for _ in range(h):
        lst = list(map(int, input().split()))
        arr.append(lst)

    for i in range(h):                      # 0, 0 부터 탐색
        for j in range(w):
            visited[i][j] = 1
            BFS(i, j, 0, 0)
            visited[i][j] = 0
    print('#{} {}'.format(test, result ** 2))
