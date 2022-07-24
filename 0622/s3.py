import sys

sys.stdin = open('input.txt')

T = 10  # test case number


for tc in range(1, T+1):
    col = int(input())
    arr = list(map(int, input().split()))
    result = 0
    i = 2
    while i < col - 2:
        max_num = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        if arr[i] > max_num:
            result += arr[i] - max_num
            i += 3
        else:
            i += 1

    print('#{} {}'.format(tc, result))

