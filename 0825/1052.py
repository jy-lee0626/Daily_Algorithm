import sys

N, K = map(int, sys.stdin.readline().split())

bottle_cnt = 0

while bin(N).count('1') > K:
  idx = bin(N)[::-1].index('1')
  bottle_cnt += 2**idx
  N += 2**idx

print(bottle_cnt)


