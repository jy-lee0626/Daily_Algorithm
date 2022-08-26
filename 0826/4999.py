import sys

say = str(sys.stdin.readline().rstrip())
hear = str(sys.stdin.readline().rstrip())

if len(say) >= len(hear):
  print('go')
else:
  print('no')