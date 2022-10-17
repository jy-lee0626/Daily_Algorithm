import sys

lst = []
for i in range(5):
  value = int(sys.stdin.readline().rstrip())
  lst.append(value)

a = lst[1] // lst[3] + (1 if lst[1] % lst[3] else 0)
b = lst[2] // lst[4] + (1 if lst[2] % lst[4] else 0)
max_num = max(a, b)
print(lst[0] - max_num)