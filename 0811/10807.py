import sys

n = sys.stdin.readline().rstrip()

my_arr = list(map(int, sys.stdin.readline().rstrip().split()))
a = int(sys.stdin.readline().rstrip())
print(my_arr.count(a))