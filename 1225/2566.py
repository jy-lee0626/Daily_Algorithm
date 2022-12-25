import sys

result = 0
x = 0
y = 0

for i in range(9):
  lst = list(map(int, sys.stdin.readline().split()))
  for j, value in enumerate(lst):
    if value >= result:
      x, y = i + 1, j + 1
      result = value

print(result)
print(x, y)