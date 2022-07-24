import sys

sys.stdin = open('input.txt')

T = int(input())  # test case number


for tc in range(1, T+1):
    day = int(input())
    arr = list(map(int, input().split()))
    max_num = arr.pop()
    result = 0
    while arr:
        now = arr.pop()
        if max_num < now:
            max_num = now
        else:
            result += max_num - now

    print('#{} {}'.format(tc, result))

