import sys

while True:
  a, b, c = map(str, sys.stdin.readline().split())
  
  if a == '#':
    break
  elif b > '17' or c >= '80':
    print(a + ' Senior')
  else:
    print(a + ' Junior')