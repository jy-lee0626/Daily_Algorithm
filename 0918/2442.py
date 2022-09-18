import sys

n = int(sys.stdin.readline())

max_num = 2*n-1
middle = max_num//2
star = 1

for i in range(n):
  print(' ' * middle + '*' * star)
  middle -= 1
  star += 2
  
