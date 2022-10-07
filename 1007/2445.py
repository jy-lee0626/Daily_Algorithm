import sys

num = int(sys.stdin.readline())
star = 1
blank = num - 1
for i in range(num * 2 - 1):
    print('*' * star + ' ' * blank, end='')
    print(' ' * blank + '*' * star)
    if i > num - 2:
        star -= 1
        blank += 1
    else:
        star += 1
        blank -= 1
