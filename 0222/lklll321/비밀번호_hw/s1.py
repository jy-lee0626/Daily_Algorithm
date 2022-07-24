import sys

sys.stdin = open('input.txt')

T = 10  # test case number

for tc in range(1, T+1):
    N, password = map(list, input().split())
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            password.pop(i)
            password.pop(i)
            i = 0
        else:
            i += 1
    result = ''.join(password)
    print('#{} {}'.format(tc, result))

