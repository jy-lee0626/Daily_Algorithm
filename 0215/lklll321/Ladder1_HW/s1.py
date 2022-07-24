import sys

sys.stdin = open('input.txt')

T = 10  # test case
'''
x를 찾아서 거꾸로 올라가자!
100x100 크기의 2차원 배열
-> 100번째 list에서 2를 찾고 1을 따라서 거꾸로 올라간다.
문제에서 x 와 y 를 반대로 줬다. -> 마지막에 바꾸면 될듯
'''

for tc in range(1, T+1):
    N = int(input())  # test case number
    arr = [list(map(int, input().split())) for _ in range(100)]  # 100개의 리스트
    dx = -1  # 델타 x 방향
    x = 99    # x 시작 위치

    for k in range(100):  # 도착지점 찾기
        if arr[99][k] == 2:
           y = k

    while x > 0:  # x 가 0 될 때까지 반복
        x = x + dx  # 처음에는 무조건 위로 올라간다.
        if 0 < y and arr[x][y - 1] == 1:  # 왼쪽에 1이 있으면 왼쪽으로 이동
            while 0 < y and arr[x][y - 1] == 1:  # 왼쪽이 더 이상 1이 아닐 때 까지 이동
                y -= 1
        elif y < 99 and arr[x][y + 1] == 1:  # 오른쪽에 1이 있으면 오른쪽으로 이동
            while y < 99 and arr[x][y + 1] == 1:  # 오른쪽이 더 이상 1이 아닐 때 까지 이동
                y += 1

    print('#{} {}'.format(N, y))

