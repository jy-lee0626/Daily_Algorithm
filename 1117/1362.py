import sys

N = 0
while True:
  N += 1
  die = False
  # continue_function = True
  o, w = map(int, sys.stdin.readline().split())
  if not o:
    break
  while True:
    action, num = map(str, sys.stdin.readline().split())
    if action == 'F':
      w += int(num)
    elif action == 'E':
      w -= int(num)
    else:
      break
    
    if w <= 0:
      die = True

  if die or w <= 0:
    face = 'RIP'
  elif 0.5 * o < w < 2 * o:
    face = ':-)'
  else:
    face = ':-('
    
  print('{} {}'.format(N, face))