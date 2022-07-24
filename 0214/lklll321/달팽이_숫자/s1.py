import sys

sys.stdin = open('input.txt')

T = int(input())  # test case

for tc in range(1, T+1):
    N = int(input())  # N*N 2차 배열인지
    arr = [[0 for _ in range(N)] for _ in range(N)]  # N*N 2차 배열
    num = 0  # 행렬에 넣을 숫자
    i = 0
    j = 0
    while num <= (1 << N):
        arr[i][j] = num
        pass
        # 모르겠다.

        num += 1


    print('#{} '.format(tc, ))
