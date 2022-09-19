import sys

num = int(sys.stdin.readline())
num_list = str(sys.stdin.readline())
result = 0

for i in range(num):
  result += int(num_list[i])
  
print(result)