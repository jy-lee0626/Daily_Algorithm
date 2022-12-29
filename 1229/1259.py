import sys

while True:
  value = str(sys.stdin.readline().rstrip())
  if value != '0':
    cnt = len(value)//2
    result = True
    for i in range(cnt):
      if value[i] == value[-i-1]:
        pass
      else:
        result = False

    print('yes' if result else 'no')
  else:
    break
