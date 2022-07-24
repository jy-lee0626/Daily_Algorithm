import sys

sys.stdin = open('input.txt')

T = int(input())  # text case


for tc in range(1, T+1):
    grid = [[0] * 10 for _ in range(10)]  # 10X10 격자
    N = int(input())
    result = 0
    for i in range(N):
        arr = list(map(int, input().split()))
        if arr[4] == 1:   # 빨간색일 경우
            for k in range(arr[0], arr[2] + 1): # x 첫번째 부터 x 끝까지
                for m in range(arr[1], arr[3] + 1): # y 첫번째 부터 y 끝까지
                    if grid[k][m] == 2:
                        grid[k][m] = 3
                    else:
                        grid[k][m] = 1
        elif arr[4] == 2:  # 파란색일 경우
            for k in range(arr[0], arr[2] + 1): # x 첫번째 부터 x 끝까지
                for m in range(arr[1], arr[3] + 1): # y 첫번째 부터 y 끝까지
                    if grid[k][m] == 1:
                        grid[k][m] = 3
                    else:
                        grid[k][m] = 2

    for i in grid:
        for k in i:
            if k == 3:
                result += 1


    print('#{} {}'.format(tc, result))

