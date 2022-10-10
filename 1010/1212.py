import sys

num = str(sys.stdin.readline().rstrip())
oct_num = int(num, 8)
print(bin(oct_num)[2:])
