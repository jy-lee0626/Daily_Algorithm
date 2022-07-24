import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    list_nm = list(map(int, input().split())) # N, M 값 뽑아주기
    N = list_nm[0]      # list 갯수
    M = list_nm[1]      # 몇개씩 할건지
    max_value = 0       # max 값 초기화
    list_value = list(map(int, input().split()))  # 정수들
    min_value = sum(list_value[0:0 + M])  # min 값 초기설정

    for i in range(N - M + 1):   # N-M+1 만큼 반복
        if sum(list_value[i:i+M]) > max_value:  # max 값 비교하기
            max_value = sum(list_value[i:i+M])  # 새로운 값이 더 크면 max 바꾸기
        if sum(list_value[i:i+M]) < min_value:  # min 값 비교하기
            min_value = sum(list_value[i:i+M])  # 새로운 값이 더 작으면 min 바꾸기

    result = max_value - min_value   # 결과에 max - min 저장

    print('#{} {}'.format(tc, result))

