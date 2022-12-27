import sys

lst = []
n = 0
N, K = map(int, sys.stdin.readline().split())

for i in range(N, 0, -1):
  if not N % i and N / i not in lst:
    lst.append(N // i)
    n += 1
    if n == K:
      break

if len(lst) >= K:
  print(lst[K - 1])
else:
  print(0)