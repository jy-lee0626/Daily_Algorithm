import sys

num = int(sys.stdin.readline())
n = 0
vacuum = ' '
star = '*'
vacuum_num = 0
star_num = 0
while n < num * 2 - 1:
  print(vacuum * vacuum_num + star * (num * 2 - (star_num * 2 + 1)))
  
  n += 1
  if n > num - 1:
    star_num -= 1
    vacuum_num -= 1
  else:
    star_num += 1
    vacuum_num += 1
    