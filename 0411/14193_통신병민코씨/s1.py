def find(r, c):
    q = deque()
    q.append(arr[r][c])
    while q:


import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())  # test case number


for tc in range(1, T+1):
    x, y = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(y)]
    for i in range(x):
        for j in range(y):
            if arr[i][j] == 'S':
                find(i, j)
                break
    print('#{} '.format(tc, ))

