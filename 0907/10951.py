import sys

while True:
  try:
    a, b = map(int, sys.stdin.readline().split())
    if a and b:
      print(a + b)
  except:
    break