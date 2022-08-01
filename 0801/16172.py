import sys

my_str = str(sys.stdin.readline().rstrip())
find_str = str(sys.stdin.readline().rstrip())

real_str = ''

for i in my_str:
    if not ord('0') <= ord(i) <= ord('9'):
        real_str += i

if find_str in real_str:
    print(1)
else:
    print(0)