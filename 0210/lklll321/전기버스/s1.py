import sys

sys.stdin = open('input.txt')

T = int(input())

# N 개의 리스트를 0으로 채우고 정류장이 있는 인덱스 마다 +1 해준다
# 만약 M의 간격이 K 보다 크면 0을 출력하게 한다.
# k 간격 안에서 가장 뒤에 있는 충전소 M 을 선택한다.
# 충전소 위치로 현재 위치를 이동한다.
# 충전 횟수 카운팅 해준다.

for tc in range(1, T+1):
    K, N, M = map(int, input().split()) # K, N, M 값 뽑기
    charge_station = list(map(int, input().split())) # 충전소 위치
    station = [0] * N  # 정류장
    location = 0  # 현재 위치
    charge_count = 0  # 충전횟수

    for i in charge_station:
        station[i] += 1  # 충전소가 있는 정류장에 1을 더해준다.

    try:                   # IndexError 가 발생하면 0 값을 반환
        while location < N - K:
            t = station[location+1:location+K+1] # k 범위 안에 정류장을 멀리 있는 순서대로
            t.reverse()  # 뒤에서 부터 인덱스 찾기 위해 reverse 해준다.
            far_charge = K - t.index(1)  # 인덱스 위치 찾기
            charge_count += 1       # 충전한 횟수 더해준다.
            location += far_charge  # 이동한 정류장 만큼 위치 변경

        print('#{} {}'.format(tc, charge_count))

    except ValueError:
        print('#{} 0'.format(tc))