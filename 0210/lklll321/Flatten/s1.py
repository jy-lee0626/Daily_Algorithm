import sys

sys.stdin = open('input.txt')

'''
리스트에 최고점을 찾고 -1 해준다.
리스트에 최저점을 찾고 +1 해준다.
덤프 횟수 만큼 반복한다. 
최고점 - 최저점을 반환한다.

-> 
상자의 순서는 상관없다.
max 값과 min 값만 찾으면 될 거 같다.
'''
for n in range(1, 11):   # 10개의 테스트 케이스가 주어진다.
    T = int(input())  # 덤프 횟수
    result = 0   # 반환값
    arr = list(map(int, input().split()))  # 상자의 높이 리스트
    for tc in range(1, T+1):
        arr.sort()  # 정렬해준다.
        arr[0] += 1   # 최저점에 상자를 하나 쌓는다.
        arr[-1] -= 1   #최고점에 상자를 하나 뺀다.

    result = max(arr) - min(arr)  # 리스트 안에서 최고점 - 최저점을 반환한다.

    print('#{} {}'.format(n, result))

