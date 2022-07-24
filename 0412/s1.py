def DFS(x, y, cnt, user):
    global ans

    if cnt == 4:
        print(visited, user)
        if ans < user:

            ans = user

    if y % 2:  # 홀수
        for i in range(6):
            ni = x + di_h[i]
            nj = y + dj_h[i]
            if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj] and cnt < 4:
                visited[ni][nj] = 1
                DFS(ni, nj, cnt + 1, user + cell[ni][nj])
                visited[ni][nj] = 0
    else:  # 짝수
        for i in range(6):
            ni = x + di_j[i]
            nj = y + dj_j[i]
            if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj] and cnt < 4:
                visited[ni][nj] = 1
                DFS(ni, nj, cnt + 1, user + cell[ni][nj])
                visited[ni][nj] = 0

import sys

sys.stdin = open('input1.txt')

T = int(input())  # test case number


for tc in range(1, 2):
    W, H = map(int, input().split())  # 가로, 세로
    cell = [list(map(int, input().split())) for _ in range(H)]  # Cell
    ans = 0
    visited = [[0] * W for _ in range(H)]
    di_h = [-1, 1, 0, 0, 1, 1]
    dj_h = [0, 0, -1, 1, -1, 1]
    di_j = [-1, 1, 0, 0, -1, -1]
    dj_j = [0, 0, -1, 1, -1, 1]

    for i in range(H):
        for j in range(W):
            print(i, j)
            visited[i][j] = 1
            DFS(i, j, 1, cell[i][j])
            visited[i][j] = 0
    print(ans)
    print(440 + 190 + 450 + 420)
    print('#{} {}'.format(tc, ans**2))

