import sys

h, m, s = map(int, sys.stdin.readline().split(":"))

cnt = 0

if 1 <= h <= 12:
  cnt += 1
if 1 <= m <= 12:
  cnt += 1
if 1 <= s <= 12:
  cnt += 1
if 60 <= h or 60 <= m or 60 <= s:
  cnt = 0

if not cnt:
  print(0)
elif cnt == 1:
  print(2)
elif cnt == 2:
  print(4)
elif cnt == 3:
  print(6)