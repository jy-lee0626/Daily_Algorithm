import sys

lst = list(range(1, 31))
for i in range(28):
    num = int(sys.stdin.readline())
    lst.remove(num)
print(lst[0])
print(lst[1])