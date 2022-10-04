import sys

num = int(sys.stdin.readline().rstrip())
call = list(map(int, sys.stdin.readline().split()))
Y = 0
M = 0

for i in call:
  Y += (i // 30 + 1) * 10
  M += (i // 60 + 1) * 15

if Y > M:
  print('M', M)
elif M > Y:
  print('Y', Y)
else:
  print("Y M", Y)