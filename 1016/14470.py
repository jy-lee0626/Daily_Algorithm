import sys

time = 0

start = int(sys.stdin.readline().rstrip())
end = int(sys.stdin.readline().rstrip())
minus = int(sys.stdin.readline().rstrip())
thaw = int(sys.stdin.readline().rstrip())
plus = int(sys.stdin.readline().rstrip())

if start < 0:
  time += abs(start) * minus
  time += thaw
  time += end * plus
elif start > 0:
  time += (end - start) * plus
else:
  time += thaw
  time += end * plus
print(time)