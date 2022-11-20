import sys

N, M, L = map(int, sys.stdin.readline().split())
result = 0
lst = [0] * N
idx = 0
while True:
  lst[idx] += 1
  if lst[idx] == M:
    break
  if lst[idx] % 2:
    idx += L
    if idx >= N:
      idx -= N
  else:
    idx -= L
    if idx < 0:
      idx += N
  result += 1
  
print(result)