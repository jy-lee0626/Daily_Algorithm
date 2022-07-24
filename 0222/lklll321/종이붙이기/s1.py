def paper(n):
    if n == 0:
        return 1
    elif n == 1:
        return 3
    else:
        return paper(n-1) + 2 * paper(n-2)

import sys

sys.stdin = open('input.txt')

T = int(input())  # test case number

for tc in range(1, T+1):
    N = int(input())  # 가로길이
    n = N // 10 - 1 # index

    print('#{} {}'.format(tc, paper(n)))

