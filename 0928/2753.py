import sys

num = int(sys.stdin.readline())

if not num % 4:
  if num % 100 or not num % 400:
    print(1)
  else:
    print(0)
else:
  print(0)