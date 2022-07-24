import sys

sys.stdin = open('input.txt')

T = int(input())  # test case

for tc in range(1, T+1):
    t, page_A, page_B = map(int, input().split())  # r : 전체 페이지, page_A : A 가 찾을 페이지, page_B : B 가 찾을 페이지
    r = t
    c = r//2   # 페이지 절반
    A = 1
    B = 1
    l = 1

    while c != page_A:
        if c < page_A:
            l = c
            c = int((l + r) / 2)
        elif c > page_A:
            r = c
            c = int((c + l) / 2)
        A += 1

    r = t
    c = r//2    # c 초기화
    l = 1
    while c != page_B:
        if c < page_B:
            l = c
            c = int((l + r) / 2)
        elif c > page_B:
            r = c
            c = int((c + l) / 2)
        B += 1


    if A > B:
        result = 'B'
    elif A == B:
        result = 0
    elif A < B:
        result = 'A'

    print('#{} {}'.format(tc, result))

