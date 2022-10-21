import sys

n = int(sys.stdin.readline())
blank = ' '
blank_num = n - 1
star_num = 1
for i in range(1, n * 2):
  if i >= n:
    print(blank * blank_num + '*' * star_num)
    blank_num += 1
    star_num -= 1
  else:
    print(blank * blank_num + '*' * star_num)
    blank_num -= 1
    star_num += 1