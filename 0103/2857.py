import sys

zero = 0
for i in range(1, 6):
  value = str(sys.stdin.readline().rstrip())
  if 'FBI' in value:
    print(i, end=' ')
    zero += 1
    
if not zero:
  print('HE GOT AWAY!')