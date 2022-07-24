import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    c = [0] * 11   # 빈 리스트 설정 -> indexError 방지 11개로 만들기
    N = int(input())     # 카드의 갯수
    card_list = list(map(int, input()))   # 카드 리스트
    num_max = 0     # 가장 많은 숫자 초기화

    for i in card_list:   # 리스트에서 숫자 뽑기
        c[i] += 1       # 뽑은 숫자로 count + 1 해주기

    j = 0      # while 을 위한 변수 j
    while j < 10:
        if c[j] >= c[num_max]:   # c 숫자 비교
            num_max = j   # 가장 많은 숫자
        j += 1     # 다음 비교

    print('#{} {} {}'.format(tc, num_max, c[num_max]))

