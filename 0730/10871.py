import sys

n, x = map(int, sys.stdin.readline().split())
my_arr = list(map(int, sys.stdin.readline().split()))
result = []
for i in range(n):
    if x > my_arr[i]:
        result.append(my_arr[i])

for i in result:
    print(i, end=' ')
