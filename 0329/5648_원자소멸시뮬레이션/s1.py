import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())                                # 원자의 갯수
    dx = [0, 0, -1, 1]                              # 좌우
    dy = [1, -1, 0, 0]                              # 상하

    lst = []
    for i in range(N):
        x, y, direct, k = map(int, input().split())
        x += 1000                                   # 0, 0 을 원점으로 만들기
        y += 1000
        lst.append([x, y, direct, k])

    result = 0

    while len(lst) > 1:
        for i, j in enumerate(lst):                 # 1초가 지났을 때 좌표
            x = j[0] + dx[j[2]]
            y = j[1] + dy[j[2]]
            if 0 <= x <= 2000 and 0 <= y <= 2000:
                j = [x, y, j[2], j[3]]
                lst[i] = j
            else:                                   # 범위를 벗어나면
                lst.pop(i)                          # 제거


        for l in range(len(lst) - 1):
            for m in range(l + 1, len(lst)):
                n = 0
                k = 0
                while n < 2:
                    if lst[l][0] == lst[m][0] and lst[l][1] == lst[m][1]:  # 1초 후 좌표가 같으면
                        result += lst[l][3]
                        result += lst[m][3]
                        lst.pop(l)
                        lst.pop(m - 1)
                        k += 1
                    n += 1
                if k >=1:
                    break
                if abs(lst[l][0] - lst[m][0]) == 1 and lst[l][1] == lst[m][1]:  # x 좌표가 1만큼만 차이나면
                    if lst[l][2] == 2 and lst[m][2] == 3:   # 방향이 서로 충돌하는 방향이면
                        result += lst[l][3]
                        result += lst[m][3]
                        lst.pop(l)
                        lst.pop(m - 1)
                        break
                    elif lst[l][2] == 3 and lst[m][2] == 2:
                        result += lst[l][3]
                        result += lst[m][3]
                        lst.pop(l)
                        lst.pop(m - 1)
                        break
                elif abs(lst[l][1] - lst[m][1]) == 1 and lst[l][0] == lst[m][0]:  # y 좌표가 1만큼만 차이나면
                    if lst[l][2] == 0 and lst[m][2] == 1:
                        result += lst[l][3]
                        result += lst[m][3]
                        lst.pop(l)
                        lst.pop(m - 1)
                        break
                    elif lst[l][2] == 1 and lst[m][2] == 0:
                        result += lst[l][3]
                        result += lst[m][3]
                        lst.pop(l)
                        lst.pop(m - 1)
                        break

    print('#{} {}'.format(tc, result))

