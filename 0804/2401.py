import sys

my_str = str(sys.stdin.readline().rstrip())
Num = int(sys.stdin.readline().rstrip())
result = 0

for i in range(Num):
    short = str(sys.stdin.readline().rstrip())
    for j in short:
        if j in my_str:
            my_str = my_str.lstrip(short)
            result += len(short)
    print(my_str, 'here')

print(result)
