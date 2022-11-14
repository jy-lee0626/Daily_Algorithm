import sys

n = str(sys.stdin.readline().rstrip())
f = int(sys.stdin.readline().rstrip())
new_number = int(n[0:-2] + '00')
if new_number % f:
  sum_num = f - (new_number % f)
  new_number = str(new_number + sum_num)
  print(new_number[-2:])
else:
  print('00')
