import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
a_arr = list(map(int, sys.stdin.readline().split()))
b_arr = list(map(int, sys.stdin.readline().split()))

result = 0

a_arr.sort(reverse=True)
b_arr.sort()

for i in range(N):
  result += a_arr[i] * b_arr[i]

print(result)