import sys

for i in range(3):
  num = int(sys.stdin.readline().rstrip())
  result = 0
  for j in range(num):
    result += int(sys.stdin.readline().rstrip())
  
  if result == 0:
    print('0')
  elif result > 0:
    print('+')
  else:
    print('-')
