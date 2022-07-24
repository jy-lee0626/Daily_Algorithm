import sys

sys.stdin = open('input.txt')

# index 2부터 시작해서 T-2까지 양 옆 2칸씩 숫자를 비교한다.
# 기준점 - 양 옆 4개의 숫자 중 가장큰 수 = 세대수에 추가해준다.

for tc in range(1, 11):
    # 1개의 테스트 케이스가 끝나면 초기화 해준다.
    T = int(input())
    lst = list(map(int, input().split()))
    result = 0

    # 처음 2개와 마지막 2개는 0으로 고정임으로 'list index out of range Error' 를 방지하기 위해 2 ~ T-2 까지 설정해준다.
    for i in range(2, T - 2):
        # 빌딩 하나 끝나면 초기화
        a = 0
        # 기준이 되는 빌딩 양 옆 2칸씩 비교해서 기준 빌딩이 제일 높다면 실행
        if lst[i] > lst[i - 2] and lst[i] > lst[i - 1] and lst[i] > lst[i + 1] and lst[i] > lst[i + 2]:
            # 양 옆 빌딩들 중 가장 높은 빌딩을 찾는다.
            a = max(lst[i - 2], lst[i - 1], lst[i + 1], lst[i + 2])
            # 기준 빌딩 - 가장 높은 빌딩을 빼준 값을 result에 추가해준다.
            result += (lst[i] - a)

    print('#{} {}'.format(tc, result))

