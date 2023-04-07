import sys

my_str = str(sys.stdin.readline().rstrip())
N = len(my_str)
for i in range(N//10 + 1):
  print(my_str[10 * i:10 * i + 10])