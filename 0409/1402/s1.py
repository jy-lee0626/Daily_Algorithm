def find(a, b):
    lst = []
    for i in range(1, a + 1):
        if not a % i:
            if b == i + a // i:
                print('yes')
                return
            lst.append(i + a // i)

    lst = set(lst)

    for j in lst:
        for k in range(1, j + 1):
            if not a % k:
                if b == k + a // k:
                    print('yes')
                    return
    print('no')

import sys

sys.stdin = open('input.txt')

T = int(input())  # test case number


for tc in range(1, T+1):
    a, b = map(int, input().split())
    find(a, b)


