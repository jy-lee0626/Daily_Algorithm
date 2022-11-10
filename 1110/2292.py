import sys

N = int(sys.stdin.readline())
a = 1
time = 1

while True:
  if N <= a:
    break
  a += 6 * time
  time += 1

print(time)