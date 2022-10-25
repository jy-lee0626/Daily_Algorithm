import sys

total, win = map(int, sys.stdin.readline().split())
win_rate = win * 100 // total
cnt = 0

if win_rate >= 99:
  print(-1)
else:
  left = 1
  right = total
  while left <= right:
    mid = (left + right) // 2
    if (win + mid) * 100 // (total + mid) <= win_rate:
      left = mid + 1
    else:
      cnt = mid
      right = mid - 1
  print(cnt)