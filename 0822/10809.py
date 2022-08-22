import sys

s = str(sys.stdin.readline())

for i in range(ord('a'), ord('z') + 1):
  print(s.find(chr(i)), end=' ')