import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):   # case 10개
    T = int(input())  # case number
    arr = [list(map(int, input().split())) for _ in range(100)] # 2차원 배열
    lst = []  # 빈 리스트
    z = 0   # 우하향 대각선 값
    k = 0   # 좌하향 대각선 값
    for i in range(100):
        x = 0
        y = 0
        for j in range(100):
            x += arr[i][j]    # row 한줄 씩 계산하기
            y += arr[j][i]    # column 한줄 씩 계산하기

            if i == j:
                z += arr[i][j]

            if i + j == 99:
                k += arr[i][j]
        lst.append(x)   # 리스트에 추가
        lst.append(y)   # 리스트에 추가
    lst.append(z)
    lst.append(k)
    result = max(lst)

    print('#{} {}'.format(T, result))

