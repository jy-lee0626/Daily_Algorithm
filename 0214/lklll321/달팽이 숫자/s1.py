import sys

sys.stdin = open('input.txt')

T = int(input())  # test case

for tc in range(1, T+1):
    N = int(input())  # N*N 2차 배열인지
    arr = [[0 for _ in range(N)] for _ in range(N)]  # N*N 2차 배열
    num = 1  # 행렬에 넣을 숫자
    direction = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i = 0
    j = 0

    while num <= N*N:
        if 0 <= i < N and 0 <= j < N and not arr[i][j]:
            arr[i][j] = num
            num += 1
        else:
            direction += 1
            if i >= N:
                i -= 1
            elif i < 0:
                i += 1
            elif j >= N:
                j -= 1
            elif j < 0:
                j += 1
            elif arr[i][j]:
                direction = direction % 4
                i = oi + di[direction]
                j = oj + dj[direction]
                continue

        direction = direction % 4
        oi = i
        oj = j
        i = i + di[direction]
        j = j + dj[direction]



    print('#{} {}'.format(tc, arr))

