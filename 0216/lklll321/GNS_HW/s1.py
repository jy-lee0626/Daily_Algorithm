import sys

sys.stdin = open('input.txt')

T = int(input())  # test case

for tc in range(1, T+1):
    N, num = input().split()  # test case num, test case 갯수
    arr = list(input().split())  # list
    lst_str = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    lst_tuple = {}
    lst = []  # 빈 리스트 만들기
    result = []  # 결과 값
    for i in range(len(lst_str)):   # 튜플에 keys, values 로 묶어주기
        lst_tuple[lst_str[i]] = i

    for j in arr:  # arr list 를 key 로 이용해 value 값 뽑아주기
        a = lst_tuple.get(j)    # get 을 이용해 value 값인 숫자를 가져온다.
        lst.append(a)           # 새로운 list 에 숫자들을 추가한다.
    lst.sort()   # 정렬해준다.
    lst_rever = {v:k for k, v in lst_tuple.items()}  # 튜플의 keys 와 values 바꿔주기

    for k in lst:  # 정렬한 숫자를 keys 로 활용해 values 뽑아오기
        b = lst_rever.get(k)
        result.append(b)

    print('#{}'.format(tc))
    print(*result)

