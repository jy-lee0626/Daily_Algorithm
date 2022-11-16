import sys

a, b, c = map(int, sys.stdin.readline().split())
my_arr = [0] * (a + b + c + 1)
for i in range(1, a + 1):
  for j in range(1, b + 1):
    for k in range(1, c + 1):
      my_arr[i + j + k] += 1
  
max_num = max(my_arr)
print(my_arr.index(max_num))