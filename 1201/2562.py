import sys

idx = 0
max_num = 0
for i in range(1, 10):
  num = int(sys.stdin.readline().rstrip())
  if num > max_num:
    max_num = num
    idx = i
print(max_num)
print(idx)
