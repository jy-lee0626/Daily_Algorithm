import sys

num = int(sys.stdin.readline().rstrip())
arr = [1, 2, 3]

for i in range(num):
  a, b = map(int, sys.stdin.readline().split())
  x = arr.index(a)
  y = arr.index(b)
  arr[x], arr[y] = arr[y], arr[x]
  
print(arr[0])