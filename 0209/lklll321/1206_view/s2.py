import sys

sys.stdin = open('input.txt')

# ---- code ----

for i in range(10):
    n = int(input())
    t = list(map(int, input().split()))
    result = 0              # 조망권이 갖춰진 총 세대수를 저장할 변수
    for j in range(2, n-2):
        total = min([t[j]-t[j-2], t[j]-t[j-1], t[j]-t[j+1], t[j]-t[j+2]])
        # total = 해당 세대의 좌우 총 4칸 중 가장 높은 세대와의 차
        if total > 0:       # 조망권이 갖춰진 세대라면
            result += total # 총 세대수에 더한다
    print(f'#{i+1} {result}')
