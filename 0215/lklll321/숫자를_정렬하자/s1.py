import sys

sys.stdin = open('input.txt')

T = int(input())  # test case

for tc in range(1, T+1):
    N = int(input())  # 숫자가 몇개인지
    arr = list(map(int, input().split()))
    for i in range(N - 1):
        for k in range(N - 1 - i):  # 큰 수 부터 뒤로 배치
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]


    print('#{}'.format(tc), end=' ')
    print(*arr)

