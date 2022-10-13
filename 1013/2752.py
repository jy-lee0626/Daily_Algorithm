import sys

lst = list(map(int, sys.stdin.readline().split()))
result = sorted(lst)
print(*result)