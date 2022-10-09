import sys

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
if lst[0] == lst[1] == lst[2]:
    print(10000 + lst[0] * 1000)
elif lst[0] == lst[1] or lst[1] == lst[2]:
    print(1000 + lst[1] * 100)
else:
    print(lst[2] * 100)

