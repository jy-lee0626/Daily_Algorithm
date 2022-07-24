def bracket(text):
    num_a = 0  # () 괄호 검사
    num_b = 0  # {} 괄호 검사
    lst = []
    for i in text:   # 괄호만 lst 에 담기
        if i == '(':
            num_a += 1
            lst.append(i)
        elif i == ')':
            num_a -= 1
            lst.append(i)
        elif i == '{':
            num_b += 1
            lst.append(i)
        elif i == '}':
            num_b -= 1
            lst.append(i)
        elif num_a < 0 or num_b < 0:  # 한번이라도 음수가 나오면 0 반환
            return 0

    for k in lst:
        if k == ')':
            if c == '{':
                return 0
        elif k == '}':
            if c == '(':
                return 0
        c = k

    if num_a + num_b:  # num_a , num_b 둘 다 0이면 1 반환 아니면 0 반환
        return 0
    return 1

import sys

sys.stdin = open('input.txt')

T = int(input())  # test case number

for tc in range(1, T+1):
    text = input()  # text
    print('#{} {}'.format(tc, bracket(text)))

