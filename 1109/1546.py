import sys

N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
max_num = max(lst)
sum_num = 0
for i in range(N):
  sum_num += lst[i] / max_num * 100

print("{:.6f}".format(sum_num / N))