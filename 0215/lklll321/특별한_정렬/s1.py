#1.
import sys

sys.stdin = open('input.txt')

T = int(input())  # text case

for tc in range(1, T+1):
    N = int(input())  # 리스트 갯수
    arr = list(map(int, input().split()))
    arr.sort()
    arr_rev = list(reversed(arr))
    result = [0] * N
    index_1 = 0
    index_2 = 0
    for i in range(N):
        if i%2:
            result[i] = arr[index_1]
            index_1 += 1
        else:
            result[i] = arr_rev[index_2]
            index_2 += 1

    if N % 2:  # N이 홀수이면 가운데 빈곳에 넣어주기
        result[N//2] = arr[N//2]

    print('#{} '.format(tc, ), end='')
    for i in range(10):
        print(result[i], end=' ')
    print()
