import sys

S = str(sys.stdin.readline())

for i in range(ord('a'), ord('z') + 1):
    a = chr(i)
    print(S.count(a), end=' ')