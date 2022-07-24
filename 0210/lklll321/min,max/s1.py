import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())     # 양수의 개수
    arr = list(map(int, input().split()))   # 양의 정수들
    int_list = []           # 리스트 초기화
    result = 0          # result 값 초기화

    int_list = sorted(arr)       # 리스트를 오름차순으로 정렬해준다.
    result = int_list[-1] - int_list[0]      # 가장 큰 수에서 가장 작은 수 빼기

    print('#{} {}'.format(tc, result))

