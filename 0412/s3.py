def BFS(x, y, user):
    global result
    visited = [[0] * W for _ in range(H)]
    heap = []
    heap.append((user, x, y))
    n = 0
    ans = 0
    while n < 4:
        heap.sort(reverse=True)
        user, x, y = heap.pop(0)
        if visited[x][y]:
            continue
        ans += user
        visited[x][y] = 1
        if y % 2:  # 홀수
            for p in range(6):
                ni = x + di_h[p]
                nj = y + dj_h[p]
                if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj]:
                    heap.append((cell[ni][nj], ni, nj))
        else:  # 짝수
            for t in range(6):
                ni = x + di_j[t]
                nj = y + dj_j[t]
                if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj]:
                    heap.append((cell[ni][nj], ni, nj))
        n += 1

    if ans > result:
        result = ans


import sys
sys.stdin = open('input1.txt')

T = int(input())  # test case number


for tc in range(1, T + 1):
    W, H = map(int, input().split())  # 가로, 세로
    cell = [list(map(int, input().split())) for _ in range(H)]  # Cell
    result = 0

    di_h = [-1, 1, 0, 0, 1, 1]
    dj_h = [0, 0, -1, 1, -1, 1]
    di_j = [-1, 1, 0, 0, -1, -1]
    dj_j = [0, 0, -1, 1, -1, 1]

    for i in range(H):
        for j in range(W):
            BFS(i, j, cell[i][j])

    print('#{} {}'.format(tc, result ** 2))