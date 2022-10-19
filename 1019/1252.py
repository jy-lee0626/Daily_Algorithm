import sys

a, b = map(str, sys.stdin.readline().split())
sum_num = bin(int(a, 2) + int(b, 2))
result = str(sum_num).replace('0b', '')
print(result)