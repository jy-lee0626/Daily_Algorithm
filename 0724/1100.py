import sys

sys.stdin = open('input.txt')

arr = [list(map(str, input().split())) for _ in range(8) ]

cnt = 0


for i in range(8):
    for j in range(8):
        if i%2 and j%2 and arr[i][0][j] == 'F':       # x좌표가 홀수 and y좌표가 홀수 일 때
            cnt += 1
        elif i%2 == 0 and j%2 == 0 and arr[i][0][j] == 'F':  # x좌표가 짝수 and y좌표가 짝수 일 때
            cnt += 1

print(cnt)