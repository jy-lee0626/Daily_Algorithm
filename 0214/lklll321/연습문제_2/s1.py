import sys

sys.stdin = open('input.txt')

T = int(input())  # testcase

for tc in range(1, T+1):
    N = int(input())   # N*N 2차 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    num = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    num += abs(arr[i][j] - arr[ni][nj])

    print('#{} {}'.format(tc, num))
<<<<<<< HEAD
=======

>>>>>>> ad8c79219617003e365cf5c82e3362709c0ec56b
