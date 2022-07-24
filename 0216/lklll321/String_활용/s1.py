import sys

sys.stdin = open('input.txt', encoding='UTF8')

T = 10   # 10개의 test case

for tc in range(1, T+1):
    num = int(input())  # test case number
    my_str = input()
    target_str = input()
    M = len(my_str)
    N = len(target_str)
    cnt = 0
    for i in range(N - M + 1):
        if target_str[i:M + i] == my_str:
            cnt += 1

    print('#{} {}'.format(tc, cnt))

