import sys

x, y = map(str, sys.stdin.readline().split())
x = x[::-1]
y = y[::-1]
k = str(int(x) + int(y))
print(k[::-1])
