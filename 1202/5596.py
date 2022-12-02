import sys

minkook = sum(map(int, sys.stdin.readline().split()))
manse = sum(map(int, sys.stdin.readline().split()))
print(max(minkook, manse))