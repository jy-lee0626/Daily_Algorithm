import sys

sys.stdin = open('input.txt')

T = int(input())  # 배열의 크기
arr = [list(map(int, input().split())) for _ in range(T)]

# 1. 행우선
arr_c = []
for r in range(T):
    for c in range(T):
        arr_c.append(arr[r][c])
print(*arr_c)

# 2. 열우선
arr_r = []
for c in range(T):
    for r in range(T):
        arr_r.append(arr[r][c])
print(*arr_r)

# 3. 지그재그
arr_zig = []
for r in range(T):
    for c in range(T):
        arr_zig.append(arr[r][c + (T - 1 - 2*c)*(r%2)])
print(*arr_zig)

# 4. 전치행렬
for r in range(T):
    for c in range(T):
        if r < c:
            arr[r][c], arr[c][r] = arr[c][r], arr[r][c]
print(arr)




# for tc in range(1, T+1):
#
#     print('#{} '.format(tc, ))

