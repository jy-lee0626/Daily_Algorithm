import sys

'''
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7
'''
N = int(sys.stdin.readline().rstrip())
for i in range(1, N + 1):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #{}: {} + {} = {}'.format(i, a, b, a + b))