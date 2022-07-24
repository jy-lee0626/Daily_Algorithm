import sys

sys.stdin = open('input.txt')

T = int(input())   # test case
A = list(range(1, 13))  # 1 ~ 12까지 숫자를 가진 list
'''
원소를 N개 가진 부분 집합들을 만들고
그 부분 집합들의 합이 K이면 result += 1 하기
'''
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N : 부분 집합의 수 , K : 부분 집합의 합
    result = 0
    lst = []  # 빈 리스트 만들기
    for i in range(1 << len(A)):
        lst_a = []
        for j in range(len(A)):
            if i & (1 << j):
                lst_a.append(A[j])
        if len(lst_a) == N and sum(lst_a) == K:
            result += 1

    print('#{} {}'.format(tc, result))

