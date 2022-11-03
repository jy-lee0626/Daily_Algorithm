import sys

bird = int(sys.stdin.readline())
n = 1
time = 0

while bird:
  if n > bird:
    n = 1
    time -= 1
  else:
    bird -= n
    n += 1

  time += 1

print(time)